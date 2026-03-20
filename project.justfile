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
		tests/data/nist/NIST_SP-800-53_rev5_LOW-baseline-resolved-profile_catalog.yaml

# Validate all NIST profile documents with the profile schema.
validate-oscal-profile:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/nist/NIST_SP-800-53_rev5_LOW-baseline_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/nist/NIST_SP-800-53_rev5_MODERATE-baseline_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/nist/NIST_SP-800-53_rev5_HIGH-baseline_profile.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		tests/data/nist/NIST_SP-800-53_rev5_PRIVACY-baseline_profile.yaml

# Validate with top-level schema using explicit target class.
validate-oscal-top:
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C SP80053Document \
		tests/data/nist/NIST_SP-800-53_rev5_LOW-baseline-resolved-profile_catalog.yaml
	uv run linkml validate \
		-s src/nist_sp_800_53/schema/nist_sp_800_53.yaml \
		-C SP80053Document \
		tests/data/nist/NIST_SP-800-53_rev5_LOW-baseline_profile.yaml
