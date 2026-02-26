# B612 Mono

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Nicolas Chauveau, Thomas Paillot, Jonathan Favre-Lamarine, Jean-Luc Vinot
**METADATA.pb path**: `ofl/b612mono/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/polarsys/b612 |
| Commit | `48ac6ba67ecab8123e8e36d6aa05367db0c7b638` |
| Config YAML | override in google/fonts |
| Branch | -- |

## How the Repository URL Was Found

The repository URL `https://github.com/polarsys/b612` is documented in the METADATA.pb `source {}` block. It is also referenced in the copyright string: "Copyright 2012 The B612 Project Authors (https://github.com/polarsys/b612)".

Both B612 and B612 Mono share the same upstream repository. The B612 Mono fonts were onboarded in a separate commit (`bff0396e9`, 2019-03-13, "b612mono: v1.008 added") slightly before B612 itself (2019-03-18). The onboarding PR #1878 body states: "Taken from the upstream repo https://github.com/polarsys/b612 at commit https://github.com/polarsys/b612/commit/7b5a653a6ae2bb05479297fed05ddf8c212d5477".

## How the Commit Hash Was Identified

The situation is identical to B612. The METADATA.pb records commit `48ac6ba67ecab8123e8e36d6aa05367db0c7b638`, while the onboarding PR #1878 explicitly references commit `7b5a653a6ae2bb05479297fed05ddf8c212d5477`.

The B612 Mono fonts were actually added on 2019-03-13, which is *before* commit `48ac6ba` was created (2019-03-18). This means the fonts were definitively taken from commit `7b5a653` (2019-03-12) or earlier, since `48ac6ba` did not exist yet when B612 Mono was onboarded.

The 2 commits between `7b5a653` and `48ac6ba` only modified README.md (EPL version update and http-to-https link changes), so the font source files are identical at both commits.

The commit hash `48ac6ba` was added to METADATA.pb by a previous enrichment pass (commit `edbfb125a`, 2025-11-19, "sources info for b612mono: v1.008 (PR #1878)").

## How Config YAML Was Resolved

The upstream repository does not contain a `config.yaml` file. An override config.yaml exists at `/mnt/shared/google/fonts/ofl/b612mono/config.yaml` with the following content:

```yaml
buildVariable: false
sources:
  - sources/ufo/B612Mono-Bold.ufo
  - sources/ufo/B612Mono-BoldItalic.ufo
  - sources/ufo/B612Mono-Italic.ufo
  - sources/ufo/B612Mono-Regular.ufo
```

Since the override config.yaml exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2019-03-18 14:24:05 +0100
- Commit message: "Merge pull request #17 from sunpoet/master"
- Source files at commit: UFO sources for B612Mono-Bold, B612Mono-BoldItalic, B612Mono-Italic, B612Mono-Regular (all under `sources/ufo/`)

Note: The PR-referenced commit `7b5a653` also exists:
- Commit date: 2019-03-12 18:10:12 +0100
- Commit message: "Merge pull request #15 from intactile/master"

## Confidence

**Medium**: The repository URL and general source data are well-established. However, the METADATA.pb commit hash (`48ac6ba`) is technically incorrect for B612 Mono because that commit did not exist when B612 Mono was added to google/fonts on 2019-03-13. The correct onboarding commit, as stated in PR #1878, is `7b5a653a6ae2bb05479297fed05ddf8c212d5477`. The source files are identical between the two commits, so there is no practical impact, but the METADATA.pb is recording a commit that postdates the onboarding by 5 days. The commit should ideally be corrected to `7b5a653a6ae2bb05479297fed05ddf8c212d5477`.

## Open Questions

- The METADATA.pb commit hash `48ac6ba` should be corrected to `7b5a653a6ae2bb05479297fed05ddf8c212d5477` to match the actual onboarding commit referenced in PR #1878. This is especially important for B612 Mono since `48ac6ba` did not exist when B612 Mono was added.
- Same consideration applies to B612 (see B612 investigation report).
- The B612 upstream repo has been inactive since 2019-03-18.
