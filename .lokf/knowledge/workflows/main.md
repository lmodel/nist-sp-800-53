---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/nist-sp-800-53.yaml` is current."
resource: .github/workflows/main.yaml
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
---

# Build and test (main.yaml)

`.github/workflows/main.yaml` is the workflow named "Build and test". It runs on a push to `main` and on every pull request, with `contents: read`, and cancels a superseded run of the same ref. Its one job, `test`, which stops after 30 minutes, runs on Python 3.10, 3.11, 3.12, 3.13 and 3.14 after harden-runner in audit mode. It installs just 1.47.0, the version the sidecar pins, and the project with `uv sync --locked --group dev`, and runs `just test`. On Python 3.13 it also runs `just lint`, and it syncs the sidecar's environment and runs `just lokf-adapt-check`, because the copy is what the bundle validates against and the release attaches.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml, the header comment, the on key and the jobs
