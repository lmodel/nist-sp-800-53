# nist-sp-800-53

This project is a LinkML model of the security and privacy controls that the
National Institute of Standards and Technology (NIST) defines in Special
Publication (SP) 800-53, Revision 5, at Release 5.2.0. It covers the twenty
control families, the controls and control enhancements with their
statements, discussions, organization-defined parameters, related controls
and references, the assessment objectives and methods of SP 800-53A, and the
four control baselines of SP 800-53B.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [`nist_sp_800_53.yaml`](schema/nist_sp_800_53.yaml): the schema

## Validating data

`linkml-validate -s src/nist_sp_800_53/schema/nist_sp_800_53.yaml -C Sp80053Control control.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it.

Validate a file before loading it into either model in
`src/nist_sp_800_53/datamodel/`. LinkML 1.12.1 generates models that check
less:

- The dataclasses check required fields and enum values, but no pattern.
- The Pydantic models also check the patterns a field carries itself, such as
  the form of `catalog_release` or `item_label`. They do not check the
  patterns of the six identifier types, so a family, control, enhancement,
  parameter or withdrawal identifier goes unchecked.

No check covers these rules:

- that a control's identifier starts with its family's letters, an
  enhancement's with its control's identifier, and a parameter's with its
  control's zero-padded identifier;
- that a list never repeats an identifier;
- that a related or required control, a moved-to target, a baseline's
  selection, an aggregated parameter and a `{{ insert: param, ... }}`
  placeholder each name an element the catalog defines;
- that a withdrawn control or enhancement says where it went and carries
  none of what an active one carries, and that an active one carries its
  statement, discussion, assessment objective and methods;
- that a parameter is an assignment with a label or a selection with
  choices, never both;
- that a control's reference names a publication the catalog lists;
- that an SP 800-53A label belongs to the element it labels.

`tests/test_upstream.py` checks all but the last over NIST's catalog and
baselines of Release 5.2.0.
