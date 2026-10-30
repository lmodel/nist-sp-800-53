## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/nist-sp-800-53.yaml` is the copy `lokf adapt` writes from the schema
# so that it can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the
# moves). The roots are the classes a knowledge concept may use as its
# `type`: the family, the control, the control enhancement and the baseline,
# the four elements that SP 800-53 and SP 800-53B give an identifier and that
# other documents cite. A statement, a parameter, an assessment objective or
# method and a reference belong to one control, so they stay inlined in it,
# and Sp80053Catalog is the document that holds them all. The recipes run the
# `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs another,
# such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root Sp80053Family --root Sp80053Control --root Sp80053ControlEnhancement --root Sp80053Baseline"

# Rewrite .lokf/nist-sp-800-53.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/nist-sp-800-53.yaml

# Fail when .lokf/nist-sp-800-53.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/nist-sp-800-53.yaml --check
