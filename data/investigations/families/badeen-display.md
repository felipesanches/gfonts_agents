# Badeen Display

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Hani Alasadi
**METADATA.pb path**: `ofl/badeendisplay/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/haniadnansd/Badeen-Display |
| Commit | `c1370b602b4a9819c4ddce4af17962a42edb8bc3` |
| Config YAML | `source/config.yaml` |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/haniadnansd/Badeen-Display` is documented in the METADATA.pb `source` block, in the font copyright string, and in the google/fonts issue #7814 (which requested the font's addition). The repository owner `haniadnansd` is Hani Alasadi, the designer.

## How the Commit Hash Was Identified

The commit `c1370b602b4a9819c4ddce4af17962a42edb8bc3` is referenced in the google/fonts commit `c31eae5` (by Yanone, 2024-11-20): "Taken from the upstream repo https://github.com/haniadnansd/Badeen-Display at commit c1370b602b4a9819c4ddce4af17962a42edb8bc3. Resolves #7814."

Cross-verification:
- The upstream commit is dated 2024-11-14 21:51:58 +0400 (message: "Update DESCRIPTION.en_us.html").
- The google/fonts commit is dated 2024-11-20 15:36:38 +0100, 6 days after the upstream commit.
- The 6-day gap is consistent with an onboarding review workflow.
- The commit is HEAD of the upstream main branch -- no subsequent commits exist.
- The font was added to resolve issue #7814, which was a standard "Add font" request by the designer.
- Prior upstream commits show the repository was prepared for onboarding: PR #7 from yanone/main created the DESCRIPTION.en_us.html, then c1370b6 updated it.

## How Config YAML Was Resolved

The upstream repo contains `source/config.yaml` (note: `source` singular, not `sources`) at the referenced commit with the following content:

```yaml
sources:
    - BadeenDisplay.glyphs
```

This is a valid (minimal) gftools-builder configuration. The METADATA.pb correctly records the path as `source/config.yaml`. No override config.yaml exists in the google/fonts family directory.

Note: The repo has both `source/` and `Source/` directories (case-sensitive), with the config.yaml in the lowercase `source/` directory. Both directories contain `BadeenDisplay.glyphs`.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-11-14 21:51:58 +0400
- Commit message: "Update DESCRIPTION.en_us.html"
- Source files at commit: `source/BadeenDisplay.glyphs`, `source/config.yaml`, `Source/BadeenDisplay.glyphs`, `fonts/ttf/BadeenDisplay-Regular.ttf`
- Commit is HEAD of upstream main branch: Yes (no newer commits)
- Resolves issue: google/fonts#7814

## Confidence

**High**: The commit hash is consistently referenced in the google/fonts commit body and METADATA.pb. The commit is the latest in the upstream repo. The config.yaml path is verified. The onboarding was done by Yanone, a well-known font engineer who regularly handles Google Fonts onboarding.

## Open Questions

None. The dual `source/` and `Source/` directories in the upstream repo are slightly unusual (likely a case-sensitivity issue on the designer's end), but the config.yaml correctly points to the lowercase `source/` directory which contains the actual build configuration.
