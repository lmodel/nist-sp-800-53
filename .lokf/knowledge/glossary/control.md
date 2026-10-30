---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/glossary/control
genre: reference
title: Control
description: "In SP 800-53, a security or privacy control: a safeguard with an identifier such as AC-2, a statement, a discussion, parameters, related controls, references and enhancements. The schema renders a control as `Sp80053Control`, with its identifier in `control_identifier`; a withdrawn one keeps its identifier and says where it went."
definition: A security or privacy safeguard with an identifier such as AC-2, a statement of what it requires, a discussion, organization-defined parameters, related controls, references, and the assessment objective and methods SP 800-53A gives it.
resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: nist_sp_800_53.yaml
    resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
    title: the class Sp80053Control
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the controls of class SP800-53
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Control

The schema's `Sp80053Control` carries the control's identifier in `control_identifier`, its `title`, its `control_statement`, `control_discussion`, `control_parameters`, `related_control_ids` and `control_references`, the `assessment_objective` and `assessment_methods` of SP 800-53A, the `implementation_level` and `contributes_to_assurance` facts of NIST's reference data, and its `control_enhancements`. A control Revision 5 withdrew carries `control_status: WITHDRAWN` and `incorporated_into`, `moved_to` or `withdrawal_reason`.[^nist_sp_800_53.yaml] In NIST's catalog a control is a control of class `SP800-53` with a plain label such as `AC-2`, a zero-padded one such as `AC-02` and a sort id.[^nist_sp-800-53_rev5_catalog.json]

[^nist_sp_800_53.yaml]: src/nist_sp_800_53/schema/nist_sp_800_53.yaml, the class Sp80053Control and its slots
[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the controls of class SP800-53
