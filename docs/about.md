# About nist-sp-800-53

Electronic (LinkML) Version of NIST SP 800-53 Rev 5 Controls and SP 800-53A Rev 5 Assessment Procedures

## Schema Design

The schema (`src/nist_sp_800_53/schema/nist_sp_800_53.yaml`) is the single source of truth. All other artifacts — Python dataclasses, Pydantic models, JSON Schema, TypeScript, OWL, GraphQL, Protobuf, SHACL, SHEx, SQL DDL, and Java — are generated from it via `just gen-project`.

**Schema statistics (as of 2026-05-15, linkml 1.11.0):**

| Component | Count |
|-----------|-------|
| Classes   | 38    |
| Slots     | 68    |
| Enums     | 4     |
| Subsets   | 4     |

**Subsets** model the distinct document formats covered:

| Subset | Description |
|--------|-------------|
| `nist_sp_800_53r5_catalog` | SP 800-53 Rev 5 OSCAL catalog and resolved-profile catalogs |
| `nist_sp_800_53r5_profile` | SP 800-53 Rev 5 OSCAL baseline profiles (LOW / MODERATE / HIGH / PRIVACY) |
| `nist_sp_800_53r4_catalog` | SP 800-53 Rev 4 backward-compatibility (catalogs and profiles) |
| `nist_sp_800_53r5_cprt` | NIST Cybersecurity and Privacy Reference Tool (CPRT) JSON export format |

Key design choices:

- Classes that wrap complex, open-ended OSCAL structures use `class_uri: linkml:Any` to allow permissive nested validation while keeping the top-level schema strict.
- Hyphenated OSCAL slot names (e.g., `back-matter`, `how-many`) are preserved as slot names and handled via the open-world `class_uri: linkml:Any` pattern on their parent classes.
- `SP80053Document` is the sole `tree_root`, accepting a `catalog`, `profile`, or `response` (CPRT) key at the root — enabling a single schema to validate all three document families.

## Test Coverage

`linkml validate` is used to validate all official data files against the schema.

**Validated data (`tests/data/third-party/`):**

| Directory | Files | Description |
|-----------|-------|-------------|
| `nist/` | 18 YAML | Official NIST OSCAL documents: SP 800-53 Rev 5 catalog, LOW/MODERATE/HIGH/PRIVACY baseline profiles and resolved-profile catalogs; Rev 4 LOW/MODERATE/HIGH baseline profiles; OSCAL example catalog and profile files |
| `cprt/` | 3 JSON | NIST CPRT exports: SP 800-53 v5.2.0 (controls), SP 800-53A v5.2.0 (assessment procedures), SP 800-53B v5.2.0 (control baselines) |
| `hyperGRC/` | 11 YAML | hyperGRC agency app component OSCAL files (validated as `ControlGroup`) |

All files pass `linkml validate` with zero errors.

Pytest (`tests/test_data.py`) runs two parametrized test functions:

- `test_valid_data_files` — loads every `tests/data/valid/*.yaml` file into its target class (class name taken from the filename stem prefix) and asserts the object is non-null.
- `test_invalid_data_files` — loads every `tests/data/invalid/*.yaml` file and asserts that a `ValueError` or `TypeError` is raised (e.g. an out-of-range enum value).

**Unit test data (`tests/data/`):**

| Directory | Files | What is covered |
|-----------|-------|-----------------|
| `valid/` | 23 YAML | `Catalog`, `ProfileDocument`, `ControlGroup`, `Control`, `ControlEnhancement`, `CatalogElement`, `IdentifiedElement`, `Part`, `Property`, `Link`, `Guideline`, `Role` — minimal and feature-rich variants; catalog/profile with metadata, groups, params, selections, merge, modify |
| `invalid/` | 6 YAML | One fault per file: `_class` set to an out-of-range enum value on `Property` (`CatalogPropertyClassValue`), `ControlGroup`, `Control`, `ControlEnhancement`, `Part`, and `IdentifiedElement` (`CatalogElementClassValue`) |

New schema elements should be accompanied by example data in those directories before merging (see `CONTRIBUTING.md`).

## Upstream Limitations

### Hyphenated slot names silently convert to underscores in JSON Schema output

**Affects:** `linkml` ≥ 1.10.0 (confirmed still present in 1.11.0) | `gen-json-schema`, `linkml validate`

When a slot is named with a hyphen (e.g., `depends-on`, `back-matter`), `gen-json-schema` emits the property as an underscore name (`depends_on`, `back_matter`). `linkml validate` therefore rejects data files that use the hyphenated key — even though the slot is declared by that name — reporting *"Additional properties are not allowed ('depends-on' was unexpected)"*. The `alias` slot annotation does not fix this. `linkml` 1.11.0 added `--preserve-names` to `gen-json-schema` but testing confirms it does not affect slot property name serialisation — hyphens are still converted to underscores.

**Workaround used here:** Classes that own hyphenated OSCAL slots carry `class_uri: linkml:Any`, which sets `additionalProperties: true` in their JSON Schema `$defs` entry and lets the hyphenated key through as an unconstrained additional property.  The trade-off is that those classes lose closed-world property validation — any undeclared key is silently accepted.

See `ISSUE-sp80053.md` (project root) for a minimal reproducer and 1.11.0 status notes.

## OSCAL Schema Alignment

The schema is aligned to the [lmodel/oscal](https://w3id.org/lmodel/oscal) LinkML schema (`oscal-schema/` directory) via SSSOM mappings and inline `*_mappings` annotations.

**Should they be merged?** No. The OSCAL schema has 202 classes / 281 slots covering the full OSCAL suite (SSP, assessment plans, POA&M, component definitions, mapping). The NIST schema intentionally covers only the catalog + profile + CPRT subset (38 classes / 68 slots). Merging would force consumers to carry 164 unrelated classes.

**Alignment approach:**

- `oscal_catalog: https://w3id.org/lmodel/oscal_catalog/` and `oscal_profile: https://w3id.org/lmodel/oscal_profile/` are declared as schema prefixes.
- 33 classes carry `exact_mappings` (17) or `close_mappings` (16) to their OSCAL counterparts. Key renames: `CatalogBody` → `oscal_catalog:Catalog`, `ControlGroup` → `oscal_catalog:Group`, `ProfileBody` → `oscal_profile:Profile`, `ImportResource` → `oscal_profile:ProfileImport`, `MergeRules` → `oscal_profile:ProfileMerge`, `Selection` → `oscal_catalog:ParameterSelection`, `Guideline` → `oscal_catalog:ParameterGuideline`, `ProfileAlter` → `oscal_profile:Alteration`, `ProfileAdd` → `oscal_profile:Addition`, `ProfileSetParameter` → `oscal_profile:ParameterSetting`.
- `close_mappings` is used where the NIST class is a proper subset of the OSCAL class (e.g. `Metadata`, `Parameter`, `Part`, `Address`, `Party`).
- 67 of 68 slots carry `exact_mappings` to their identically-named OSCAL counterparts. Only `response` (CPRT-specific) has no OSCAL counterpart.

**SSSOM file:** `src/nist_sp_800_53/mappings/nist-sp-800-53-to-oscal-mappings.sssom.tsv` — 99 mapping rows (35 class + 67 slot - 3 unmapped CPRT classes).

**Tooling:** `scripts/overlay_sssom.py` reapplies the SSSOM file to the schema idempotently (run via `just overlay-sssom`; preview with `just overlay-sssom-dry-run`).

# References

- [NIST CSRC Controls](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/downloads)
- [NIST SP 800-53A Rev 5 final](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)
- [NIST SP 800-53B Rev 5 final](https://csrc.nist.gov/pubs/sp/800/53/b/1/final)
- [OSCAL Content (usnistgov)](https://github.com/usnistgov/oscal-content/tree/main/nist.gov/SP800-53)
- [NIST CPRT](https://csrc.nist.gov/projects/cprt)
