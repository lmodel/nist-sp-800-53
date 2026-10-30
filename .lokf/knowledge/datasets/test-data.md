---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: sixteen valid examples and forty-one counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which derives Release 5.2.0 from NIST's catalog and baselines and holds the examples to it, `tests/test_watch.py`, which runs the upstream watch against a stubbed network, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies in `tests/neighbours/`."
resource: tests
sources:
  - id: test_data.py
    resource: tests/test_data.py
    title: the four tests
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the Derivation class, COUNTS and the rule tests
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS, SHARED_WITH_NEIGHBOURS and ROOTS
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the stub and the six tests
  - resource: tests/data
    title: the valid and invalid examples
  - resource: tests/neighbours
    title: the five released copies
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:54:10Z"
---

# Test data and tests

`tests/data/valid/` holds sixteen examples, at least one per class, written in the project's own words with the publication's real identifiers. `tests/data/invalid/` holds forty-one counter-examples, one per constraint the schema states. Each opens with a `# Fails at:` line that names where the validator must report it, and a comment saying why. `tests/test_data.py` loads each valid example into the generated dataclass and holds each example to the validator, which must pass a valid one and fail a counter-example at the place its first line names. It also checks that every class has an example.[^test_data.py]

`tests/test_upstream.py` checks that the copies in `src/nist_sp_800_53/schema/oscal-content/` carry the pinned git object hashes, that the header's pins match the watch's, and that the catalog and the profiles carry the version the header names. It derives an `Sp80053Catalog` from them, validates it, and holds it to the release's counts:

- 20 families;
- 324 controls, of which 24 are withdrawn, and 872 enhancements, of which 158 are withdrawn;
- 166 incorporated-into and 34 moved-to targets;
- 1,600 parameters, 3,720 assessment objectives and 2,931 methods;
- 838 control references to 160 of the 192 listed documents;
- baselines of 149, 287, 370 and 96 selections.

It also checks the rules no pattern can express:

- identifiers nest and never repeat;
- a parameter's identifier starts with its element's;
- every cited identifier names an element;
- a withdrawn element says where it went and holds nothing else in the catalog;
- a statement has text or items;
- a parameter is an assignment or a selection;
- every reference a control cites is listed.

A valid example that names an element of the catalog must give its title, its withdrawn status and where it went as the catalog does.[^test_upstream.py]

`tests/test_schema_rules.py` checks that:

- `tests/neighbours/` holds exactly the released adapt copies of slsa v0.7.0, github-actions v0.2.1, oscal v0.1.0, spdx v0.1.0 and nist-sp-800-218 v0.1.0, each pinned by sha256;
- no class, enum, type or subset name of the copy is LOKF's or a neighbour's;
- the copy shares no key with a neighbour;
- it re-roots exactly the four concept classes on `Concept`;
- every mapping is a CURIE whose prefix the copy binds;
- every `oscal:` mapping names a class of oscal's copy.[^test_schema_rules.py]

`tests/test_watch.py` runs `scripts/check_upstream_release.py` against a stubbed GitHub API and doi.org, and checks that it reports a newer release without the pinned folder, a changed file, a network failure, a file NIST adds and a tag that names another commit.[^test_watch.py]

[^test_data.py]: tests/test_data.py, test_valid_data_files, test_valid_data_files_validate, test_invalid_data_files_fail and test_every_concept_class_has_an_example
[^test_upstream.py]: tests/test_upstream.py, COUNTS, METHODS, BASELINE_SIZES and the tests
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS, SHARED_WITH_NEIGHBOURS, ROOTS and the tests
[^test_watch.py]: tests/test_watch.py, the stub and the tests
