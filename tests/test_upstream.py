"""Checks that the schema renders the release NIST's catalog publishes.

NIST publishes SP 800-53 Release 5.2.0 as an OSCAL catalog, with the SP
800-53A assessment procedures inside it, and the four SP 800-53B baselines as
OSCAL profiles, in usnistgov/oscal-content.
src/nist_sp_800_53/schema/oscal-content/ holds the copies that
scripts/check_upstream_release.py pins. These tests read the copies with the
standard library alone, derive from them the Sp80053Catalog the schema
describes, and hold that catalog to the validator and to the release's
counts.
"""

import hashlib
import importlib.util
import json
import re
from functools import lru_cache
from pathlib import Path

import yaml
from linkml.validator import validate

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "nist_sp_800_53" / "schema" / "nist_sp_800_53.yaml"
COPY = ROOT / "src" / "nist_sp_800_53" / "schema" / "oscal-content"
CATALOG = COPY / "NIST_SP-800-53_rev5_catalog.json"
BASELINES = {
    "LOW": COPY / "NIST_SP-800-53_rev5_LOW-baseline_profile.json",
    "MODERATE": COPY / "NIST_SP-800-53_rev5_MODERATE-baseline_profile.json",
    "HIGH": COPY / "NIST_SP-800-53_rev5_HIGH-baseline_profile.json",
    "PRIVACY": COPY / "NIST_SP-800-53_rev5_PRIVACY-baseline_profile.json",
}
RMF = "http://csrc.nist.gov/ns/rmf"

# The catalog links a control, a family or a statement item inside its prose
# as [AC-2](#ac-2), and a reference as [SP 800-12](#<uuid>). The publication
# prints the identifier bare and the reference label in brackets.
PROSE_LINK = re.compile(r"\[([^\]]*)\]\(#([^)]+)\)")
UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

# What Release 5.2.0 holds, counted over NIST's catalog and baselines: the
# twenty families; the controls and enhancements, with those Revision 5
# withdrew apart; where the withdrawn ones went; and the parameters,
# statements, discussions, objectives, methods, links and references of the
# controls and enhancements that remain.
COUNTS = {
    "families": 20,
    "controls": 324,
    "withdrawn controls": 24,
    "enhancements": 872,
    "withdrawn enhancements": 158,
    "incorporated into": 166,
    "moved to": 34,
    "withdrawn with a reason only": 2,
    "parameters": 1600,
    "aggregating parameters": 142,
    "statements": 1014,
    "statement items": 1122,
    "discussions": 1014,
    "assessment objectives": 3720,
    "assessment methods": 2931,
    "related control links": 3512,
    "required control links": 715,
    "control references": 838,
    "reference documents": 192,
    "reference documents cited by controls": 160,
    "baselines": 4,
}
METHODS = {"EXAMINE": 1013, "INTERVIEW": 1012, "TEST": 906}
BASELINE_SIZES = {"LOW": 149, "MODERATE": 287, "HIGH": 370, "PRIVACY": 96}
FAMILY_IDS = [
    "AC", "AT", "AU", "CA", "CM", "CP", "IA", "IR", "MA", "MP",
    "PE", "PL", "PM", "PS", "PT", "RA", "SA", "SC", "SI", "SR",
]  # fmt: skip


def _watch():
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@lru_cache(maxsize=1)
def _header():
    return yaml.safe_load(SCHEMA.read_text())


@lru_cache(maxsize=1)
def _catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))["catalog"]


@lru_cache(maxsize=1)
def _profiles():
    return {
        level: json.loads(path.read_text(encoding="utf-8"))["profile"]
        for level, path in BASELINES.items()
    }


def _props(element, name, cls=None, ns=None):
    return [
        p["value"]
        for p in element.get("props", [])
        if p["name"] == name and p.get("class") == cls and p.get("ns") == ns
    ]


def _prop(element, name, cls=None, ns=None):
    (value,) = _props(element, name, cls, ns)
    return value


def _parts(element, name):
    return [p for p in element.get("parts", []) if p["name"] == name]


def _links(element, rel):
    return [link["href"].lstrip("#") for link in element.get("links", []) if link["rel"] == rel]


class Derivation:
    """The Sp80053Catalog that NIST's catalog and baseline profiles describe,
    in the schema's terms."""

    def __init__(self, catalog, profiles):
        self.catalog = catalog
        self.profiles = profiles
        self.elements = {}
        self.family_of = {}
        for group in catalog["groups"]:
            self.family_of[group["id"]] = group
            for control in group["controls"]:
                self._index(control)
        resources = catalog["back-matter"]["resources"]
        self.resources = {r["uuid"]: r for r in resources}

    def _index(self, control):
        self.elements[control["id"]] = control
        for enhancement in control.get("controls", []):
            self._index(enhancement)

    def label(self, oscal_id):
        """The identifier the publication prints for a catalog id."""
        if oscal_id in self.elements:
            return _prop(self.elements[oscal_id], "label")
        if oscal_id in self.family_of:
            return _prop(self.family_of[oscal_id], "label")
        control_identifier, sep, path = oscal_id.partition("_smt.")
        if sep and control_identifier in self.elements:
            (statement,) = _parts(self.elements[control_identifier], "statement")
            printed, holder, prefix = self.label(control_identifier), statement, control_identifier + "_smt"
            for segment in path.split("."):
                prefix += "." + segment
                (holder,) = [p for p in holder.get("parts", []) if p["id"] == prefix]
                label = _prop(holder, "label")
                if label.endswith("."):
                    label = label[:-1] if prefix.count(".") == 1 else "." + label[:-1]
                printed += label
            return printed
        raise KeyError(oscal_id)

    def prose(self, text):
        """The prose as the publication prints it: a cited reference in
        brackets by its label, a link to the catalog's own metadata by its
        text, and a linked control, family or statement item by its text,
        which is the identifier as the publication prints it."""

        def replace(match):
            text, target = match.groups()
            if UUID.match(target):
                resource = self.resources[target]
                return f"[{resource['title']}]" if "citation" in resource else text
            assert (
                target in self.elements
                or target in self.family_of
                or "_smt." in target
                or "_odp" in target
                or "_prm_" in target
            ), target
            return text

        return PROSE_LINK.sub(replace, text)

    def statement(self, part):
        entry = {}
        if "prose" in part:
            entry["statement_text"] = self.prose(part["prose"])
        items = [self.item(p) for p in part.get("parts", [])]
        if items:
            entry["statement_items"] = items
        return entry

    def item(self, part):
        assert part["name"] == "item", part["id"]
        entry = {"item_label": _prop(part, "label"), "item_text": self.prose(part["prose"])}
        items = [self.item(p) for p in part.get("parts", [])]
        if items:
            entry["statement_items"] = items
        return entry

    def parameter(self, param):
        entry = {"parameter_id": param["id"]}
        labels = _props(param, "label", "sp800-53a")
        if labels:
            (entry["assessment_label"],) = labels
        if "label" in param:
            entry["parameter_label"] = self.prose(param["label"])
        guidelines = [self.prose(g["prose"]) for g in param.get("guidelines", [])]
        if guidelines:
            entry["parameter_guidelines"] = guidelines
        if "select" in param:
            entry["selection_choices"] = [self.prose(c) for c in param["select"]["choice"]]
            how_many = param["select"].get("how-many")
            if how_many is not None:
                entry["selection_cardinality"] = how_many.upper().replace("-", "_")
        aggregates = _props(param, "aggregates", ns=RMF)
        if aggregates:
            entry["aggregated_parameters"] = aggregates
        alternatives = _props(param, "alt-identifier")
        if alternatives:
            entry["alternative_identifiers"] = alternatives
        alt_labels = _props(param, "alt-label", "sp800-53")
        if alt_labels:
            (entry["alternative_label"],) = alt_labels
        return entry

    def objective(self, part):
        assert part["name"] == "assessment-objective", part["id"]
        entry = {"objective_label": _prop(part, "label", "sp800-53a")}
        if "prose" in part:
            entry["objective_text"] = self.prose(part["prose"])
        subs = [self.objective(p) for p in part.get("parts", [])]
        if subs:
            entry["sub_objectives"] = subs
        return entry

    def method(self, part):
        (objects,) = _parts(part, "assessment-objects")
        return {
            "assessment_method": _prop(part, "method", ns=RMF),
            "assessment_objects": [
                self.prose(line) for line in objects["prose"].split("\n\n") if line.strip()
            ],
        }

    def common(self, control):
        """What a control and an enhancement share, in the schema's slots."""
        entry = {"title": control["title"]}
        statements = _parts(control, "statement")
        status = _props(control, "status")
        if status:
            (entry["control_status"],) = [s.upper() for s in status]
            incorporated = [self.label(t) for t in _links(control, "incorporated-into")]
            moved = [self.label(t) for t in _links(control, "moved-to")]
            if incorporated:
                entry["incorporated_into"] = incorporated
            if moved:
                entry["moved_to"] = moved
            if statements and not incorporated and not moved:
                ((reason,),) = [[s["prose"] for s in statements]]
                entry["withdrawal_reason"] = reason
            return entry
        (statement,) = statements
        entry["control_statement"] = self.statement(statement)
        (guidance,) = _parts(control, "guidance")
        entry["control_discussion"] = self.prose(guidance["prose"])
        params = [self.parameter(p) for p in control.get("params", [])]
        if params:
            entry["control_parameters"] = params
        related = [self.label(t) for t in _links(control, "related")]
        if related:
            entry["related_control_ids"] = related
        references = [self.resources[t]["title"] for t in _links(control, "reference")]
        if references:
            entry["control_references"] = references
        (objective,) = _parts(control, "assessment-objective")
        entry["assessment_objective"] = self.objective(objective)
        entry["assessment_methods"] = [self.method(p) for p in _parts(control, "assessment-method")]
        entry["implementation_level"] = [
            v.upper() for v in _props(control, "implementation-level", ns=RMF)
        ]
        assurance = _props(control, "contributes-to-assurance", ns=RMF)
        if assurance:
            entry["contributes_to_assurance"] = assurance == ["true"]
        return entry

    def enhancement(self, control):
        assert control["class"] == "SP800-53-enhancement", control["id"]
        entry = {"enhancement_id": _prop(control, "label")}
        entry.update(self.common(control))
        required = [self.label(t) for t in _links(control, "required")]
        if required:
            entry["required_controls"] = required
        return entry

    def control(self, control):
        assert control["class"] == "SP800-53", control["id"]
        entry = {"control_identifier": _prop(control, "label")}
        entry.update(self.common(control))
        enhancements = [self.enhancement(e) for e in control.get("controls", [])]
        if enhancements:
            entry["control_enhancements"] = enhancements
        return entry

    def family(self, group):
        assert group["class"] == "family", group["id"]
        entry = {"family_id": _prop(group, "label"), "title": group["title"]}
        overviews = _parts(group, "overview")
        if overviews:
            (overview,) = overviews
            entry["description"] = self.prose(overview["prose"])
        entry["family_controls"] = [self.control(c) for c in group["controls"]]
        return entry

    def baseline(self, level, profile):
        (imported,) = profile["imports"]
        (selection,) = imported["include-controls"]
        return {
            "baseline_level": level,
            "title": profile["metadata"]["title"],
            "baseline_controls": [self.label(i) for i in selection["with-ids"]],
        }

    def reference(self, resource):
        entry = {"reference_label": resource["title"], "reference_citation": resource["citation"]["text"]}
        (rlink,) = resource["rlinks"]
        entry["reference_url"] = rlink["href"]
        return entry

    def derive(self):
        return {
            "catalog_release": self.catalog["metadata"]["version"],
            "control_families": [self.family(g) for g in self.catalog["groups"]],
            "control_baselines": [
                self.baseline(level, profile) for level, profile in self.profiles.items()
            ],
            "catalog_references": [
                self.reference(r) for r in self.resources.values() if "citation" in r
            ],
        }


@lru_cache(maxsize=1)
def _derived():
    return Derivation(_catalog(), _profiles()).derive()


def _controls():
    return [c for f in _derived()["control_families"] for c in f["family_controls"]]


def _enhancements():
    return [e for c in _controls() for e in c.get("control_enhancements", [])]


def _elements():
    return _controls() + _enhancements()


def _active():
    return [e for e in _elements() if "control_status" not in e]


def _withdrawn():
    return [e for e in _elements() if "control_status" in e]


def _identifier(element):
    return element.get("control_identifier") or element["enhancement_id"]


def _walk_items(holder):
    for item in holder.get("statement_items", []):
        yield item
        yield from _walk_items(item)


def _walk_objectives(objective):
    yield objective
    for sub in objective.get("sub_objectives", []):
        yield from _walk_objectives(sub)


def _parameters():
    return [p for e in _active() for p in e.get("control_parameters", [])]


def test_copy_matches_the_pinned_blobs():
    """Every copied file has the git object hash the watch pins, so the copy
    is the file NIST published at the pinned commit, and nothing else is in
    the folder."""
    pinned = _watch().PINNED_BLOBS
    assert {p.name for p in COPY.iterdir()} == set(pinned)
    for name, (_source, sha) in pinned.items():
        assert _blob_sha(COPY / name) == sha, name


def test_header_pins_match_the_watch():
    """The header records the release, commit and publication the watch
    checks."""
    watch = _watch()
    header = _header()
    notes = header["annotations"]
    assert notes["oscal_content_tag"] == watch.PINNED_TAG
    assert notes["oscal_content_commit"] == watch.PINNED_COMMIT
    assert header["source"] == f"https://doi.org/{watch.PINNED_DOI}"
    tree = f"https://github.com/usnistgov/oscal-content/tree/{watch.PINNED_TAG}/"
    assert tree + watch.PINNED_PATH.rpartition("/")[0] in header["see_also"]


def test_catalog_is_the_pinned_release():
    """The copies are NIST's catalog and baselines of the release in the
    header, by the release NIST's reference tool names and the version each
    file's metadata carries."""
    version = _header()["version"]
    identifier = "SP_800_53_" + version.replace(".", "_")
    assert _header()["annotations"]["cprt_framework_version"] == identifier
    assert _catalog()["metadata"]["version"] == version
    for profile in _profiles().values():
        assert profile["metadata"]["version"] == version


def test_derived_catalog_validates():
    """The whole of Release 5.2.0, as the catalog and the baselines give it,
    is a valid Sp80053Catalog."""
    report = validate(_derived(), str(SCHEMA), "Sp80053Catalog")
    assert not report.results, [r.message for r in report.results][:10]


def test_counts_match_the_release():
    """The derived catalog holds what the release holds."""
    active = _active()
    withdrawn = _withdrawn()
    objectives = [o for e in active for o in _walk_objectives(e["assessment_objective"])]
    methods = [m for e in active for m in e["assessment_methods"]]
    references = [r for e in active for r in e.get("control_references", [])]
    counted = {
        "families": len(_derived()["control_families"]),
        "controls": len(_controls()),
        "withdrawn controls": sum(1 for c in _controls() if "control_status" in c),
        "enhancements": len(_enhancements()),
        "withdrawn enhancements": sum(1 for e in _enhancements() if "control_status" in e),
        "incorporated into": sum(len(e.get("incorporated_into", [])) for e in withdrawn),
        "moved to": sum(len(e.get("moved_to", [])) for e in withdrawn),
        "withdrawn with a reason only": sum(1 for e in withdrawn if "withdrawal_reason" in e),
        "parameters": len(_parameters()),
        "aggregating parameters": sum(1 for p in _parameters() if "aggregated_parameters" in p),
        "statements": len(active),
        "statement items": sum(1 for e in active for _ in _walk_items(e["control_statement"])),
        "discussions": len(active),
        "assessment objectives": len(objectives),
        "assessment methods": len(methods),
        "related control links": sum(len(e.get("related_control_ids", [])) for e in active),
        "required control links": sum(len(e.get("required_controls", [])) for e in _enhancements()),
        "control references": len(references),
        "reference documents": len(_derived()["catalog_references"]),
        "reference documents cited by controls": len(set(references)),
        "baselines": len(_derived()["control_baselines"]),
    }
    assert counted == COUNTS
    assert {k: sum(1 for m in methods if m["assessment_method"] == k) for k in METHODS} == METHODS
    assert {
        b["baseline_level"]: len(b["baseline_controls"]) for b in _derived()["control_baselines"]
    } == BASELINE_SIZES


def test_identifiers_nest_and_are_unique():
    """Each identifier starts with the identifier of what holds it, which no
    pattern in the schema can check, and none repeats."""
    seen = []
    for family in _derived()["control_families"]:
        seen.append(family["family_id"])
        for control in family["family_controls"]:
            assert control["control_identifier"].startswith(family["family_id"] + "-")
            seen.append(control["control_identifier"])
            for enhancement in control.get("control_enhancements", []):
                assert enhancement["enhancement_id"].startswith(control["control_identifier"] + "(")
                seen.append(enhancement["enhancement_id"])
    assert len(seen) == len(set(seen))
    assert [f["family_id"] for f in _derived()["control_families"]] == FAMILY_IDS
    parameters = [p["parameter_id"] for p in _parameters()]
    assert len(parameters) == len(set(parameters))


def test_every_cited_identifier_names_an_element():
    """A related or required control, a baseline's selection, a moved-to
    target and an aggregated parameter each name something the catalog
    defines, which no pattern can check."""
    identifiers = {_identifier(e) for e in _elements()}
    parameters = {p["parameter_id"] for p in _parameters()}
    for element in _active():
        assert set(element.get("related_control_ids", [])) <= identifiers, _identifier(element)
        assert set(element.get("required_controls", [])) <= identifiers, _identifier(element)
        for parameter in element.get("control_parameters", []):
            assert set(parameter.get("aggregated_parameters", [])) <= parameters
    for element in _withdrawn():
        assert set(element.get("moved_to", [])) <= identifiers, _identifier(element)
    for baseline in _derived()["control_baselines"]:
        assert set(baseline["baseline_controls"]) <= identifiers, baseline["baseline_level"]
        assert len(baseline["baseline_controls"]) == len(set(baseline["baseline_controls"]))


def test_withdrawn_elements_say_where_they_went():
    """A withdrawn control or enhancement carries where it was incorporated,
    where it moved, or the catalog's reason, and nothing an active one
    carries; an active one carries its statement, discussion, objective and
    methods and no withdrawal slot."""
    for element in _withdrawn():
        assert element["control_status"] == "WITHDRAWN"
        went = [k for k in ("incorporated_into", "moved_to", "withdrawal_reason") if k in element]
        assert went, _identifier(element)
        assert not {"control_statement", "control_discussion", "assessment_objective"} & set(element)
    for element in _active():
        assert not {"incorporated_into", "moved_to", "withdrawal_reason"} & set(element)
        assert element["assessment_methods"], _identifier(element)
    reasons = {_identifier(e): e["withdrawal_reason"] for e in _withdrawn() if "withdrawal_reason" in e}
    assert set(reasons) == {"CP-10(3)", "SC-19"}
    assert [e["incorporated_into"] for e in _withdrawn() if _identifier(e) == "AC-2(10)"] == [["AC-2k"]]
    assert [e["incorporated_into"] for e in _withdrawn() if _identifier(e) == "SA-12"] == [["SR"]]


def test_parameters_are_assignments_or_selections():
    """A parameter carries a label or selection choices, never both and never
    neither, and a placeholder in any text names a parameter of the
    catalog."""
    parameters = {p["parameter_id"] for p in _parameters()}
    for parameter in _parameters():
        assert ("parameter_label" in parameter) != ("selection_choices" in parameter), parameter
    placeholders = re.compile(r"\{\{\s*insert:\s*param,\s*([^\s}]+)\s*\}\}")
    text = json.dumps(_derived())
    cited = set(placeholders.findall(text))
    assert cited and cited <= parameters, sorted(cited - parameters)[:5]
    assert "](#" not in text


def test_control_references_name_listed_documents():
    """Every reference a control cites is one of the catalog's references."""
    labels = {r["reference_label"] for r in _derived()["catalog_references"]}
    assert len(labels) == len(_derived()["catalog_references"])
    for element in _active():
        assert set(element.get("control_references", [])) <= labels, _identifier(element)
