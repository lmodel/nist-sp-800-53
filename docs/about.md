# About nist-sp-800-53

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says how they are named and what the model leaves out.

NIST Special Publication (SP) 800-53 sorts its controls into families. A
control is a safeguard with a statement of what it requires, a discussion,
parameters the organization defines, related controls and references, and
it may have enhancements, each a control in its own right. SP 800-53A gives
each control and enhancement an assessment objective, a nested set of
determination statements, and the assessment methods an assessor applies.
SP 800-53B selects controls and enhancements into four baselines. The
schema gives each of these a class, and holds the families, the baselines
and the cited publications under one catalog.

Element names are the schema's own. Classes carry the `Sp80053` prefix
(`Sp80053Control`, `Sp80053Baseline`) so they can be imported beside other
vocabularies. Slots are snake_case, and a generic noun is qualified with the
publication's own, as in `control_discussion` and `assessment_objective`.
The identifiers keep the form the National Institute of Standards and
Technology (NIST) prints, such as `AC-2` and `AC-2(1)`; a parameter keeps
the catalog's identifier, such as `ac-02_odp.01`, and the label SP 800-53A
gives it, such as `AC-02_ODP[01]`. The enums' values are upper case, as the
catalog writes the assessment methods `EXAMINE`, `INTERVIEW` and `TEST`.
Every element is in the `nist_sp_800_53:` namespace
(`https://w3id.org/lmodel/nist-sp-800-53/`).

The descriptions are this project's own words. NIST's own text of each
control, parameter, objective and method stays in NIST's catalog, which the
repository keeps beside the schema.

## What is left out

The schema models what the catalog and the four baseline profiles carry at
Release 5.2.0. It leaves out:

- the resolved baseline catalogs;
- the catalog's own metadata and back-matter entries about the catalog;
- each objective's link to the statement item it assesses;
- NIST's Cybersecurity and Privacy Reference Tool exports;
- Revision 4;
- the prose of SP 800-53A and SP 800-53B outside the catalog and the
  profiles.

A withdrawn control or enhancement stays, with
where it went.

## Reference

- [SP 800-53 Revision 5 on NIST's site](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [The Release 5.2.0 announcement](https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls)
- [SP 800-53A Revision 5](https://doi.org/10.6028/NIST.SP.800-53Ar5) and [SP 800-53B](https://doi.org/10.6028/NIST.SP.800-53B)
- [NIST's catalog and baselines in the Open Security Controls Assessment Language](https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/SP800-53/rev5)
