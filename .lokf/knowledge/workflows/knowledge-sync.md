---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: "The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve."
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

`.github/workflows/knowledge-sync.yaml` is a copy of the ktl-sidecar template at Knowledge Trust Ladder v0.59.0. It runs every Monday at 04:10 UTC and by hand. It runs `.lokf/scripts/knowledge-sync.sh` against the newest release of the skills repository. The script reads that release's `knowledge-sync.manifest`, copies every template this host carries, moves `TRUST_LADDER_SKILLS_REF` and `TRUST_LADDER_SKILLS_SHA` in `knowledge-librarian.yaml`, and writes the changelog entry under `## [Unreleased]` and `### Security`. The workflow opens one pull request from `.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md` with the `KNOWLEDGE_SYNC_TOKEN` secret of the `knowledge-sync` Environment, refreshed until merged, and holds any workflow change other than the pin for a person to apply.[^knowledge-sync.yaml]

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment, the on key and the jobs
