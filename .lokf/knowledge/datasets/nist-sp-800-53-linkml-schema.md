---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
genre: reference
title: nist-sp-800-53 LinkML schema
description: "The LinkML schema of the SP 800-53 controls at Release 5.2.0, `src/nist_sp_800_53/schema/nist_sp_800_53.yaml` (schema id `https://w3id.org/lmodel/nist-sp-800-53`, version 5.2.0): eleven classes, five enums and six identifier types. Its `lokf adapt` copy `.lokf/nist-sp-800-53.yaml`, rooted on the family, the control, the control enhancement and the baseline, is the bundle's domain schema."
resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
version: 5.2.0
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53a
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53b
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/sp-800-53-catalog-copy
sources:
  - id: nist_sp_800_53.yaml
    resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
    title: the header, the classes, the enums and the types
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: nist-sp-800-53.yaml
    resource: .lokf/nist-sp-800-53.yaml
    title: the notes lokf adapt wrote
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:54:10Z"
---

# nist-sp-800-53 LinkML schema

`src/nist_sp_800_53/schema/nist_sp_800_53.yaml` has the id `https://w3id.org/lmodel/nist-sp-800-53`, the name `nist_sp_800_53` and the version `5.2.0`, the release of Revision 5 that NIST's catalog carries. Its `source` is the publication's digital object identifier, `https://doi.org/10.6028/NIST.SP.800-53r5`, and its licence is Apache-2.0. Its annotations name the release as NIST's reference tool does, `SP_800_53_5_2_0`, with the usnistgov/oscal-content tag `v1.6.0` and commit the copies were taken from.[^nist_sp_800_53.yaml]

## Elements

The schema has eleven classes, each with the `Sp80053` prefix: `Sp80053Catalog`, the tree root, `Sp80053Family`, `Sp80053Control`, `Sp80053ControlEnhancement`, `Sp80053Statement`, `Sp80053StatementItem`, `Sp80053Parameter`, `Sp80053AssessmentObjective`, `Sp80053AssessmentMethod`, `Sp80053Reference` and `Sp80053Baseline`. Five enums hold the withdrawn status, the implementation levels, the selection cardinalities, the three assessment methods and the four baseline levels, with upper-case values. Six types pattern the identifiers: a family's two letters, a control's `AC-2`, an enhancement's `AC-2(1)`, either of the two, a withdrawal target such as `AC-2k` or `SR`, and a parameter's `ac-02_odp.01`. The two slots `title` and `description` carry `schema:name` and `schema:description`, so `lokf adapt` folds them into LOKF's. Every other key is the schema's own, such as `control_identifier`, `control_discussion` and `assessment_objective`. The family, the control, the enhancement and the baseline require a `title`. Each class names its lmodel/oscal counterpart in `broad_mappings`, the parameter `oscal:Parameter`.[^nist_sp_800_53.yaml]

The README lists what the schema models and the counts the tests hold: twenty families, 324 controls, 872 enhancements, 1,600 parameters, 3,720 assessment objectives, 2,931 assessment methods, 192 references, 160 of them cited by a control, and the four baselines.[^readme.md]

## The domain schema

`just lokf-adapt`, in `project.justfile`, writes `.lokf/nist-sp-800-53.yaml` from the schema with `--root Sp80053Family --root Sp80053Control --root Sp80053ControlEnhancement --root Sp80053Baseline`. Those four classes become types a knowledge concept may name. `just lokf-adapt-check` fails when the copy is stale.[^project.justfile] The copy's header says it was generated from `nist_sp_800_53.yaml` at version 5.2.0 and imports `lokf`. It says that `title` and `description` folded into LOKF's slots and that nothing was renamed.[^nist-sp-800-53.yaml] The sidecar's justfile names the copy on its `schema :=` line and its pyproject in the `[tool.lokf]` table, so every `lokf` command validates this bundle against it.

[^nist_sp_800_53.yaml]: src/nist_sp_800_53/schema/nist_sp_800_53.yaml, the header, the classes, the enums and the types
[^readme.md]: README.md, the What it models section
[^project.justfile]: project.justfile, lokf_adapt_roots and the two recipes
[^nist-sp-800-53.yaml]: .lokf/nist-sp-800-53.yaml, the comment lines at the top
