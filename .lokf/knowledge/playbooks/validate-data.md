---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the schema
description: "How to validate SP 800-53 data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No check covers the nesting of identifiers, a repeated one, or what a withdrawn element carries."
resource: docs/index.md
sources:
  - id: index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
---

# Validate data against the schema

Run `linkml-validate -s src/nist_sp_800_53/schema/nist_sp_800_53.yaml -C Sp80053Control control.yaml` to check a file against the JSON Schema generated from the schema. `tests/test_data.py` holds every example to the same check.

Validate before loading a file into either model in `src/nist_sp_800_53/datamodel/`, because the models check less:

- the dataclasses check required fields and enum values but no pattern;
- the Pydantic models check the patterns a field carries itself, such as `catalog_release` and `item_label`, but not those of the six identifier types.[^index.md]

No check covers the rules `docs/index.md` lists:

- identifiers nest, a `_prm_` parameter's under its control's identifier as the catalog writes it, unpadded, and never repeat;
- a cited identifier or placeholder names an element the catalog defines;
- a withdrawn element says where it went, and an active one carries its statement, discussion, objective and methods;
- a parameter is an assignment or a selection;
- a statement has text, items or both;
- a control's reference names a listed publication;
- an SP 800-53A label belongs to the element it labels.

`tests/test_upstream.py` checks all but the last over NIST's catalog and baselines.[^index.md]

[^index.md]: docs/index.md, the Validating data section
