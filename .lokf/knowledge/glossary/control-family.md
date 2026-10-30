---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/glossary/control-family
genre: reference
title: Control family
description: In SP 800-53, one of the twenty families the controls are sorted into, such as Access Control (AC) or Supply Chain Risk Management (SR). The schema renders a family as `Sp80053Family`, with its two letters in `family_id`.
definition: One of the twenty groups SP 800-53 sorts its controls into, named by two letters such as AC.
resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: nist_sp_800_53.yaml
    resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
    title: the class Sp80053Family
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the groups of class family
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Control family

The schema's `Sp80053Family` describes one of the twenty families SP 800-53 sorts its controls into, with the family's two letters in `family_id`, its name in `title`, an optional `description` and its controls in `family_controls`.[^nist_sp_800_53.yaml] In NIST's catalog each family is a group of class `family`, labelled with its letters, and only the Program Management group carries an overview part.[^nist_sp-800-53_rev5_catalog.json] The [families](../families/index.md) concepts hold each one.

[^nist_sp_800_53.yaml]: src/nist_sp_800_53/schema/nist_sp_800_53.yaml, the class Sp80053Family and its slots
[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the groups of class family
