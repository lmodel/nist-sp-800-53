---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/glossary/organization-defined-parameter
genre: reference
title: Organization-defined parameter
description: "In SP 800-53, an organization-defined parameter (ODP): a value the statement leaves to the organization, an assignment or a selection, which SP 800-53A labels such as AC-02_ODP[01]. The schema renders one as `Sp80053Parameter`, with the catalog's identifier in `parameter_id`."
definition: "A value a control statement leaves to the organization: an assignment it fills in, or a selection from the choices the publication lists; SP 800-53A gives each a label and a guideline."
resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53a
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: nist_sp_800_53.yaml
    resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
    title: the class Sp80053Parameter
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the params of the controls and the placeholders in their statements
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:05:26Z"
---

# Organization-defined parameter

The schema's `Sp80053Parameter` carries:

- the catalog's identifier in `parameter_id`, such as `ac-02_odp.01`;
- the SP 800-53A label in `assessment_label`;
- an assignment's `parameter_label` and `parameter_guidelines`;
- a selection's `selection_choices` and `selection_cardinality`;
- for a parameter that stands for several, `aggregated_parameters`.[^nist_sp_800_53.yaml]

In NIST's catalog a parameter is a `params` entry with a `label` or a `select`, `guidelines` and props, and a statement names it in a placeholder of the form `{{ insert: param, <identifier> }}`.[^nist_sp-800-53_rev5_catalog.json]

[^nist_sp_800_53.yaml]: src/nist_sp_800_53/schema/nist_sp_800_53.yaml, the class Sp80053Parameter and its slots
[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the params of the controls and the placeholders in their statements
