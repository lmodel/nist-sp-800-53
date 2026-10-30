---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/glossary/assessment-method
genre: reference
title: Assessment method
description: "In SP 800-53A, an assessment method: examine, interview or test, applied to the documents, people or mechanisms an assessor selects from. The schema renders one as `Sp80053AssessmentMethod`, with the method in `assessment_method` and its objects in `assessment_objects`."
definition: One of the three ways SP 800-53A assesses a control, examine, interview or test, with the objects an assessor selects from.
resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53a
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: nist_sp_800_53.yaml
    resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
    title: the class Sp80053AssessmentMethod
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the parts named assessment-method
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Assessment method

The schema's `Sp80053AssessmentMethod` carries one of `EXAMINE`, `INTERVIEW` and `TEST` in `assessment_method` and the objects it is applied to in `assessment_objects`.[^nist_sp_800_53.yaml] In NIST's catalog each active control and enhancement has up to three `assessment-method` parts, each with a `method` property and an `assessment-objects` part that lists the objects.[^nist_sp-800-53_rev5_catalog.json]

[^nist_sp_800_53.yaml]: src/nist_sp_800_53/schema/nist_sp_800_53.yaml, the class Sp80053AssessmentMethod and its slots
[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the parts named assessment-method
