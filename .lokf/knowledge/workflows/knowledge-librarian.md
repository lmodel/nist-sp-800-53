---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge Librarian (knowledge-librarian.yaml)
description: "The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent."
resource: .github/workflows/knowledge-librarian.yaml
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the header comment, the pin lines and the two jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Knowledge Librarian (knowledge-librarian.yaml)

`.github/workflows/knowledge-librarian.yaml` is a copy of the ktl-sidecar template at Knowledge Trust Ladder v0.59.0, with the pin written into it: `TRUST_LADDER_SKILLS_REF` is `v0.59.0` and `TRUST_LADDER_SKILLS_SHA` is `2b9d7e05f0bc020127b3cbd2ee54dc27774b8286`, the commit that tag names. It runs every Monday at 05:00 UTC and by hand, and does nothing until the repository variable `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`. Its `refresh` job clones the skills repository at the pin, checks the commit, and runs `.lokf/scripts/knowledge-librarian.sh`, which runs an agent with the ktl-librarian skill in a job with no write credential and hands on a patch; its `publish` job runs no agent, applies the patch on a clean checkout, confines it to the bundle, refuses a person's record, and opens the pull request a person merges.[^knowledge-librarian.yaml]

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the header comment, the pin lines and the two jobs
