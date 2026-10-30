---
type: Policy
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "The repository's licences: Apache 2.0 for the schema and the code, NIST's public-domain and CC0 terms for the catalog and baseline copies, NIST's statement that SP 800-53, SP 800-53A and SP 800-53B are not subject to copyright in the United States, MIT for the copier template's scaffolding, and Apache 2.0 for the KTL sidecar and website templates."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: license
    resource: LICENSE
    title: the Apache License, Version 2.0
  - id: website-notice
    resource: website/NOTICE
    title: the adapted graph explorer
  - id: readme.md
    resource: README.md
    title: the License section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:34:38Z"
---

# License and attribution

The schema and the code are licensed under the Apache License, Version 2.0, the text of `LICENSE`.[^license] NOTICE says that the schema, the datamodel and `project/` are this project's rendering of SP 800-53, SP 800-53A and SP 800-53B, written in its own words with NIST as the source, not NIST's and implying no endorsement; that the three publications are works of the United States Government not subject to copyright in the United States, which NIST's statement says may be subject to copyright in other countries; that the copies under `src/nist_sp_800_53/schema/oscal-content/` come from usnistgov/oscal-content v1.6.0 with NIST's licence beside them, in the public domain within the United States and dedicated worldwide under CC0 1.0; that the justfile and scaffolding derive from linkml-project-copier under the MIT licence; and that the sidecar's scripts, the knowledge workflows and the website derive from Knowledge Trust Ladder's templates under Apache 2.0.[^notice] `website/NOTICE` adds that the graph explorer is adapted from the LOKF toolkit's site, also under Apache 2.0.[^website-notice] The README repeats the licence and the disclaimer.[^readme.md]

[^license]: LICENSE, the whole file
[^notice]: NOTICE, the header, the NIST sections, linkml-project-copier and Knowledge bundle
[^website-notice]: website/NOTICE, the whole file
[^readme.md]: README.md, the License section
