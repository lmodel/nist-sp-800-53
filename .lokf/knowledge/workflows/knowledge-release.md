---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge Release (knowledge-release.yaml)
description: "The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-nist-sp-800-53.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set."
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Knowledge Release (knowledge-release.yaml)

`.github/workflows/knowledge-release.yaml` is a copy of the ktl-sidecar template at Knowledge Trust Ladder v0.59.0. It runs when dispatched with a tag, as `semantic-release.yml` does after a release, and on a published release once the repository variable `KNOWLEDGE_RELEASE_ENABLED` is `true`. It packs `.lokf/knowledge` as `knowledge-<tag>-nist-sp-800-53.zip`, builds one Copilot skill zip per instructions file under `.lokf/m365/`, and copies the domain schema the justfile names as `schema-<tag>-nist-sp-800-53.yaml`. Each asset gets a `.sha256` and a build-provenance attestation. Its `attach` job, the only job that can write, attaches them to the release. It skips a release whose bundle and schema match the last one released unless `force` is set.[^knowledge-release.yaml]

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the header comment, the on key and the jobs
