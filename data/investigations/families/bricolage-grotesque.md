# Investigation Report: Bricolage Grotesque

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bricolage Grotesque |
| Designer | Mathieu Triay |
| License | OFL |
| Date Added | 2023-06-15 |
| Repository URL | https://github.com/ateliertriay/bricolage |
| Commit Hash | `84745e5b96261ae5f8c6c856e262fe78d1d6efdd` |
| Branch | main |
| Config YAML | `sources/config.yaml` (in upstream) |
| Status | Complete |

## How URL Found

The repository URL `https://github.com/ateliertriay/bricolage` is recorded in the METADATA.pb `source {}` block and matches the copyright string in the font files. The METADATA.pb also includes a `minisite_url` of `https://ateliertriay.github.io/bricolage`, confirming the repo owner. The URL was set during the initial gftools-packager onboarding.

## How Commit Determined

The commit hash `84745e5b96261ae5f8c6c856e262fe78d1d6efdd` was directly recorded by gftools-packager in the Version 1.001 update:

- google/fonts commit `b9f6c7120`: "[gftools-packager] Bricolage Grotesque: Version 1.001;gftools[0.9.33.dev8+g029e19f] added"
  - Body: "taken from the upstream repo https://github.com/ateliertriay/bricolage at commit https://github.com/ateliertriay/bricolage/commit/84745e5b96261ae5f8c6c856e262fe78d1d6efdd"

This was the second version onboarded. The initial Version 1.000 was from commit `95ddb0da9087a5f49f4616faea519e9e27d80a99` (google/fonts commit `92f1a0b27`).

The same commit hash also appears in the fontc_crater targets list (google/fonts commit `19cdcec59`), providing independent confirmation.

## Config YAML Status

- `sources/config.yaml` exists in the upstream repository at the recorded commit
- It is correctly referenced in the METADATA.pb `config_yaml` field
- No override config.yaml exists in google/fonts

The config.yaml defines a variable font build with 3 axes (opsz, wdth, wght) from `BricolageGrotesque.glyphs` source, matching the font file `BricolageGrotesque[opsz,wdth,wght].ttf` in google/fonts.

## Verification

1. **Commit exists in upstream**: Confirmed. `84745e5b96261ae5f8c6c856e262fe78d1d6efdd` exists in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/ateliertriay/bricolage` (it is the only commit, likely a shallow clone)
2. **Commit message**: "Merge pull request #5 from emmamarichal/main" - this aligns with emmamarichal's involvement in Google Fonts onboarding
3. **File paths match**: METADATA.pb references `fonts/variable/BricolageGrotesque[opsz,wdth,wght].ttf` which exists at that commit
4. **Config YAML valid**: `sources/config.yaml` references `BricolageGrotesque.glyphs` and defines axes opsz, wdth, wght
5. **gftools-packager reference matches**: Commit hash in METADATA.pb exactly matches the gftools-packager commit message
6. **fontc_crater confirmation**: The same commit hash was independently referenced in fontc_crater targets

## Confidence Level

**HIGH** - The commit hash was recorded by gftools-packager during the Version 1.001 onboarding and independently confirmed by fontc_crater targets. The config.yaml, font files, and axes all match consistently. The merge PR #5 from emmamarichal aligns with the typical Google Fonts onboarding workflow.

## Open Questions

None. This family is fully documented.
