---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/glossary/assessment-objective
genre: reference
title: Assessment objective
description: "In SP 800-53A, an assessment objective: a determination statement an assessor checks, nested as the control statement's items are, with a label such as AC-02a.[01]. The schema renders one as `Sp80053AssessmentObjective`, with its label in `objective_label`."
definition: A determination statement an assessor checks for a control or enhancement, or a heading that groups the determination statements of one item of the control statement, as SP 800-53A gives them.
resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53a
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: nist_sp_800_53.yaml
    resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
    title: the class Sp80053AssessmentObjective
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the parts named assessment-objective
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:05:26Z"
---

# Assessment objective

The schema's `Sp80053AssessmentObjective` carries the SP 800-53A label in `objective_label`, the determination statement in `objective_text` and the objectives grouped under it in `sub_objectives`. A heading has no determination statement.[^nist_sp_800_53.yaml] In NIST's catalog each active control and enhancement has one `assessment-objective` part whose nested objectives follow the statement's items.[^nist_sp-800-53_rev5_catalog.json]

[^nist_sp_800_53.yaml]: src/nist_sp_800_53/schema/nist_sp_800_53.yaml, the class Sp80053AssessmentObjective and its slots
[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the parts named assessment-objective
