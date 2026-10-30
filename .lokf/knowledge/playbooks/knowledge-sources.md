---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose."
resource: .
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/nist_sp_800_53/schema
  - resource: src/nist_sp_800_53/datamodel
  - resource: project.justfile
  - resource: .lokf/nist-sp-800-53.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: NOTICE
  - resource: LICENSE
  - resource: scripts/check_upstream_release.py
  - resource: .github/scripts
  - resource: .github/workflows
  - resource: .github/dependabot.yml
  - resource: justfile
  - resource: .linkml/generators.yaml
  - resource: .linkmllint.yaml
  - resource: .pre-commit-config.yaml
  - resource: project
  - resource: docs/schema
  - resource: docs/elements
  - resource: tests
  - resource: CONTRIBUTING.md
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: website
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
  - resource: .claude/CLAUDE.md
exclusions:
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and spell checkers' settings; the changelog states the Python project's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: config.public.mk
    reason: "Tooling: the variables the justfile loads."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: src/nist_sp_800_53/schema/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: examples/README.md
    reason: Text from the project template about generated example output.
  - resource: src/nist_sp_800_53/__init__.py
    reason: Package plumbing.
  - resource: src/nist_sp_800_53/_version.py
    reason: Package plumbing.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sidecar sync's pull request template.
  - resource: .lokf/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, which the weekly sync replaces.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill builder and its instructions.
  - resource: .lokf/README.md
    reason: The sidecar's own README.
  - resource: .lokf/queries.http
    reason: The sidecar's sample queries.
  - resource: .lokf/ingest.yaml.sample
    reason: The sidecar's example ingest manifest, which this host does not use.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file.
  - resource: .lokf/.gitignore
    reason: The sidecar's git settings.
  - resource: .lokf/.gitattributes
    reason: The sidecar's git settings.
generated:
  by: process:ktl-librarian
  at: "2026-10-30T09:09:14Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:05:26Z"
---

# Knowledge sources

Steady-state refresh runs re-verify these sources instead of discovering them again. Update this map whenever the repository's knowledge geography changes.

Each concept derived from a file or folder of this repository names it by its path from the repository root, in `resource` and in `sources`. `knowledge-report.sh worklist` lists the concepts whose source moved since their stamp. It never fetches a page, so re-read the publications' pages when the schema header's version or the upstream pins move.

| Source | Yields | Re-check by |
| --- | --- | --- |
| `src/nist_sp_800_53/schema/nist_sp_800_53.yaml` | `datasets/nist-sp-800-53-linkml-schema`, the seven `glossary/` terms, the three `references/` | re-read the header's `version`, `source`, `see_also`, annotations and comments, each class's required slots and patterns, the enums' values and the `broad_mappings` |
| `project.justfile`, `.lokf/nist-sp-800-53.yaml`, `.lokf/justfile`, `.lokf/pyproject.toml`, the README's Knowledge Trust Ladder (KTL) section | the domain-schema section of `datasets/nist-sp-800-53-linkml-schema` | re-read the `--root` list, the copy's notes, the `schema :=` line and the `[tool.lokf]` table |
| `src/nist_sp_800_53/schema/oscal-content/`, the NIST sections of `NOTICE` | `datasets/sp-800-53-catalog-copy`, the twenty `families/`, the four `baselines/`, the three `references/` | re-read the catalog's metadata, its groups and their controls and enhancements, and each profile's `with-ids`; the upstream watch compares the blobs weekly |
| `scripts/check_upstream_release.py`, `.github/scripts/` | `playbooks/update-upstream-pins`, `workflows/upstream-watch`, `references/sp-800-53` | re-read the pins, the digital object identifiers and the issue title |
| `README.md` (What it models, Influences, Mappings, Not modelled here), `docs/about.md`, `.linkmllint.yaml`, `CHANGELOG.md` | `explanations/scope-and-influences`, `explanations/element-names` | re-read each section and the lint comment |
| `justfile`, `.linkml/generators.yaml`, `project/`, `src/nist_sp_800_53/datamodel/`, `docs/schema/`, `docs/elements/`, `.pre-commit-config.yaml` | `datasets/generated-artefacts` | re-read the `gen-project`, `gen-doc` and `test` recipes and the `excludes`; re-list `project/*/` |
| `tests/` | `datasets/test-data` | re-count `valid/` and `invalid/`; re-read the tests and the neighbours' checksums |
| the Validating data section of `docs/index.md` | `playbooks/validate-data` | re-read the section |
| `CONTRIBUTING.md`, `.claude/CLAUDE.md`, the `lint`, `gen-project`, `gen-doc` and `test` recipes | `playbooks/regenerate-and-test` | confirm the setup, the checklist and the recipes |
| `.releaserc.json`, `.github/scripts/changelog-release.mjs`, `CHANGELOG.md`, the Releasing section of `CONTRIBUTING.md` | `playbooks/release` | re-read the release rules, the commands and the baseline paragraph |
| the nine files in `.github/workflows/` | the nine `workflows/` concepts | re-read each file's `on` keys, its jobs' permissions and environments, and the variables and secrets it reads |
| `.github/release/` | `workflows/semantic-release` | re-read `package.json` and the versions the lockfile pins |
| `website/` | `services/documentation-site` | re-read `site.config.mjs` and `website/README.md` |
| `NOTICE`, `LICENSE`, `website/NOTICE`, the License section of `README.md` | `policies/license-and-attribution` | re-read each third-party entry |
| `SECURITY.md`, `.github/dependabot.yml` | `policies/security-policy` | re-read the table of surfaces and the settings not yet in force |
| `AI_COVENANT.md` | `policies/ai-covenant` | re-read the project note and the section on agent automation |
| <https://doi.org/10.6028/NIST.SP.800-53r5>, <https://doi.org/10.6028/NIST.SP.800-53Ar5>, <https://doi.org/10.6028/NIST.SP.800-53B> and the pages the schema header's `see_also` lists | the `resource` of each `references/` concept | external pages, named but not read by this bootstrap, which took the publications' facts from NOTICE, the schema header and the catalog's metadata; read them when the upstream watch reports a new edition |

The paths under `exclusions` were looked at and left out, each for the reason it gives. They are governance text, tooling settings, template text, package plumbing, the pointer for agents, and the sidecar's own files. Of the sidecar's files, the domain schema, the justfile's `schema :=` line and the `[tool.lokf]` table are sources.
