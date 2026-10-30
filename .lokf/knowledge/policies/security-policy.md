---
type: Policy
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the four updates entries
generated:
  by: process:ktl-librarian
  at: "2026-10-30T09:09:14Z"
status: draft
---

# Security policy

`SECURITY.md` asks for a vulnerability to be reported through GitHub's private vulnerability reporting, never a public issue, with the file affected, how it is exploitable and whether it reaches the released schema or only the automation. One person maintains the repository and replies in days. Only the latest release receives fixes, as patches noted in the changelog. The repository releases a LinkML schema, its Python datamodel and the schema's `lokf adapt` copy, and publishes nothing to PyPI. `scripts/check_upstream_release.py` runs only in the upstream watch. It reads listings and the latest release of usnistgov/oscal-content and asks doi.org about NIST's editions, and writes nothing but its report.[^security.md]

Its table says what holds each surface:

- read-only test and lint jobs with `persist-credentials: false` and `uv sync --locked`;
- the release job behind the `release` Environment;
- the website's deploy job alone holding `pages: write`;
- the watch's one write scope, `issues: write`;
- the librarian's agent job with no write token, and a publish job that confines its patch to the bundle;
- the knowledge release's attach job.

A ruleset on `main` blocks deletion and force-pushes and keeps the history linear. Two settings are not yet in force: required reviewers on the `release` Environment, and secret scanning with push protection. A problem in the publications or NIST's copies belongs with NIST, and one in LinkML with LinkML.[^security.md] Dependabot keeps the pinned actions, the Python tree, the sidecar's tree, the website's npm packages and the release tools' npm lock current, monthly.[^dependabot.yml]

[^security.md]: SECURITY.md, Reporting a vulnerability, Supported versions, What this repository releases, What executes here and Not covered
[^dependabot.yml]: .github/dependabot.yml, the four updates entries
