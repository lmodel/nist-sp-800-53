---
type: Explanation
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: "How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies: classes with the `Sp80053` prefix, generic nouns qualified with the publication's own, NIST's identifiers kept as printed, upper-case enum values, `title` and `description` carrying LOKF's IRIs, and no other key shared, which `tests/test_schema_rules.py` checks."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: the naming paragraphs
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: SHARED_WITH_NEIGHBOURS and the name tests
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the standard_naming setting and its comment
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:34:38Z"
---

# Element names and the shared namespace

Element names are the schema's own. Classes carry the `Sp80053` prefix, such as `Sp80053Control`, so that they can be imported beside other vocabularies. Slots are snake_case, and a generic noun is qualified with the publication's own, as in `control_discussion` and `assessment_objective`. The identifiers keep the form NIST prints, such as `AC-2` and `AC-2(1)`; a parameter keeps the catalog's identifier, such as `ac-02_odp.01`, and the label SP 800-53A gives it. Every element is in the `nist_sp_800_53:` namespace, `https://w3id.org/lmodel/nist-sp-800-53/`.[^about.md]

The enums' values are upper case, as the catalog writes the assessment methods `EXAMINE`, `INTERVIEW` and `TEST`, so `.linkmllint.yaml` asks the `standard_naming` rule for permissible values in upper case and keeps the rule at error level.[^linkmllint.yaml]

## Beside other schemas

A host imports the adapt copy beside LOKF's `lokf.yaml` and other adapt copies, and LinkML merges them into one namespace, where the last definition of a name wins silently. The README says that no class, enum or type therefore shares a name with LOKF's or with the copies of slsa, github-actions, oscal, spdx and nist-sp-800-218. A slot shares a name only where it carries LOKF's meaning and IRI, as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing.[^readme.md] The control's identifier slot is `control_identifier` because `control_id` is a key of oscal's copy.

`tests/test_schema_rules.py` checks the copy against `lokf.yaml` and the schema assets of slsa v0.7.0, github-actions v0.2.1, oscal v0.1.0, spdx v0.1.0 and nist-sp-800-218 v0.1.0. Its list of keys shared with each neighbour is empty, so a new shared key fails the test.[^test_schema_rules.py]

[^about.md]: docs/about.md, the paragraph on element names
[^linkmllint.yaml]: .linkmllint.yaml, the comment and the standard_naming rule
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
