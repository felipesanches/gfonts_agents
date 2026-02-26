# Investigation Report: Cairo Play

## Source Data

| Field | Value |
|---|---|
| Family Name | Cairo Play |
| Designer | Mohamed Gaber, Accademia di Belle Arti di Urbino |
| License | OFL |
| Repository URL | https://github.com/Gue3bara/Cairo |
| Commit Hash | `73d16933c6a0f341c27a69e401da83dcb0d53114` |
| Branch | master |
| Config YAML | `sources/cairoplay.yaml` |
| Status | complete |

## How URL Found

The repository URL `https://github.com/Gue3bara/Cairo` is recorded in the METADATA.pb `source {}` block and is consistent with the copyright notice in the font metadata: "Copyright 2009 The Cairo Project Authors (https://github.com/Gue3bara/Cairo)". The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/Gue3bara/Cairo/`.

## How Commit Determined

The commit `73d16933c6a0f341c27a69e401da83dcb0d53114` is recorded in METADATA.pb. It was explicitly referenced in the gftools-packager commit `27c225737` (PR #5972), which states:

> Cairo Play Version 3.130;gftools[0.9.24] taken from the upstream repo https://github.com/Gue3bara/Cairo at commit https://github.com/Gue3bara/Cairo/commit/73d16933c6a0f341c27a69e401da83dcb0d53114.

The PR was authored by yanone. This commit corresponds to "Merge pull request #94 from yanone/master" in the upstream repo and is the HEAD of the master branch, confirming it was the latest upstream commit at the time of onboarding.

## Config YAML Status

The config file `sources/cairoplay.yaml` exists at the recorded commit in the upstream repo. It contains gftools-builder configuration for building the variable font `CairoPlay[slnt,wght].ttf` from `CairoPlay.glyphs` source.

## Verification

- **Commit exists in upstream repo**: Yes, verified
- **Config YAML exists at commit**: Yes, `sources/cairoplay.yaml` confirmed
- **Binary file path matches**: Yes, `fonts/CairoPlay/variable/CairoPlay[slnt,wght].ttf` is built to the output directory specified in the config
- **PR reference cross-verified**: PR #5972 explicitly cites the commit hash
- **gftools-packager commit message**: Matches the recorded commit hash

## Confidence Level

**High** - All data is consistent and cross-verified through the gftools-packager commit message, PR #5972, and the upstream repository.

## Open Questions

None. All source data is complete and verified.
