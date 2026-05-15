## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Fix Python reserved keyword 'class' generated as an attribute name due to alias.
# This is needed because gen-python emits 'class:' and 'self.class' verbatim
# when the slot alias is 'class', which is a Python keyword.
fix-python-keywords:
	sed -i \
		-e 's/\bclass: Optional\b/_class: Optional/g' \
		-e 's/self\.class\b/self._class/g' \
		-e 's/NIST_SP_800_53\.class\b/NIST_SP_800_53["class"]/g' \
		{{pymodel}}/{{schema_name}}.py

validate-oscal-catalog:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/NIST_SP-800-53_rev5_LOW-baseline-resolved-profile_catalog.yaml

validate-basic-catalog-oscal:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/basic-catalog.yaml

# Validate all NIST profile documents with the profile schema.
validate-oscal-profile:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/NIST_SP-800-53_rev5_LOW-baseline_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/NIST_SP-800-53_rev5_MODERATE-baseline_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/NIST_SP-800-53_rev5_HIGH-baseline_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/NIST_SP-800-53_rev5_PRIVACY-baseline_profile.yaml

# Validate OSCAL example catalog and profile documents (OSCAL 1.1.3 / 1.2.2).
validate-oscal-examples:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/basic_catalog.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/basic-profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/basic_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/basic-profile-resolved.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/basic-resolved-profile_catalog.yaml

# Validate all three NIST CPRT (Cybersecurity and Privacy Reference Tool) JSON exports.
validate-cprt:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/cprt/cprt_SP_800_53_5_2_0_05-15-2026.json
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/cprt/cprt_SP_800_53_A_5_2_0_05-15-2026.json
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/cprt/cprt_SP_800_53_B_5_2_0_05-15-2026.json

# Validate NIST SP 800-53 Rev 4 baseline profile documents.
validate-oscal-rev4-profiles:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/NIST_SP-800-53_rev4_LOW-baseline_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/NIST_SP-800-53_rev4_MODERATE-baseline_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/third-party/nist/NIST_SP-800-53_rev4_HIGH-baseline_profile.yaml

# ── hyperGRC agencyapp fixtures ───────────────────────────────────────────────
# Source: https://github.com/GovReady/hyperGRC/tree/master/example/agencyapp
# OSCAL output files are pre-generated and stored under tests/data/third-party/hyperGRC/agencyapp/.

# Validate the combined agencyapp controls (all components merged by family).
validate-hypergrc-agencyapp-controls:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/controls-oscal.yaml

# Validate the NIST SP 800-53 Rev 4 catalog converted from agencyapp standards/.
validate-hypergrc-agencyapp-catalog:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C SP80053Document \
		tests/data/third-party/hyperGRC/agencyapp/nist-sp-800-53-rev4-catalog.yaml

# Validate the FISMA Low Impact profile converted from agencyapp certifications/.
validate-hypergrc-agencyapp-profile:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C SP80053Document \
		tests/data/third-party/hyperGRC/agencyapp/fisma-low-impact-profile.yaml

# Validate all eight per-component ControlGroup files under components-oscal/.
validate-hypergrc-agencyapp-components:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/components-oscal/centos-fake.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/components-oscal/cisco-cloud-rtr-fake.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/components-oscal/cylance-fake.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/components-oscal/govready-fake.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/components-oscal/jenkins-fake.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/components-oscal/keycloak-fake.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/components-oscal/openldap-fake.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C ControlGroup \
		tests/data/third-party/hyperGRC/agencyapp/components-oscal/soc-services-fake.yaml

# Validate all hyperGRC agencyapp OSCAL output files.
validate-hypergrc-agencyapp: \
	validate-hypergrc-agencyapp-controls \
	validate-hypergrc-agencyapp-catalog \
	validate-hypergrc-agencyapp-profile \
	validate-hypergrc-agencyapp-components

# Apply SSSOM mapping files to the schema YAML (idempotent).
overlay-sssom:
	uv run python3 scripts/overlay_sssom.py

# Dry-run: report what overlay-sssom would change without writing files.
overlay-sssom-dry-run:
	uv run python3 scripts/overlay_sssom.py --dry-run --verbose

# Validate all OSCAL documents (catalogs, profiles, basic catalog, hyperGRC examples, and CPRT).
validate-oscal-all: \
	validate-oscal-catalog \
	validate-oscal-profile \
	validate-oscal-top \
	validate-basic-catalog-oscal \
	validate-oscal-examples \
	validate-oscal-rev4-profiles \
	validate-hypergrc-agencyapp \
	validate-cprt

# Validate with top-level schema using explicit target class.
validate-oscal-top:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C SP80053Document \
		tests/data/third-party/nist/NIST_SP-800-53_rev5_LOW-baseline-resolved-profile_catalog.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C SP80053Document \
		tests/data/third-party/nist/NIST_SP-800-53_rev5_LOW-baseline_profile.yaml
