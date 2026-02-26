# Cactus Classical Serif - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cactus Classical Serif |
| Designer | Henry Chan, Tian Haidong, Moonlit Owen |
| License | OFL |
| Date Added | 2024-05-14 |
| Repository URL | https://github.com/MoonlitOwen/CactusSerif |
| Commit Hash | a267f9f32087eb9e6a9203c734cb952a64bc05be |
| Config YAML | source/config.yaml |
| Status | complete |

## How URL Was Found

The repository URL has changed over time:
- **Original (v1.000)**: `https://github.com/aaronbell/CactusSerif` - This was the URL used for the initial onboarding in commit `344f7a69b` (2024-05-14) by Aaron Bell.
- **Updated (v1.005)**: `https://github.com/MoonlitOwen/CactusSerif` - The repo moved when v1.005 was submitted via PR #9545. Aaron Bell noted in the PR: "Font is now building directly in the upstream repository (https://github.com/MoonlitOwen/CactusSerif)".

The METADATA.pb was updated to point to the MoonlitOwen repo in commit `bdb9dcdf6` (2025-11-28).

## How Commit Was Determined

The commit hash `a267f9f32087eb9e6a9203c734cb952a64bc05be` was determined through investigation of PR #9545 and the upstream repo history:

- The original v1.000 onboarding (commit `344f7a69b`) referenced `aaronbell/CactusSerif` at commit `eb5a6eaf`.
- The v1.005 update was submitted by Aaron Bell via PR #9545 in June 2025.
- In the MoonlitOwen/CactusSerif repo, commit `a267f9f3` (2025-06-09, "Upload built fonts") is the commit where the v1.005 fonts were built. It was authored by NightFurySL2001 (who was acknowledged in the PR for assistance).
- Aaron Bell's google/fonts commit `a05de1830` (2025-06-09) imported the font from this exact build.

The commit `a267f9f3` is the second-to-last commit in the repo; two more commits follow (readme update and another font build).

## Config YAML Status

**config.yaml exists** at `source/config.yaml` in the upstream repository at the recorded commit. It is a valid gftools-builder configuration that builds from `temp/CactusClassicalSerif-Regular.ufo`.

Key settings from the config:
- Source: `temp/CactusClassicalSerif-Regular.ufo`
- Family name: "Cactus Classical Serif"
- Version: 1.005
- Overlap removal enabled, autohinting disabled
- No webfont or small cap builds

## Verification

- **Repository URL**: Valid. The MoonlitOwen/CactusSerif repository exists and is accessible.
- **Commit Hash**: Verified. The hash `a267f9f32087eb9e6a9203c734cb952a64bc05be` exists in the repo.
- **Config YAML**: Verified. `source/config.yaml` exists at the recorded commit with valid gftools-builder configuration.
- **Font Files**: The upstream repo has `fonts/ttf/CactusClassicalSerif-Regular.ttf` matching google/fonts.
- **PR Cross-reference**: PR #9545 confirms the migration from aaronbell to MoonlitOwen repository and the v1.005 update.

## Confidence Level

**HIGH** - All data is well-documented. The repository URL, commit hash, and config.yaml path are all verified. The migration from aaronbell to MoonlitOwen is clearly documented in PR #9545.

## Open Questions

None. This family is fully documented and verified.
