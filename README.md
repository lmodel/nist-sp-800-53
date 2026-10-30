<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-sp-800-53

NIST SP 800-53 Security and Privacy Controls Release 5.2.0 with SP 800-53A and SP 800-53B (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project, for example which controls the privacy baseline selects. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-sp-800-53](https://lmodel.github.io/nist-sp-800-53)

## What it models

The security and privacy controls that the National Institute of Standards and Technology (NIST) defines in [Special Publication (SP) 800-53, Revision 5](https://doi.org/10.6028/NIST.SP.800-53r5), at Release 5.2.0 of August 2025, with the assessment procedures of [SP 800-53A](https://doi.org/10.6028/NIST.SP.800-53Ar5) and the control baselines of [SP 800-53B](https://doi.org/10.6028/NIST.SP.800-53B):

* **Families** (`Sp80053Family`): the twenty families the controls are sorted into, Access Control (AC) to Supply Chain Risk Management (SR).
* **Controls** (`Sp80053Control`): the 324 controls, each with an identifier such as `AC-2`, its statement and the statement's items, its discussion, its organization-defined parameters, its related controls and the publications it cites. Revision 5 withdrew 24 of them; each keeps its identifier and says where it was incorporated or moved, or, for SC-19, why it was withdrawn.
* **Control enhancements** (`Sp80053ControlEnhancement`): the 872 enhancements, each with an identifier such as `AC-2(1)`, what a control carries, and the control it requires. 158 are withdrawn.
* **Organization-defined parameters** (`Sp80053Parameter`): the 1,600 assignments and selections the statements leave to the organization, with the labels and guidelines SP 800-53A gives them.
* **Assessment objectives and methods** (`Sp80053AssessmentObjective`, `Sp80053AssessmentMethod`): the 3,720 assessment objectives (2,792 determination statements and 928 headings) and the 2,931 examine, interview and test methods of SP 800-53A, one set for each active control and enhancement.
* **References** (`Sp80053Reference`): the 192 publications the catalog lists, 160 of them cited by a control, by the labels the catalog gives them, such as `SP 800-12`.
* **Baselines** (`Sp80053Baseline`): the Low (149 selections), Moderate (287), High (370) and Privacy (96) baselines of SP 800-53B, each a list of control and enhancement identifiers.
* **The catalog** (`Sp80053Catalog`): one release as a single document that holds all of these.

The schema header's `version` is the release of Revision 5, 5.2.0, as NIST's Cybersecurity and Privacy Reference Tool numbers it (`SP_800_53_5_2_0`). Its `source` is the publication's digital object identifier (DOI). NIST also publishes the catalog, with the SP 800-53A procedures inside it, and the four baselines in the Open Security Controls Assessment Language (OSCAL). [src/nist_sp_800_53/schema/oscal-content/](src/nist_sp_800_53/schema/oscal-content) holds those five files as usnistgov/oscal-content released them in v1.6.0, matched to the release by git object hash. `tests/test_upstream.py` derives the whole release from the copies, validates it, and holds it to the counts above. A weekly workflow opens an issue when NIST registers the next final edition, changes a copied file, or the copy drifts.

Revision 5 was published in September 2020 and updated in December 2020. Release 5.2.0 is its current release, and no later release or Revision 6 exists. Release tags number the schema's versions.

## Influences

None beyond SP 800-53, SP 800-53A and SP 800-53B: the schema renders the three publications. Its layout follows [lmodel/nist-sp-800-218](https://github.com/lmodel/nist-sp-800-218), and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

The schema crosses to OSCAL and borrows nothing from it. NIST's catalog renders each element as an OSCAL one:

* a family as a group;
* a control and an enhancement as controls;
* a statement, a discussion, an assessment objective and an assessment method as parts;
* a parameter as a parameter;
* a reference as a back-matter resource;
* a baseline as a profile.

Each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`, because the OSCAL class is the more general one.

## Not modelled here

* The four resolved baseline catalogs that usnistgov/oscal-content publishes beside the profiles: they repeat the catalog's controls, and a baseline here is the list of identifiers the profile selects.
* The catalog's own OSCAL metadata and the back-matter entries about the catalog, such as the links to the PDF and to earlier OSCAL releases.
* Each objective's link to the statement item it assesses, which the nesting of the objectives already shows.
* NIST's Cybersecurity and Privacy Reference Tool exports of the same release: the tool gives no release or hash to pin, and the identifier it gives the release is in the schema's annotations.
* SP 800-53 Revision 4, which usnistgov/oscal-content still carries, and the parts of SP 800-53A and SP 800-53B that the catalog and the profiles do not carry, such as SP 800-53B's tailoring guidance.
* The rules no pattern can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/nist_sp_800_53/schema/](src/nist_sp_800_53/schema): the LinkML schema, `nist_sp_800_53.yaml` (edit this), and NIST's catalog and baseline copies
* [src/nist_sp_800_53/datamodel/](src/nist_sp_800_53/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/nist-sp-800-53.yaml`, which `lokf adapt` writes from `src/nist_sp_800_53/schema/nist_sp_800_53.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-sp-800-53.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. `project.justfile` names the classes the copy roots on `Concept`, and a concept may name any of them as its `type`. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
Sp80053Family, Sp80053Control, Sp80053ControlEnhancement, Sp80053Baseline
```

A concept writes the publication's identifier in `family_id`, `control_identifier` or `enhancement_id`, and a baseline's level in `baseline_level`. An enhancement's concept names its control's concept in `isPartOf`, and a control's concept names its family's. A name and a description are the concept's own `title` and `description`.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's or with the copies of slsa, github-actions, oscal, spdx and nist-sp-800-218. A slot shares a name only where it carries LOKF's meaning and Internationalized Resource Identifier (IRI), as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing. The copy shares no other key with the five neighbours, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

SP 800-53, SP 800-53A and SP 800-53B are works of the United States Government and are not subject to copyright in the United States. The schema's descriptions are this project's own words. NIST's catalog and baselines in [src/nist_sp_800_53/schema/oscal-content/](src/nist_sp_800_53/schema/oscal-content) keep NIST's licence beside them: see [NOTICE](NOTICE).

This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
