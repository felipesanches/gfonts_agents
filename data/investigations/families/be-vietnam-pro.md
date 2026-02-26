# Be Vietnam Pro - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Be Vietnam Pro |
| Repository URL | https://github.com/bettergui/BeVietnamPro |
| Commit Hash | 804e62d81abbbcdcce5686069c69b41b8c245192 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Category | SANS_SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/bettergui/BeVietnamPro` is documented in the METADATA.pb `source{}` block. It was first added in the merge commit `66f91f10f` (2024-04-03) by Simon Cozens ("Merge upstream.yaml into METADATA.pb"). It is also confirmed by the copyright field: "Copyright 2021 The Be Vietnam Pro Project Authors (https://github.com/bettergui/BeVietnamPro)" and by PR #3771.

## How the Commit Hash Was Determined

The commit hash `804e62d81abbbcdcce5686069c69b41b8c245192` was identified through PR #3771, which updated Be Vietnam Pro to Version 1.002. The PR body (by RosaWagner) states: "Be Vietnam Pro Version 1.002; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/bettergui/BeVietnamPro at commit https://github.com/bettergui/BeVietnamPro/commit/804e62d81abbbcdcce5686069c69b41b8c245192."

The google/fonts commit `1cfe4cb46` (2021-08-27) is the last commit that modified the .ttf files, and its message confirms the same commit hash. This was a gftools-packager update.

The commit hash was later added to METADATA.pb in the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list").

The upstream commit `804e62d` is: "fix(sources): Update winAscent in Master".

### Font version history in google/fonts:
1. `659c177cd` - Be Vietnam Pro: Version 1.000 added (#3456) - initial addition
2. `428bc97e0` - Be Vietnam Pro: updated branch in upstream.yaml
3. `1cfe4cb46` (2021-08-27) - Be Vietnam Pro: Version 1.002; ttfautohint (v1.8.3) added (#3771) - **last TTF modification**

## Config YAML Status

The upstream repository has `sources/config.yaml` at the recorded commit `804e62d`. Verified locally:

```yaml
sources:
  - BeVietnamPro.glyphs
  - BeVietnamPro-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Be Vietnam Pro
```

The `config_yaml: "sources/config.yaml"` field is present in the current METADATA.pb on google/fonts main branch. No override config.yaml is needed or present in the google/fonts family directory.

## Verification

- **Repository exists**: Yes, confirmed locally at `/mnt/shared/upstream_repos/fontc_crater_cache/bettergui/BeVietnamPro`
- **Commit hash exists**: Yes, verified: `804e62d fix(sources): Update winAscent in Master`
- **Config.yaml exists at recorded commit**: Yes, at `sources/config.yaml`
- **Source files at commit**: `sources/BeVietnamPro.glyphs`, `sources/BeVietnamPro-Italic.glyphs`, `sources/config.yaml`
- **PR confirmed**: PR #3771 by RosaWagner confirms the commit hash
- **Font is a large family**: 18 TTF files (9 weights x 2 styles: normal + italic)

## Confidence Level

**High** - The commit hash is confirmed by multiple sources: the gftools-packager commit message in google/fonts, PR #3771 body, and the fontc_crater targets list. The upstream commit exists and contains the expected source files and config.yaml. All metadata fields are complete.

## Open Questions

None. This family is fully documented with repository URL, commit hash, and config.yaml path all verified.
