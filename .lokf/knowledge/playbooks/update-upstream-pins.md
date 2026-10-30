---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the weekly upstream watch reports that NIST registered the next final edition of SP 800-53, released a changed catalog or baseline in usnistgov/oscal-content, or that a copy drifted: replace the copies whole from one release, move the pins in `scripts/check_upstream_release.py` and the schema header, and run the tests."
resource: scripts/check_upstream_release.py
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the module docstring and the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the pin tests
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the schedule and the issue step
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Update the upstream pins

The watch opens an issue titled "Upstream watch: NIST's SP 800-53 has changed" when `scripts/check_upstream_release.py` exits 1, which it does when NIST has registered `10.6028/NIST.SP.800-53r6`, when usnistgov/oscal-content's latest release changes a copied file or holds a folder for another edition, or when a copy differs from its pinned blob.[^upstream-watch.yaml][^check_upstream_release.py]

1. Read the issue's report. A newer edition is a decision: read the publication and decide whether the schema moves to it. A changed catalog or baseline of the pinned edition is a replacement.
2. Replace every file in `src/nist_sp_800_53/schema/oscal-content/` from one release of usnistgov/oscal-content, byte for byte, with `curl -sfL` from `raw.githubusercontent.com/usnistgov/oscal-content/<tag>/...`, and never edit one.
3. Move `PINNED_TAG`, `PINNED_COMMIT` and each hash in `PINNED_BLOBS` in the script, and `oscal_content_tag`, `oscal_content_commit`, `version`, `publication_date` and `cprt_framework_version` in the schema header, together.[^check_upstream_release.py]
4. Run `just test`: `tests/test_upstream.py` checks the hashes, the header's pins and the counts, and a new release changes the counts it holds.[^test_upstream.py]
5. Run `python3 scripts/check_upstream_release.py` by hand; it should report every copy matching and the latest release the pinned one.

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the cron and the issue step
[^check_upstream_release.py]: scripts/check_upstream_release.py, the module docstring, PINNED_TAG, PINNED_COMMIT, PINNED_BLOBS and the DOIs
[^test_upstream.py]: tests/test_upstream.py, test_copy_matches_the_pinned_blobs, test_header_pins_match_the_watch and test_counts_match_the_release
