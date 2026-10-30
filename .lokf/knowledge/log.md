# Change Log

## 2026-10-30

* **Changed**: nist-sp-800-53 LinkML schema: the four identifiers are slots listed first in their classes, so the generated dataclasses key each inlined list by its identifier.
* **Changed**: Scope, influences and mappings says that SC-19 and CP-10(3) give a reason for their withdrawal in place of a destination, as `docs/about.md` now does.
* **Prose**: reworded 33 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the generators' settings moved from `config.yaml` to `.linkml/generators.yaml`.
* **Changed**: nist-sp-800-53 LinkML schema: the four concept classes require a title, the parameter maps to `oscal:Parameter`, and the README says how many references a control cites.
* **Changed**: NIST's SP 800-53 catalog and baseline copies: two withdrawn elements give a reason rather than a link, and the watch checks that the tag still names the pinned commit.
* **Changed**: Test data and tests: forty-one counter-examples, each naming where it fails, the tests that hold examples to the catalog, parameter prefixes and lists without repeats, and the stubbed watch tests.
* **Changed**: Update the upstream pins: the watch's new findings, and a step that regenerates the artefacts and the adapt copy after the header moves.
* **Changed**: the four workflows the repository owns now stop each job after a set time, `main.yaml` installs just 1.47.0, and the release title check names rebase and merge.
* **Changed**: Security policy: Dependabot also watches the website's npm packages.
* **Changed**: Documentation site: the retired schema's class pages redirect to their successors.
* **Changed**: Validate data against the schema: the rules `docs/index.md` lists name the `_prm_` parameters' prefix and a statement's text or items.
* **Changed**: Regenerate and test after a schema change: a counter-example opens with the line that says where it fails.
* **Changed**: Scope, influences and mappings: the 192 references are those the catalog lists, not all cited by a control.
* **Changed**: NIST SP 800-53A Revision 5: the aggregating parameters carry no SP 800-53A label, and not every parameter has a guideline.
* **Changed**: Control enhancement: SC-42(2) requires its own control as well as SC-42(1).
* **Changed**: Organization-defined parameter: the placeholder reads `{{ insert: param, <identifier> }}`, with two braces each side, as the catalog writes it.
* **Changed**: Security policy now says that a ruleset on `main` blocks deletion and force-pushes, as `SECURITY.md` does since the repository's settings were read; two settings remain not in force.
* **Added**: Documentation site, from `website/site.config.mjs` and `website/README.md`.
* **Added**: nist-sp-800-53 LinkML schema, from `src/nist_sp_800_53/schema/nist_sp_800_53.yaml`, its adapt copy and the lokf-adapt recipes.
* **Added**: NIST's SP 800-53 catalog and baseline copies, from `src/nist_sp_800_53/schema/oscal-content/`, NOTICE and the watch's pins.
* **Added**: Generated artefacts, from the justfile's recipes, `config.yaml` and `project/`.
* **Added**: Test data and tests, from `tests/`.
* **Added**: NIST SP 800-53 Revision 5, Release 5.2.0, from NOTICE, the schema header and the catalog's metadata.
* **Added**: NIST SP 800-53A Revision 5, from the schema header, the catalog's parts and NOTICE.
* **Added**: NIST SP 800-53B, from the four baseline profiles, the schema header and NOTICE.
* **Added**: Scope, influences and mappings, from the README, the changelog and `docs/about.md`.
* **Added**: Element names and the shared namespace, from `docs/about.md`, the README, `.linkmllint.yaml` and the schema rules test.
* **Added**: Control family, from the class `Sp80053Family` and NIST's catalog copy.
* **Added**: Control, from the class `Sp80053Control` and NIST's catalog copy.
* **Added**: Control enhancement, from the class `Sp80053ControlEnhancement` and NIST's catalog copy.
* **Added**: Organization-defined parameter, from the class `Sp80053Parameter` and NIST's catalog copy.
* **Added**: Assessment objective, from the class `Sp80053AssessmentObjective` and NIST's catalog copy.
* **Added**: Assessment method, from the class `Sp80053AssessmentMethod` and NIST's catalog copy.
* **Added**: Control baseline, from the class `Sp80053Baseline` and NIST's catalog copy.
* **Added**: Access Control, the family AC, from NIST's catalog copy.
* **Added**: Awareness and Training, the family AT, from NIST's catalog copy.
* **Added**: Audit and Accountability, the family AU, from NIST's catalog copy.
* **Added**: Assessment, Authorization, and Monitoring, the family CA, from NIST's catalog copy.
* **Added**: Configuration Management, the family CM, from NIST's catalog copy.
* **Added**: Contingency Planning, the family CP, from NIST's catalog copy.
* **Added**: Identification and Authentication, the family IA, from NIST's catalog copy.
* **Added**: Incident Response, the family IR, from NIST's catalog copy.
* **Added**: Maintenance, the family MA, from NIST's catalog copy.
* **Added**: Media Protection, the family MP, from NIST's catalog copy.
* **Added**: Physical and Environmental Protection, the family PE, from NIST's catalog copy.
* **Added**: Planning, the family PL, from NIST's catalog copy.
* **Added**: Program Management, the family PM, from NIST's catalog copy.
* **Added**: Personnel Security, the family PS, from NIST's catalog copy.
* **Added**: Personally Identifiable Information Processing and Transparency, the family PT, from NIST's catalog copy.
* **Added**: Risk Assessment, the family RA, from NIST's catalog copy.
* **Added**: System and Services Acquisition, the family SA, from NIST's catalog copy.
* **Added**: System and Communications Protection, the family SC, from NIST's catalog copy.
* **Added**: System and Information Integrity, the family SI, from NIST's catalog copy.
* **Added**: Supply Chain Risk Management, the family SR, from NIST's catalog copy.
* **Added**: Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.2.0 LOW IMPACT BASELINE, the Low baseline, from NIST's profile `NIST_SP-800-53_rev5_LOW-baseline_profile.json`.
* **Added**: Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.2.0 MODERATE IMPACT BASELINE, the Moderate baseline, from NIST's profile `NIST_SP-800-53_rev5_MODERATE-baseline_profile.json`.
* **Added**: Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.1.1 HIGH IMPACT BASELINE, the High baseline, from NIST's profile `NIST_SP-800-53_rev5_HIGH-baseline_profile.json`.
* **Added**: Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.2.0 PRIVACY BASELINE, the Privacy baseline, from NIST's profile `NIST_SP-800-53_rev5_PRIVACY-baseline_profile.json`.
* **Open question**: Electronic (OSCAL) Version of NIST Special Publication 800-53 Revision 5.1.1 HIGH IMPACT BASELINE: the profile's title names Revision 5.1.1 while its metadata version is 5.2.0 and the other three titles name 5.2.0; is the title NIST's slip, to be reported upstream, or does the High baseline carry a different release?
* **Added**: Regenerate and test after a schema change, from CONTRIBUTING.md, the recipes and `.claude/CLAUDE.md`.
* **Added**: Validate data against the schema, from `docs/index.md`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py`, its tests and the watch workflow.
* **Added**: Cut a release, from `.releaserc.json`, the changelog and CONTRIBUTING.md.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: License and attribution, from NOTICE, LICENSE, website/NOTICE and the README.
* **Added**: Security policy, from `SECURITY.md` and the Dependabot settings.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Knowledge sources map, the bootstrap's map of what each source yields and how to re-check it, with the paths left out on purpose.
* **Removal**: the sidecar's two example services, which the bootstrap's concepts replace.

## 2026-10-29

* **Initialization**: Scaffolded the LOKF bundle for nist-sp-800-53 with placeholder
  services. Real concepts to follow.
