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
  - id: release-tools
    resource: .github/release
    title: the release tools' package.json and package-lock.json
generated:
  by: process:ktl-librarian
  at: "2026-10-30T09:09:14Z"
status: draft
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` is the workflow named "Semantic release". Its `plan` job runs on a pull request into `main`, including a retitling, and stops after 10 minutes. It:

- installs semantic-release and its plugins from `.github/release/package-lock.json` with `npm ci --ignore-scripts`, as the `release` job does;[^release-tools]
- reads whether the commits would release;
- refuses to release before a `v*` tag exists;
- refuses an empty `## [Unreleased]` section when they would release;
- refuses a title without a releasing type, and names rebase and merge as the other way to keep the release;
- previews the release with `--dry-run`.

Its `release` job runs on a push to `main`, in the `release` Environment with `contents: write` and `actions: write`, and stops after 20 minutes. It repeats the baseline check and runs semantic-release, which promotes the changelog through `changelog-release.mjs`, tags and publishes. It then dispatches `knowledge-release.yaml` for the tag once `KNOWLEDGE_RELEASE_ENABLED` is `true`. [Cut a release](../playbooks/release.md) says how to prepare a change for it.[^semantic-release.yml]

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and the two jobs
[^release-tools]: .github/release, package.json and package-lock.json
