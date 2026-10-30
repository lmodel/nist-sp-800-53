# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

## [0.1.0] - 2026-10-30

### Added

- **A LinkML schema of the security and privacy controls of NIST Special Publication (SP) 800-53, Revision 5, at Release 5.2.0**, with the assessment procedures of SP 800-53A and the baselines of SP 800-53B. It holds the twenty families, the 324 controls and 872 control enhancements with their statements, discussions, organization-defined parameters, related controls and references, the assessment objectives and methods of each, the 182 withdrawn controls and enhancements with where each went or why, and the Low, Moderate, High and Privacy baselines.
- **Copies of NIST's catalog and four baseline profiles from usnistgov/oscal-content v1.6.0, and a weekly upstream watch.** A test derives the whole release from the copies and holds it to the validator and to the release's counts, and the watch also asks doi.org whether NIST has published the next final edition.
- **`.lokf/nist-sp-800-53.yaml`, the schema's `lokf adapt` copy, rooted on the family, the control, the control enhancement and the baseline.** The knowledge release attaches it as `schema-<tag>-nist-sp-800-53.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies, with which it shares no key.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The schema models the publication's own elements, not a copy of a catalog in the Open Security Controls Assessment Language (OSCAL) or of a Cybersecurity and Privacy Reference Tool (CPRT) export.** The OSCAL-shaped classes shared names with LOKF's and lmodel/oscal's, and their `class_uri: linkml:Any` let a document with any keys validate.
- **The schema's name is `nist_sp_800_53`, as its file and package are, and the Python project's name is `nist-sp-800-53-linkml`.** PyPI publishing stays off.

### Removed

- **The CPRT exports, the NIST and hyperGRC fixtures and the SSSOM overlay script.** The CPRT API gives no release or hash to pin, and the fixtures validated the OSCAL shape, which lmodel/oscal models.
- **The PyPI publishing workflow and the mkdocs site and its preview.** The knowledge website replaces the site.
