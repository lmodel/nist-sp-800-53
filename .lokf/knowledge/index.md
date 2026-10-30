---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/nist-sp-800-53/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: nist-sp-800-53 Knowledge Bundle
description: NIST SP 800-53 Security and Privacy Controls Release 5.2.0 with SP 800-53A and SP 800-53B (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# nist-sp-800-53 Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for nist-sp-800-53. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The Astro Starlight site in `website/`, for <https://lmodel.github.io/nist-sp-800-53>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website.

# Datasets

* [nist-sp-800-53 LinkML schema](datasets/nist-sp-800-53-linkml-schema.md) - The LinkML schema of the SP 800-53 controls at Release 5.2.0, `src/nist_sp_800_53/schema/nist_sp_800_53.yaml` (schema id `https://w3id.org/lmodel/nist-sp-800-53`, version 5.2.0): eleven classes, five enums and six identifier types. Its `lokf adapt` copy `.lokf/nist-sp-800-53.yaml`, rooted on the family, the control, the control enhancement and the baseline, is the bundle's domain schema.
* [NIST's SP 800-53 catalog and baseline copies](datasets/sp-800-53-catalog-copy.md) - NIST's catalog of SP 800-53 Release 5.2.0 in the Open Security Controls Assessment Language (OSCAL), with the SP 800-53A procedures inside it, and the four SP 800-53B baseline profiles, copied with NIST's licence from usnistgov/oscal-content v1.6.0 into `src/nist_sp_800_53/schema/oscal-content/` and matched to that release by git object hash. The tests derive the whole release from them.
* [Generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and Java), the Python dataclasses and Pydantic models in `src/nist_sp_800_53/datamodel/`, `docs/schema/` and `docs/elements/`, and `.lokf/nist-sp-800-53.yaml`. None is edited by hand.
* [Test data and tests](datasets/test-data.md) - The schema's tests: sixteen valid examples and thirty-four counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which derives Release 5.2.0 from NIST's catalog and baselines, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies in `tests/neighbours/`.

# References

* [NIST SP 800-53 Revision 5, Release 5.2.0](references/sp-800-53.md) - NIST Special Publication 800-53, Revision 5, Security and Privacy Controls for Information Systems and Organizations (September 2020, updated December 2020; Release 5.2.0 of August 2025; <https://doi.org/10.6028/NIST.SP.800-53r5>), the publication the schema renders at its current release.
* [NIST SP 800-53A Revision 5](references/sp-800-53a.md) - NIST Special Publication 800-53A, Revision 5, Assessing Security and Privacy Controls in Information Systems and Organizations (<https://doi.org/10.6028/NIST.SP.800-53Ar5>): the assessment objectives, methods and parameter labels that NIST's catalog carries for each control and enhancement, and that the schema renders.
* [NIST SP 800-53B](references/sp-800-53b.md) - NIST Special Publication 800-53B, Control Baselines for Information Systems and Organizations (<https://doi.org/10.6028/NIST.SP.800-53B>): the Low, Moderate, High and Privacy baselines, which NIST publishes as four OSCAL profiles at Release 5.2.0 and the schema renders as `Sp80053Baseline`.

# Explanations

* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the schema renders and what it leaves out: SP 800-53 Revision 5 at Release 5.2.0 with SP 800-53A and SP 800-53B, as NIST's catalog and baseline profiles carry them, with lmodel/nist-sp-800-218 and lmodel/slsa as its influences on layout. It maps its classes to lmodel/oscal's, and models neither the resolved baseline catalogs, the catalog's own metadata, the CPRT exports nor Revision 4.
* [Element names and the shared namespace](explanations/element-names.md) - How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies: classes with the `Sp80053` prefix, generic nouns qualified with the publication's own, NIST's identifiers kept as printed, upper-case enum values, `title` and `description` carrying LOKF's IRIs, and no other key shared, which `tests/test_schema_rules.py` checks.

# Glossary

* [Control family](glossary/control-family.md) - In SP 800-53, one of the twenty families the controls are sorted into, such as Access Control (AC) or Supply Chain Risk Management (SR). The schema renders a family as `Sp80053Family`, with its two letters in `family_id`.
* [Control](glossary/control.md) - In SP 800-53, a security or privacy control: a safeguard with an identifier such as AC-2, a statement, a discussion, parameters, related controls, references and enhancements. The schema renders a control as `Sp80053Control`, with its identifier in `control_identifier`; a withdrawn one keeps its identifier and says where it went.
* [Control enhancement](glossary/control-enhancement.md) - In SP 800-53, a control enhancement: added functionality or strength for a control, with an identifier such as AC-2(1), cited apart from its control. The schema renders one as `Sp80053ControlEnhancement`, with its identifier in `enhancement_id` and the control it requires in `required_controls`.
* [Organization-defined parameter](glossary/organization-defined-parameter.md) - In SP 800-53, an organization-defined parameter (ODP): a value the statement leaves to the organization, an assignment or a selection, which SP 800-53A labels such as AC-02_ODP[01]. The schema renders one as `Sp80053Parameter`, with the catalog's identifier in `parameter_id`.
* [Assessment objective](glossary/assessment-objective.md) - In SP 800-53A, an assessment objective: a determination statement an assessor checks, nested as the control statement's items are, with a label such as AC-02a.[01]. The schema renders one as `Sp80053AssessmentObjective`, with its label in `objective_label`.
* [Assessment method](glossary/assessment-method.md) - In SP 800-53A, an assessment method: examine, interview or test, applied to the documents, people or mechanisms an assessor selects from. The schema renders one as `Sp80053AssessmentMethod`, with the method in `assessment_method` and its objects in `assessment_objects`.
* [Control baseline](glossary/control-baseline.md) - In SP 800-53B, a control baseline: the controls and enhancements selected for a low, moderate or high impact system, or for privacy. The schema renders one as `Sp80053Baseline`, with its level in `baseline_level` and its selections in `baseline_controls`.

# Families

* [Access Control](families/access-control.md) - The SP 800-53 family AC, Access Control: 25 controls and 122 control enhancements in Release 5.2.0, of which 2 controls and 14 enhancements are withdrawn.
* [Awareness and Training](families/awareness-and-training.md) - The SP 800-53 family AT, Awareness and Training: 6 controls and 11 control enhancements in Release 5.2.0, of which 1 control and 1 enhancement are withdrawn.
* [Audit and Accountability](families/audit-and-accountability.md) - The SP 800-53 family AU, Audit and Accountability: 16 controls and 53 control enhancements in Release 5.2.0, of which 1 control and 12 enhancements are withdrawn.
* [Assessment, Authorization, and Monitoring](families/assessment-authorization-and-monitoring.md) - The SP 800-53 family CA, Assessment, Authorization, and Monitoring: 9 controls and 23 control enhancements in Release 5.2.0, of which 1 control and 6 enhancements are withdrawn.
* [Configuration Management](families/configuration-management.md) - The SP 800-53 family CM, Configuration Management: 14 controls and 52 control enhancements in Release 5.2.0, of which 0 controls and 10 enhancements are withdrawn.
* [Contingency Planning](families/contingency-planning.md) - The SP 800-53 family CP, Contingency Planning: 13 controls and 43 control enhancements in Release 5.2.0, of which 1 control and 6 enhancements are withdrawn.
* [Identification and Authentication](families/identification-and-authentication.md) - The SP 800-53 family IA, Identification and Authentication: 13 controls and 61 control enhancements in Release 5.2.0, of which 0 controls and 15 enhancements are withdrawn.
* [Incident Response](families/incident-response.md) - The SP 800-53 family IR, Incident Response: 10 controls and 32 control enhancements in Release 5.2.0, of which 1 control and 1 enhancement are withdrawn.
* [Maintenance](families/maintenance.md) - The SP 800-53 family MA, Maintenance: 7 controls and 23 control enhancements in Release 5.2.0, of which 0 controls and 2 enhancements are withdrawn.
* [Media Protection](families/media-protection.md) - The SP 800-53 family MP, Media Protection: 8 controls and 22 control enhancements in Release 5.2.0, of which 0 controls and 10 enhancements are withdrawn.
* [Physical and Environmental Protection](families/physical-and-environmental-protection.md) - The SP 800-53 family PE, Physical and Environmental Protection: 23 controls and 36 control enhancements in Release 5.2.0, of which 1 control and 7 enhancements are withdrawn.
* [Planning](families/planning.md) - The SP 800-53 family PL, Planning: 11 controls and 6 control enhancements in Release 5.2.0, of which 3 controls and 3 enhancements are withdrawn.
* [Program Management](families/program-management.md) - The SP 800-53 family PM, Program Management: 32 controls and 5 control enhancements in Release 5.2.0, none withdrawn.
* [Personnel Security](families/personnel-security.md) - The SP 800-53 family PS, Personnel Security: 9 controls and 9 control enhancements in Release 5.2.0, of which 0 controls and 1 enhancement are withdrawn.
* [Personally Identifiable Information Processing and Transparency](families/personally-identifiable-information-processing-and-transparency.md) - The SP 800-53 family PT, Personally Identifiable Information Processing and Transparency: 8 controls and 13 control enhancements in Release 5.2.0, none withdrawn.
* [Risk Assessment](families/risk-assessment.md) - The SP 800-53 family RA, Risk Assessment: 10 controls and 16 control enhancements in Release 5.2.0, of which 1 control and 3 enhancements are withdrawn.
* [System and Services Acquisition](families/system-and-services-acquisition.md) - The SP 800-53 family SA, System and Services Acquisition: 24 controls and 123 control enhancements in Release 5.2.0, of which 7 controls and 32 enhancements are withdrawn.
* [System and Communications Protection](families/system-and-communications-protection.md) - The SP 800-53 family SC, System and Communications Protection: 51 controls and 111 control enhancements in Release 5.2.0, of which 4 controls and 19 enhancements are withdrawn.
* [System and Information Integrity](families/system-and-information-integrity.md) - The SP 800-53 family SI, System and Information Integrity: 23 controls and 96 control enhancements in Release 5.2.0, of which 1 control and 16 enhancements are withdrawn.
* [Supply Chain Risk Management](families/supply-chain-risk-management.md) - The SP 800-53 family SR, Supply Chain Risk Management: 12 controls and 15 control enhancements in Release 5.2.0, none withdrawn.

# Baselines

* [Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.2.0 LOW IMPACT BASELINE](baselines/low.md) - The SP 800-53B Low baseline at Release 5.2.0, as NIST's profile selects it: 149 identifiers, 131 controls and 18 control enhancements, from 18 families.
* [Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.2.0 MODERATE IMPACT BASELINE](baselines/moderate.md) - The SP 800-53B Moderate baseline at Release 5.2.0, as NIST's profile selects it: 287 identifiers, 177 controls and 110 control enhancements, from 18 families.
* [Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.1.1 HIGH IMPACT BASELINE](baselines/high.md) - The SP 800-53B High baseline at Release 5.2.0, as NIST's profile selects it: 370 identifiers, 188 controls and 182 control enhancements, from 18 families.
* [Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.2.0 PRIVACY BASELINE](baselines/privacy.md) - The SP 800-53B Privacy baseline at Release 5.2.0, as NIST's profile selects it: 96 identifiers, 75 controls and 21 control enhancements, from 16 families.

# Playbooks

* [Regenerate and test after a schema change](playbooks/regenerate-and-test.md) - How to change the schema and check it: `uv sync --group dev`, edit `src/nist_sp_800_53/schema/nist_sp_800_53.yaml`, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request.
* [Validate data against the schema](playbooks/validate-data.md) - How to validate SP 800-53 data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No check covers the nesting of identifiers, a repeated one, or what a withdrawn element carries.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the weekly upstream watch reports that NIST registered the next final edition of SP 800-53, released a changed catalog or baseline in usnistgov/oscal-content, or that a copy drifted: replace the copies whole from one release, move the pins in `scripts/check_upstream_release.py` and the schema header, and run the tests.
* [Cut a release](playbooks/release.md) - How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-nist-sp-800-53.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [AI covenant](policies/ai-covenant.md) - The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders SP 800-53, SP 800-53A or SP 800-53B in the project's own words and cites it, NIST's catalog and baseline copies are never edited, and the scheduled librarian proposes changes only through reviewed pull requests.
* [License and attribution](policies/license-and-attribution.md) - The repository's licences: Apache 2.0 for the schema and the code, NIST's public-domain and CC0 terms for the catalog and baseline copies, NIST's statement that SP 800-53, SP 800-53A and SP 800-53B are not subject to copyright in the United States, MIT for the copier template's scaffolding, and Apache 2.0 for the KTL sidecar and website templates.
* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, and the three repository settings that are not yet in force.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/nist-sp-800-53.yaml` is current.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its sp-800-53-copies job runs `scripts/check_upstream_release.py` against NIST's editions and usnistgov/oscal-content, and on a finding opens or updates the issue titled Upstream watch: NIST's SP 800-53 has changed.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-nist-sp-800-53.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true.
