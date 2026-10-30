---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release."
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment, the on key and the two jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` is the workflow named "Semantic release". On a pull request into `main`, including a retitling, its `plan` job, stopped after 10 minutes, installs pinned semantic-release packages with `--ignore-scripts`, reads whether the commits would release, refuses to release before a `v*` tag exists, refuses an empty `## [Unreleased]` section when they would, refuses a title without a releasing type and names rebase and merge as the other way to keep the release, and previews the release with `--dry-run`. On a push to `main`, its `release` job, stopped after 20 minutes, runs in the `release` Environment with `contents: write` and `actions: write`, repeats the baseline check, runs semantic-release, which promotes the changelog through `changelog-release.mjs`, tags and publishes, and then dispatches `knowledge-release.yaml` for the tag once `KNOWLEDGE_RELEASE_ENABLED` is `true`. [Cut a release](../playbooks/release.md) says how to prepare a change for it.[^semantic-release.yml]

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and the two jobs
