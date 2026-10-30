---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/glossary/control-enhancement
genre: reference
title: Control enhancement
description: "In SP 800-53, a control enhancement: added functionality or strength for a control, with an identifier such as AC-2(1), cited apart from its control. The schema renders one as `Sp80053ControlEnhancement`, with its identifier in `enhancement_id` and the control it requires in `required_controls`."
definition: Added functionality or strength for a control, with an identifier of its own such as AC-2(1), which the publication and other documents cite apart from the control.
resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: nist_sp_800_53.yaml
    resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
    title: the class Sp80053ControlEnhancement
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the controls of class SP800-53-enhancement and their required links
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Control enhancement

The schema's `Sp80053ControlEnhancement` carries what a control carries, its identifier in `enhancement_id`, and in `required_controls` the control, or in one case the enhancement, that must be implemented for it to apply: its own control for every enhancement but SC-42(2), which requires SC-42(1).[^nist_sp_800_53.yaml] In NIST's catalog an enhancement is a control of class `SP800-53-enhancement` nested in its control, with a `required` link.[^nist_sp-800-53_rev5_catalog.json]

[^nist_sp_800_53.yaml]: src/nist_sp_800_53/schema/nist_sp_800_53.yaml, the class Sp80053ControlEnhancement and its slots
[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the controls of class SP800-53-enhancement and their required links
