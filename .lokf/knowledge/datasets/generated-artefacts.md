---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and Java), the Python dataclasses and Pydantic models in `src/nist_sp_800_53/datamodel/`, `docs/schema/` and `docs/elements/`, and `.lokf/nist-sp-800-53.yaml`. None is edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project, gen-doc and test recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the excludes and generator_args
  - id: pre-commit-config.yaml
    resource: .pre-commit-config.yaml
    title: the exclude block
  - resource: project
    title: the generated folders
  - resource: src/nist_sp_800_53/datamodel
    title: the two Python models
  - resource: docs/schema
    title: the merged schema
  - resource: docs/elements
    title: the element pages gen-doc writes
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
---

# Generated artefacts

`just gen-project` runs `gen-project` with `.linkml/generators.yaml` into `project/`, moves the Python dataclasses to `src/nist_sp_800_53/datamodel/`, writes the Pydantic models beside them with `gen-pydantic`, and runs `gen-java`, `gen-typescript` and `gen-owl` separately. `just gen-doc` writes the merged schema to `docs/schema/nist_sp_800_53.yaml` and the element pages to `docs/elements/`, which git ignores. `just test` regenerates into `tmp/`, runs pytest and runs the examples.[^justfile] `.linkml/generators.yaml` excludes only the markdown generator from `gen-project` and merges imports in every other.[^generators.yaml]

`project/` holds one folder per generator: `excel`, `graphql`, `java`, `jsonld`, `jsonschema`, `owl`, `prefixmap`, `protobuf`, `shacl`, `shex`, `sqlschema` and `typescript`. The pre-commit hooks skip `project/`, the datamodel, `docs/schema/`, the adapt copy and NIST's copies, so no hook rewrites a generated or copied file.[^pre-commit-config.yaml]

[nist-sp-800-53 LinkML schema](nist-sp-800-53-linkml-schema.md) says how `.lokf/nist-sp-800-53.yaml` is written. [Regenerate and test after a schema change](../playbooks/regenerate-and-test.md) says when to run each recipe.

[^justfile]: justfile, gen-project, gen-python, gen-doc, _gen-yaml and test
[^generators.yaml]: .linkml/generators.yaml, excludes and generator_args
[^pre-commit-config.yaml]: .pre-commit-config.yaml, the exclude block
