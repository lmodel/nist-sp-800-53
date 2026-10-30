#!/usr/bin/env python3
"""Check NIST's SP 800-53 copies against NIST's releases and publications.

Three things can go wrong with ``src/nist_sp_800_53/schema/oscal-content/``
without any change in this repository:

- NIST publishes a newer edition of SP 800-53, so the schema falls behind;
- NIST releases a changed catalog or baseline of the pinned edition in
  usnistgov/oscal-content, as it did for Release 5.2.0;
- the copied files drift from the files they were taken from.

The copies have no release in their paths, so the release, the commit its
tag names and each file's git object hash are pinned below. This script asks
the GitHub API for usnistgov/oscal-content's latest release and for a few
folder listings, and compares every copied file with its blob by git object
hash, so nothing is downloaded but listings. It asks doi.org whether NIST
has registered the identifier of the next final edition, because NIST
registers one for every publication. It prints a Markdown report and exits
1 when a newer edition is out, a copied file changed upstream or a copy
differs.

Set ``GITHUB_TOKEN`` to raise the API rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "src" / "nist_sp_800_53" / "schema" / "oscal-content"
API = "https://api.github.com/repos/usnistgov/oscal-content"
DOI_API = "https://doi.org/api/handles/"
USER_AGENT = "lmodel-nist-sp-800-53-upstream-check"

# The release and the commit its tag names. Move them together when the copy
# is replaced from a newer release, with PINNED_BLOBS and the schema header's
# annotations.
PINNED_TAG = "v1.6.0"
PINNED_COMMIT = "f0de6d8d8c059d374f15e0ae07508d82e370fc1d"

# The folder that holds the pinned edition's catalog and baselines, and the
# folder that holds every edition NIST has published in OSCAL. Revision 4
# is there too, superseded; a third folder would be a newer edition.
PINNED_PATH = "nist.gov/SP800-53/rev5/json"
EDITIONS_PATH = "nist.gov/SP800-53"
PINNED_EDITIONS = {"rev4", "rev5"}

# Each copied file, the path it was taken from at PINNED_COMMIT, and its git
# object hash there. tests/test_upstream.py checks the hashes offline.
PINNED_BLOBS = {
    "NIST_SP-800-53_rev5_catalog.json": (
        f"{PINNED_PATH}/NIST_SP-800-53_rev5_catalog.json",
        "55eb9f2506cab43e051eeac6b48496246afcfd2c",
    ),
    "NIST_SP-800-53_rev5_LOW-baseline_profile.json": (
        f"{PINNED_PATH}/NIST_SP-800-53_rev5_LOW-baseline_profile.json",
        "84edda2906a0edcb5e180034119e0501fc57691e",
    ),
    "NIST_SP-800-53_rev5_MODERATE-baseline_profile.json": (
        f"{PINNED_PATH}/NIST_SP-800-53_rev5_MODERATE-baseline_profile.json",
        "f0d1a6ecffa9b033480563a1f46bbac3f4ec7c41",
    ),
    "NIST_SP-800-53_rev5_HIGH-baseline_profile.json": (
        f"{PINNED_PATH}/NIST_SP-800-53_rev5_HIGH-baseline_profile.json",
        "9e275cbcc1e97e0ad52cb3dbd3cf668d653b409f",
    ),
    "NIST_SP-800-53_rev5_PRIVACY-baseline_profile.json": (
        f"{PINNED_PATH}/NIST_SP-800-53_rev5_PRIVACY-baseline_profile.json",
        "63c6ee354dbb2ddf17da03a3d186de26b9fabc2a",
    ),
    "LICENSE.md": ("LICENSE.md", "109af23dd24c2c465143aeab12ffebfffe2a4cd5"),
}

# The edition the schema renders, as its digital object identifier (DOI), and
# the identifier NIST would give the next final edition. Drafts of that
# edition are reported, not acted on: the schema follows final editions. A
# new release of Revision 5, such as 5.2.0 was, reaches this script through
# the catalog's blob, not through a DOI.
PINNED_DOI = "10.6028/NIST.SP.800-53r5"
NEXT_FINAL_DOI = "10.6028/NIST.SP.800-53r6"
NEXT_DRAFT_DOIS = (
    "10.6028/NIST.SP.800-53r6.ipd",
    "10.6028/NIST.SP.800-53r6.2pd",
    "10.6028/NIST.SP.800-53r6.fpd",
)


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        # urllib copies ordinary headers onto a redirect, so the token is not one.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _version_key(tag: str) -> tuple[int, ...]:
    """Numeric parts of a tag, padded so that v1.6 and v1.6.0 order alike."""
    parts = [int(x) for x in re.findall(r"\d+", tag)]
    return tuple(parts + [0] * (4 - len(parts)))


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the contents API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _listing(path: str, ref: str) -> dict[str, dict]:
    """The entries of one folder at a ref, by name."""
    entries = json.loads(_get(f"{API}/contents/{path}?ref={ref}"))
    if isinstance(entries, dict):
        entries = [entries]
    return {e["name"]: e for e in entries}


def _doi_registered(doi: str) -> bool:
    """Whether doi.org knows the identifier. Code 1 is found, 100 is not."""
    try:
        answer = json.loads(_get(DOI_API + doi))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return False
        raise
    return answer.get("responseCode") == 1


def check_editions() -> tuple[list[str], bool]:
    """Report whether NIST has published another edition of SP 800-53."""
    report, attention = [], False
    if not _doi_registered(PINNED_DOI):
        attention = True
        report.append(
            f"- **doi.org no longer knows `{PINNED_DOI}`**, the pinned edition."
        )
    if _doi_registered(NEXT_FINAL_DOI):
        attention = True
        report.append(
            f"- **NIST has registered `{NEXT_FINAL_DOI}`, the next final edition of SP 800-53.** "
            f"Read https://doi.org/{NEXT_FINAL_DOI}, decide whether the schema moves to it, and "
            "replace the copies once usnistgov/oscal-content publishes its catalog."
        )
    else:
        report.append(
            f"- No final edition after the pinned one: `{NEXT_FINAL_DOI}` is not registered."
        )
    drafts = [doi for doi in NEXT_DRAFT_DOIS if _doi_registered(doi)]
    if drafts:
        report.append(
            "- Drafts of the next edition, for information: "
            + ", ".join(f"https://doi.org/{doi}" for doi in drafts)
            + "."
        )
    return report, attention


def check_catalog() -> tuple[list[str], bool]:
    """Report whether the catalog and baseline copies are current and intact."""
    report = [
        f"- Pinned release: usnistgov/oscal-content {PINNED_TAG}, commit "
        f"`{PINNED_COMMIT[:12]}`, the catalog and the four baseline profiles of "
        f"`{PINNED_PATH}/` copied to `src/nist_sp_800_53/schema/oscal-content/`."
    ]
    attention = False

    latest = json.loads(_get(f"{API}/releases/latest"))["tag_name"]
    if _version_key(latest) > _version_key(PINNED_TAG):
        theirs = _listing(PINNED_PATH, latest)
        changed = sorted(
            name
            for name, (source, pinned_sha) in PINNED_BLOBS.items()
            if source.startswith(PINNED_PATH + "/")
            and theirs.get(name, {}).get("sha") != pinned_sha
        )
        if changed:
            attention = True
            report.append(
                f"- **usnistgov/oscal-content {latest} changes "
                + ", ".join(f"`{name}`" for name in changed)
                + f".** Replace the copies in `src/nist_sp_800_53/schema/oscal-content/` with the "
                f"files at that tag (https://github.com/usnistgov/oscal-content/tree/{latest}/"
                f"{PINNED_PATH}), move the pins here and in the schema header, and run `just test`."
            )
        else:
            report.append(
                f"- Latest release: {latest}, which holds the pinned catalog and baselines unchanged."
            )
        editions = {
            n for n, e in _listing(EDITIONS_PATH, latest).items() if e["type"] == "dir"
        }
        if editions - PINNED_EDITIONS:
            attention = True
            report.append(
                f"- **usnistgov/oscal-content {latest} holds another edition of SP 800-53:** "
                + ", ".join(
                    f"`{EDITIONS_PATH}/{e}/`"
                    for e in sorted(editions - PINNED_EDITIONS)
                )
                + "."
            )
    else:
        report.append(f"- Latest release: {latest}, the pinned one.")

    matching, differing = 0, []
    listings: dict[str, dict[str, dict]] = {}
    for name, (source, pinned_sha) in sorted(PINNED_BLOBS.items()):
        path = COPY / name
        folder, _, base = source.rpartition("/")
        if folder not in listings:
            listings[folder] = _listing(folder or base, PINNED_COMMIT)
        upstream = listings[folder].get(base, {}).get("sha")
        if not path.is_file():
            differing.append(f"`{name}` is missing from the copy")
        elif upstream != pinned_sha:
            differing.append(f"`{source}` at {PINNED_TAG} is not the pinned blob")
        elif _blob_sha(path) != pinned_sha:
            differing.append(f"`{name}` differs from `{source}` at {PINNED_TAG}")
        else:
            matching += 1
    extra = sorted(p.name for p in COPY.iterdir() if p.name not in PINNED_BLOBS)
    differing += [f"`{name}` is in the copy but not pinned" for name in extra]
    report.append(
        f"- {matching} of {len(PINNED_BLOBS)} copied files match the pinned commit byte for byte."
    )
    if differing:
        attention = True
        report.append(f"- **{len(differing)} problem(s) with the copy:**")
        report += [f"  - {d}" for d in differing]
    return report, attention


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for part in (check_editions, check_catalog):
        found, needs = part()
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
