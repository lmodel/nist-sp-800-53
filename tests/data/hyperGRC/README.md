# hyperGRC Test Fixtures

OSCAL-aligned YAML fixtures derived from the
[hyperGRC agencyapp example](https://github.com/GovReady/hyperGRC/tree/master/example/agencyapp). Source data ([OpenControl](https://open-control.org/) format) converted to OSCAL-compatible structures used by this schema.

The source project is licensed under the GNU General Public License v3 — see `LICENSE.md`.

## Directory layout

```
hyperGRC/
├── LICENSE.md
├── README.md                          # this file
└── agencyapp/
    ├── controls-oscal.yaml            # ControlGroup — all components merged by family
    ├── nist-sp-800-53-rev4-catalog.yaml  # SP80053Document (catalog) — Rev 4 control catalog
    ├── fisma-low-impact-profile.yaml  # SP80053Document (profile) — FISMA Low Impact baseline
    └── components-oscal/
        ├── centos-fake.yaml           # ControlGroup — CentOS component
        ├── cisco-cloud-rtr-fake.yaml  # ControlGroup — Cisco Cloud Router component
        ├── cylance-fake.yaml          # ControlGroup — Cylance component
        ├── govready-fake.yaml         # ControlGroup — GovReady component
        ├── jenkins-fake.yaml          # ControlGroup — Jenkins component
        ├── keycloak-fake.yaml         # ControlGroup — Keycloak component
        ├── openldap-fake.yaml         # ControlGroup — OpenLDAP component
        └── soc-services-fake.yaml     # ControlGroup — SOC Services component
```

## File descriptions

### `agencyapp/controls-oscal.yaml`

All control implementations from all eight components, merged and grouped by NIST SP 800-53 family. Top-level class is `ControlGroup`. Use `just validate-hypergrc-agencyapp-controls` to validate.

15 families covered: AC, AU, CA, CM, CP, IA, IR, MA, MP, PL, PM, PS, SA, SC, SI.

### `agencyapp/nist-sp-800-53-rev4-catalog.yaml`

Full NIST SP 800-53 Revision 4 control catalog, converted from the agencyapp `standards/` directory. Top-level class is `SP80053Document` with a `catalog:` wrapper. Contains 18 families, 256 base controls, and 666 control enhancements. Use `just validate-hypergrc-agencyapp-catalog`
to validate.

### `agencyapp/fisma-low-impact-profile.yaml`

FISMA Low Impact baseline profile, converted from the agencyapp `certifications/` directory. Top-level class is `SP80053Document` with a `profile:` wrapper. References `nist-sp-800-53-rev4-catalog.yaml` and includes 120 selected control IDs under `include-controls[].with-ids`. Use `just validate-hypergrc-agencyapp-profile` to validate.

### `agencyapp/components-oscal/*.yaml`

One `ControlGroup` file per component, containing only the controls that component implements. Control enhancements are nested under a synthetic parent `Control` node. Use `just validate-hypergrc-agencyapp-components` to validate all eight files.

## Conversion mapping

| OpenControl field       | OSCAL / schema field                       |
|-------------------------|--------------------------------------------|
| `family`                | `ControlGroup.id` / `ControlGroup.title`   |
| `control_key` (base)    | `Control.id`, `Control.title`              |
| `control_key` (enh.)    | `ControlEnhancement.id`, `.title`          |
| `narrative[].text`      | `Part.prose` (name: `statement`)           |
| `implementation_status` | `Property` (name: `implementation-status`) |
| `security_control_type` | `Property` (name: `security-control-type`) |

Control IDs are normalised to lowercase OSCAL format: `AC-18 (5)` → `ac-18.5`.

## Validation

All fixtures are validated by `just validate-hypergrc-agencyapp` (runs all four recipes below):

```bash
just validate-hypergrc-agencyapp-controls
just validate-hypergrc-agencyapp-catalog
just validate-hypergrc-agencyapp-profile
just validate-hypergrc-agencyapp-components
```

These are included in `just validate-oscal-all`.

## Note on `class:` vs `_class:`

Files in this directory use `class:` as the YAML key (the OSCAL/JSON Schema alias). This is required by `linkml validate`, which validates against the generated JSON Schema. The Python `yaml_loader` (used in pytest) accepts the alias transparently.
