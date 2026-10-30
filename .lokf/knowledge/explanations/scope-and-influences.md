---
type: Explanation
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the schema renders and what it leaves out: SP 800-53 Revision 5 at Release 5.2.0 with SP 800-53A and SP 800-53B, as NIST's catalog and baseline profiles carry them, with lmodel/nist-sp-800-218 and lmodel/slsa as its influences on layout. It maps its classes to lmodel/oscal's, and models neither the resolved baseline catalogs, the catalog's own metadata, the CPRT exports nor Revision 4."
resource: README.md
about:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/datasets/nist-sp-800-53-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: the What it models, Influences, Mappings and Not modelled here sections
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Unreleased section
  - id: about.md
    resource: docs/about.md
    title: the What is left out section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:48:31Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:09:14Z"
---

# Scope, influences and mappings

The README says the schema models the security and privacy controls of SP 800-53, Revision 5, at Release 5.2.0 of August 2025, with the assessment procedures of SP 800-53A and the control baselines of SP 800-53B. Under one catalog, it holds:

- the twenty families;
- the controls and enhancements, with their statements, discussions, parameters, related controls and references;
- the assessment objectives and methods;
- the 192 publications the catalog lists;
- the four baselines.

Its influences are none beyond the three publications. Its layout follows lmodel/nist-sp-800-218 and its release asset and governance files follow lmodel/slsa.[^readme.md]

The schema crosses to the Open Security Controls Assessment Language (OSCAL) and borrows nothing from it. Each class names its lmodel/oscal counterpart in `broad_mappings`: a family an OSCAL group, a control and an enhancement controls, a statement, discussion, objective and method parts, a parameter a parameter, a reference a back-matter resource and a baseline a profile. The changelog says that the schema replaced classes that copied the OSCAL and CPRT shapes, shared names with LOKF's and lmodel/oscal's, and let a document with any keys validate.[^changelog.md]

The README and `docs/about.md` leave out:

- the resolved baseline catalogs;
- the catalog's own metadata and back-matter entries about the catalog;
- each objective's link to the statement item it assesses;
- NIST's Cybersecurity and Privacy Reference Tool exports;
- Revision 4;
- the prose of SP 800-53A and SP 800-53B outside the catalog and the profiles.

A withdrawn control or enhancement stays, with where it went or, for SC-19 and CP-10(3), why it was withdrawn.[^about.md]

[^readme.md]: README.md, What it models, Influences, Mappings and Not modelled here
[^changelog.md]: CHANGELOG.md, the Changed and Removed entries under Unreleased
[^about.md]: docs/about.md, What is left out
