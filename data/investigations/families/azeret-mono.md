# Azeret Mono

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Displaay, Martin Vacha
**METADATA.pb path**: `ofl/azeretmono/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/displaay/Azeret |
| Commit | `3d45a6c3e094f08bfc70551b525bd2037cac51ba` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/displaay/Azeret` is documented in the METADATA.pb `source {}` block. It is also referenced in the copyright string of the font files: "Copyright 2021 The Azeret Project Authors (https://github.com/displaay/azeret)".

The original onboarding PR #3475 (commit `c44cf77ca`, 2021-06-09) explicitly states: "Azeret Version 1.002 taken from the upstream repo https://github.com/displaay/Azeret at commit https://github.com/displaay/Azeret/commit/3d45a6c3e094f08bfc70551b525bd2037cac51ba."

The font was initially added as `ofl/azeret`, then renamed to `ofl/azeretmono` in PR #3739 (2021-08-16, "ofl/azeret -> ofl/azeretmono"). The font binaries were last modified in the deploy commit `76adaf1d2` on 2021-11-01.

## How the Commit Hash Was Identified

The commit hash `3d45a6c3e094f08bfc70551b525bd2037cac51ba` was explicitly documented in the original onboarding PR #3475 body: "taken from the upstream repo https://github.com/displaay/Azeret at commit https://github.com/displaay/Azeret/commit/3d45a6c3e094f08bfc70551b525bd2037cac51ba."

This commit was verified in the local upstream cache at `/mnt/shared/upstream_repos/fontc_crater_cache/displaay/Azeret`. The commit exists and is dated 2021-06-04, with the message "Merge pull request #3 from RosaWagner/main".

## How Config YAML Was Resolved

The config.yaml is located at `sources/config.yaml` in the upstream repository. This was verified at the recorded commit hash. The file contains:

```yaml
sources:
  - AzeretMono.glyphs
  - AzeretMono-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Azeret Mono
```

No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2021-06-04 21:41:25 +0200
- Commit message: "Merge pull request #3 from RosaWagner/main"
- Source files at commit: `sources/AzeretMono.glyphs`, `sources/AzeretMono-Italic.glyphs`, `sources/config.yaml`

## Confidence

**High**: The commit hash is explicitly documented in the onboarding PR body, exists in the upstream repository, and was created just 5 days before the fonts were added to Google Fonts. The repository URL matches the copyright string. The config.yaml is present at the recorded commit. All data is fully verified and consistent.

## Open Questions

None
