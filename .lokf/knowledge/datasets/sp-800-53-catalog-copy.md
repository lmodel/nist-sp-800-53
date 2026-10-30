---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/sp-800-53-catalog-copy
genre: reference
title: NIST's SP 800-53 catalog and baseline copies
description: NIST's catalog of SP 800-53 Release 5.2.0 in the Open Security Controls Assessment Language (OSCAL), with the SP 800-53A procedures inside it, and the four SP 800-53B baseline profiles, copied with NIST's licence from usnistgov/oscal-content v1.6.0 into `src/nist_sp_800_53/schema/oscal-content/` and matched to that release by git object hash. The tests derive the whole release from them.
resource: src/nist_sp_800_53/schema/oscal-content
license: CC0-1.0
derivedFrom:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53a
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53b
sources:
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the metadata, the groups, the controls and the back matter
  - id: nist_sp-800-53_rev5_low-baseline_profile.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_LOW-baseline_profile.json
    title: the metadata and the import's with-ids
  - id: notice
    resource: NOTICE
    title: the NIST sections
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the derivation and the counts
  - id: oscal-content-license.md
    resource: src/nist_sp_800_53/schema/oscal-content/LICENSE.md
    title: NIST's licence
  - resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_MODERATE-baseline_profile.json
    title: the import's with-ids
  - resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_HIGH-baseline_profile.json
    title: the import's with-ids
  - resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_PRIVACY-baseline_profile.json
    title: the import's with-ids
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
---

# NIST's SP 800-53 catalog and baseline copies

`src/nist_sp_800_53/schema/oscal-content/` holds six files: `NIST_SP-800-53_rev5_catalog.json`, NIST's catalog of SP 800-53 Release 5.2.0 in the Open Security Controls Assessment Language (OSCAL); the four baseline profiles `NIST_SP-800-53_rev5_LOW-baseline_profile.json`, `..._MODERATE-...`, `..._HIGH-...` and `..._PRIVACY-...`; and NIST's `LICENSE.md`. NOTICE says that all were retrieved from usnistgov/oscal-content at commit `f0de6d8d8c059d374f15e0ae07508d82e370fc1d`, the v1.6.0 release, and are identical to their counterparts there.[^notice] It also says that NIST's work is in the public domain within the United States, and that NIST dedicates it to the worldwide public domain under CC0 1.0, as the licence file states.[^oscal-content-license.md]

## What the catalog holds

The catalog's metadata gives its version as `5.2.0`, its OSCAL version as `1.2.3` and its last modification as `2026-10-22`.[^nist_sp-800-53_rev5_catalog.json] Its 20 groups of class `family` are the control families. Each group's controls of class `SP800-53` are the controls, 324 of them, and each control's nested controls of class `SP800-53-enhancement` are the enhancements, 872. 24 controls and 158 enhancements carry the property `status: withdrawn`, with a link `incorporated-into` or `moved-to` saying where each went. SC-19 and CP-10(3) have no such link: their statement gives the reason instead. An active control's parts are its `statement` with nested `item` parts, its `guidance`, its `assessment-objective` with nested objectives, and its `assessment-method` parts, each with a `method` property and an `assessment-objects` part. Its `params` are the organization-defined parameters, and its links are `related`, `reference` and, on an enhancement, `required`. The back matter lists 202 resources, of which 192 carry a citation.

Each baseline profile imports the catalog and selects controls and enhancements under `include-controls` as a list of `with-ids`: LOW selects 149, MODERATE selects 287, HIGH selects 370, PRIVACY selects 96.[^nist_sp-800-53_rev5_low-baseline_profile.json]

`tests/test_upstream.py` derives an `Sp80053Catalog` from the six files with the standard library's JSON parser, validates it, and holds it to the release's counts, with the withdrawn controls and enhancements counted apart.[^test_upstream.py]

## The pins

`scripts/check_upstream_release.py` pins the tag `v1.6.0`, the commit, and each file's git object hash:

- `55eb9f2506cab43e051eeac6b48496246afcfd2c` for the catalog;
- `84edda2906a0edcb5e180034119e0501fc57691e`, `f0d1a6ecffa9b033480563a1f46bbac3f4ec7c41`, `9e275cbcc1e97e0ad52cb3dbd3cf668d653b409f` and `63c6ee354dbb2ddf17da03a3d186de26b9fabc2a` for the Low, Moderate, High and Privacy profiles;
- `109af23dd24c2c465143aeab12ffebfffe2a4cd5` for the licence.[^check_upstream_release.py]

The test checks the hashes offline. The upstream watch checks them against the pinned commit every week, and checks that the tag still names that commit. [Update the upstream pins](../playbooks/update-upstream-pins.md) says how to replace the copies.

[^notice]: NOTICE, the section NIST's SP 800-53 catalog and baselines in OSCAL
[^oscal-content-license.md]: src/nist_sp_800_53/schema/oscal-content/LICENSE.md, the public domain and CC0 statements
[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the metadata, the groups and the back matter
[^nist_sp-800-53_rev5_low-baseline_profile.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_LOW-baseline_profile.json, imports, include-controls and with-ids
[^test_upstream.py]: tests/test_upstream.py, the COUNTS table and the Derivation class
[^check_upstream_release.py]: scripts/check_upstream_release.py, PINNED_TAG, PINNED_COMMIT and PINNED_BLOBS
