---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its sp-800-53-copies job runs `scripts/check_upstream_release.py` against NIST's editions and usnistgov/oscal-content, and on a finding opens or updates the issue titled Upstream watch: NIST's SP 800-53 has changed."
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the cron and the two steps
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` is the workflow named "Upstream watch". It runs every Monday at 07:00 UTC, after the knowledge workflows, and by hand, with `contents: read` and `issues: write`, and stops after 10 minutes. Its job `sp-800-53-copies` runs `scripts/check_upstream_release.py` with the runner's Python, which needs only the standard library, and writes the report to the runner's temporary folder. When the check fails, `.github/scripts/report-issue.sh` opens an issue titled "Upstream watch: NIST's SP 800-53 has changed" with the report, or comments on the open issue of that title, so a weekly finding is one issue. [Update the upstream pins](../playbooks/update-upstream-pins.md) says what to do with the finding.[^upstream-watch.yaml]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the cron and the two steps
