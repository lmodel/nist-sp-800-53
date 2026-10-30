---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge Registrar (knowledge-registrar.yaml)
description: "The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Knowledge Registrar (knowledge-registrar.yaml)

`.github/workflows/knowledge-registrar.yaml` is a copy of the ktl-sidecar template at Knowledge Trust Ladder v0.59.0, the gate on this bundle. It runs on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand. Its jobs install the sidecar's toolkit from `.lokf/uv.lock`, run `just lokf-validate` and `just lokf-check-refs` against the domain schema the justfile names, run `.lokf/scripts/knowledge-conventions.sh`, and, in a job that runs no agent, read the pull request's reviews and commits to check that each new `human:` confirmation is backed by that person's approval or signed commit.[^knowledge-registrar.yaml]

[^knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml, the header comment, the on key and the jobs
