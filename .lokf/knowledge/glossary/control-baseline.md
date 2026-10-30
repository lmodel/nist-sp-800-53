---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/glossary/control-baseline
genre: reference
title: Control baseline
description: "In SP 800-53B, a control baseline: the controls and enhancements selected for a low, moderate or high impact system, or for privacy. The schema renders one as `Sp80053Baseline`, with its level in `baseline_level` and its selections in `baseline_controls`."
definition: One of the four sets of controls and enhancements SP 800-53B selects for systems at the low, moderate or high impact level, or for privacy.
resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53b
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: nist_sp_800_53.yaml
    resource: src/nist_sp_800_53/schema/nist_sp_800_53.yaml
    title: the class Sp80053Baseline
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the absence of baselines in the catalog, which the profiles carry
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Control baseline

The schema's `Sp80053Baseline` carries the level in `baseline_level`, one of `LOW`, `MODERATE`, `HIGH` and `PRIVACY`, and the selected identifiers in `baseline_controls`.[^nist_sp_800_53.yaml] NIST publishes each baseline as an OSCAL profile that imports the catalog and lists its selections under `include-controls` as `with-ids`; the catalog itself carries no baseline.[^nist_sp-800-53_rev5_catalog.json] The [baselines](../baselines/index.md) concepts hold each selection.

[^nist_sp_800_53.yaml]: src/nist_sp_800_53/schema/nist_sp_800_53.yaml, the class Sp80053Baseline and its slots
[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the absence of baselines in the catalog, which the profiles carry
