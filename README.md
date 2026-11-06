<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-sp-800-53

NIST SP 800-53 Security and Privacy Controls Release 5.2.0 with SP 800-53A and SP 800-53B (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project, for example which controls the privacy baseline selects. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-sp-800-53](https://lmodel.github.io/nist-sp-800-53)

## What it models

The schema models the security and privacy controls that the National Institute of Standards and Technology (NIST) defines in [Special Publication (SP) 800-53, Revision 5](https://doi.org/10.6028/NIST.SP.800-53r5), at Release 5.2.0 of August 2025. It adds the assessment procedures of [SP 800-53A](https://doi.org/10.6028/NIST.SP.800-53Ar5) and the control baselines of [SP 800-53B](https://doi.org/10.6028/NIST.SP.800-53B). The schema holds the twenty families (`Sp80053Family`), the 324 controls (`Sp80053Control`) and 872 control enhancements (`Sp80053ControlEnhancement`) with their parameters and references, the assessment objectives and methods of SP 800-53A, and the Low, Moderate, High and Privacy baselines (`Sp80053Baseline`).

[src/nist_sp_800_53/schema/oscal-content/](src/nist_sp_800_53/schema/oscal-content) holds NIST's catalog and its four baselines in the Open Security Controls Assessment Language (OSCAL), from usnistgov/oscal-content v1.6.0, and `tests/test_upstream.py` derives the whole release from them. A weekly workflow opens an issue when NIST registers the next final edition, changes a copied file, or the copy drifts.

## Mappings

* **OSCAL**: each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`: a family is a group, a control and an enhancement are controls, a baseline is a profile, and a statement, a discussion, an objective and a method are parts.

## Not modelled here

* The four resolved baseline catalogs that usnistgov/oscal-content publishes beside the profiles: they repeat the catalog's controls, and a baseline here is the list of identifiers the profile selects.
* The catalog's own OSCAL metadata and the back-matter entries about the catalog, such as the links to the PDF and to earlier OSCAL releases.
* Each objective's link to the statement item it assesses, which the nesting of the objectives already shows.
* NIST's Cybersecurity and Privacy Reference Tool exports of the same release: the tool gives no release or hash to pin, and the identifier it gives the release is in the schema's annotations.
* SP 800-53 Revision 4, which usnistgov/oscal-content still carries, and the parts of SP 800-53A and SP 800-53B that the catalog and the profiles do not carry, such as SP 800-53B's tailoring guidance.
* The rules no pattern can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/nist_sp_800_53/schema/](src/nist_sp_800_53/schema): the LinkML schema, `nist_sp_800_53.yaml` (edit this), and NIST's catalog and baseline copies
* [src/nist_sp_800_53/datamodel/](src/nist_sp_800_53/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/schema/nist-sp-800-53.yaml`, is the copy `just lokf-adapt` writes from `src/nist_sp_800_53/schema/nist_sp_800_53.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-sp-800-53.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots these classes on `Concept`, so a concept may name any of them as its `type`. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
Sp80053Family, Sp80053Control, Sp80053ControlEnhancement, Sp80053Baseline
```

A concept writes the publication's identifier in `family_id`, `control_identifier` or `enhancement_id`, and a baseline's level in `baseline_level`. An enhancement's concept names its control's concept in `isPartOf`, and a control's concept names its family's.

No class, enum or type of the copy shares a name with LOKF's schema or with another lmodel copy, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

SP 800-53, SP 800-53A and SP 800-53B are works of the United States Government and are not subject to copyright in the United States. The schema's descriptions are this project's own words, and NIST's catalog and baselines keep NIST's licence beside them: see [NOTICE](NOTICE). This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
