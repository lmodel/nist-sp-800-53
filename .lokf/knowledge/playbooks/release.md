---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/playbooks/release
genre: how-to
title: Cut a release
description: "How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-nist-sp-800-53.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true."
resource: .releaserc.json
sources:
  - id: releaserc.json
    resource: .releaserc.json
    title: the release rules and plugins
  - id: changelog-release.mjs
    resource: .github/scripts/changelog-release.mjs
    title: the check, notes and promote commands
  - id: changelog.md
    resource: CHANGELOG.md
    title: the baseline paragraph
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Releasing section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:34:38Z"
---

# Cut a release

1. Write the change under `## [Unreleased]` in `CHANGELOG.md` as you go. The release job runs `changelog-release.mjs check` and refuses an empty section.[^changelog-release.mjs]
2. Type the commit for what the change is. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release. `.releaserc.json` maps `security` to a patch and a breaking change to a minor bump, so the schema stays below 1.0.0.[^releaserc.json] A pull request that would release must carry a releasing type in its title too, since a squash merge takes its subject from it.[^contributing.md]
3. Before the first releasing merge, push the `v0.0.0` baseline tag on `main`. Both release jobs refuse to run without a `v*` tag, and the first release is then 0.1.0.[^changelog.md]
4. On merge, `semantic-release.yml` promotes the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub release. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches Knowledge Release, which attaches `schema-<tag>-nist-sp-800-53.yaml`, its checksum and the bundle.[^contributing.md]
5. Configure required reviewers on the `release` Environment, or every qualifying merge releases unattended.

[^changelog-release.mjs]: .github/scripts/changelog-release.mjs, the header comment and the check command
[^releaserc.json]: .releaserc.json, releaseRules and the plugins
[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
[^changelog.md]: CHANGELOG.md, the baseline paragraph
