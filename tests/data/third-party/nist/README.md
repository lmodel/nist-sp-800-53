# NIST OSCAL Test Fixtures

Official and example OSCAL documents used for schema validation.
Files were sourced from the [`usnistgov/oscal-content`](https://github.com/usnistgov/oscal-content) and copied here for pinned regression testing.

All files pass `linkml validate` against the project schema except where noted.

## Rev 5 — NIST SP 800-53 Revision 5 (OSCAL 1.1.3)

| File | Type | Just recipe |
|---|---|---|
| `NIST_SP-800-53_rev5_catalog.yaml` | Full catalog | `validate-oscal-catalog` |
| `NIST_SP-800-53_rev5_LOW-baseline_profile.yaml` | LOW baseline profile | `validate-oscal-profile` |
| `NIST_SP-800-53_rev5_MODERATE-baseline_profile.yaml` | MODERATE baseline profile | `validate-oscal-profile` |
| `NIST_SP-800-53_rev5_HIGH-baseline_profile.yaml` | HIGH baseline profile | `validate-oscal-profile` |
| `NIST_SP-800-53_rev5_PRIVACY-baseline_profile.yaml` | PRIVACY baseline profile | `validate-oscal-profile` |
| `NIST_SP-800-53_rev5_LOW-baseline-resolved-profile_catalog.yaml` | LOW resolved catalog | `validate-oscal-catalog`, `validate-oscal-top` |
| `NIST_SP-800-53_rev5_MODERATE-baseline-resolved-profile_catalog.yaml` | MODERATE resolved catalog | — |
| `NIST_SP-800-53_rev5_HIGH-baseline-resolved-profile_catalog.yaml` | HIGH resolved catalog | — |
| `NIST_SP-800-53_rev5_PRIVACY-baseline-resolved-profile_catalog.yaml` | PRIVACY resolved catalog | — |

## Rev 4 — NIST SP 800-53 Revision 4 (OSCAL 1.2.2)

Baseline profile documents validate against the schema. The Rev 4 full catalog and
resolved catalogs contain a `depends-on` parameter attribute (removed in Rev 5 OSCAL)
and are **not** included here.

| File | Type | Just recipe |
|---|---|---|
| `NIST_SP-800-53_rev4_LOW-baseline_profile.yaml` | LOW baseline profile | `validate-oscal-rev4-profiles` |
| `NIST_SP-800-53_rev4_MODERATE-baseline_profile.yaml` | MODERATE baseline profile | `validate-oscal-rev4-profiles` |
| `NIST_SP-800-53_rev4_HIGH-baseline_profile.yaml` | HIGH baseline profile | `validate-oscal-rev4-profiles` |

## OSCAL Examples (ISO/IEC 27002-based)

Small example documents from the `oscal-content` examples directory. Useful for fast unit-level validation and tutorial scenarios.

| File | OSCAL version | Type | Just recipe |
|---|---|---|---|
| `basic-catalog.yaml` | 1.1.3 | Sample catalog | `validate-basic-catalog-oscal` |
| `basic_catalog.yaml` | 1.2.2 | Sample catalog | `validate-oscal-examples` |
| `basic-profile.yaml` | 1.1.3 | Sample profile | `validate-oscal-examples` |
| `basic_profile.yaml` | 1.2.2 | Sample profile | `validate-oscal-examples` |
| `basic-profile-resolved.yaml` | 1.1.3 | Resolved profile catalog | `validate-oscal-examples` |
| `basic-resolved-profile_catalog.yaml` | 1.2.2 | Resolved profile catalog | `validate-oscal-examples` |

## Validation

Run all validations:

```bash
just validate-oscal-all
```

Run individual groups:

```bash
just validate-oscal-catalog        # Rev 5 LOW resolved catalog
just validate-oscal-profile        # Rev 5 four baseline profiles
just validate-oscal-top            # Rev 5 LOW catalog/profile via SP80053Document class
just validate-basic-catalog-oscal  # basic-catalog.yaml (OSCAL 1.1.3)
just validate-oscal-examples       # All OSCAL example files (OSCAL 1.1.3 + 1.2.2)
just validate-oscal-rev4-profiles  # Rev 4 LOW/MODERATE/HIGH profiles
```
