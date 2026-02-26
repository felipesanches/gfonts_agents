# Balsamiq Sans

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Michael Angeles
**METADATA.pb path**: `ofl/balsamiqsans/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/balsamiq/balsamiqsans |
| Commit | `009740f8b2c3915b1553182ec406aaddb1a12dc7` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` (METADATA.pb says "main", but upstream default branch is actually "master") |

## How the Repository URL Was Found
The repository URL is documented in the METADATA.pb `source {}` block and in the copyright string. The gftools-packager commit message (52964a87a, 2023-04-27) confirms: "taken from the upstream repo https://github.com/balsamiq/balsamiqsans".

## How the Commit Hash Was Identified
The gftools-packager commit message (52964a87a) has an empty commit URL: "at commit https://github.com/balsamiq/balsamiqsans/commit/." -- the hash was never recorded in the packager message. The commit hash `009740f8b2c3915b1553182ec406aaddb1a12dc7` currently in METADATA.pb was added via the fontc_crater targets batch (commit 19cdcec59, 2025-03-31). This commit (009740f) is the current HEAD of the upstream repo's master branch, dated 2024-12-17, which is well AFTER the fonts were onboarded (2023-04-27).

The fonts were actually taken from the pre-built release archive (archive_url: `https://github.com/balsamiq/balsamiqsans/releases/download/1.020/balsamiqsans-fonts.zip`). The release tag `1.020` points to commit `b1dca64c3ceeaa3c274f69fae5a6f508b9a4dcc4` (2023-04-20). The commits between `b1dca64` and `009740f` are only build script updates (`f8dc431` and `75273c4`) that do not affect the font sources or binaries.

For fontc_crater rebuild purposes, using HEAD (009740f) is appropriate since it has the latest build configuration. But strictly speaking, the original onboarding commit was the release tag at `b1dca64`.

## How Config YAML Was Resolved
`sources/config.yaml` exists at both the current HEAD (009740f) and the release tag commit (b1dca64). It was introduced in the Dalton Maag PR (#17). The config builds static TTFs and OTFs from two .glyphs sources.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2024-12-17 11:37:49 +0100
- Commit message: "Merge pull request #23 from balsamiq/update_build_script"
- Source files at commit: `sources/config.yaml`, `sources/glyphs/BalsamiqSans-Roman.glyphs`, `sources/glyphs/BalsamiqSans-Italic.glyphs`
- TTFs last updated in google/fonts: 2023-04-27 (commit 52964a87a, PR #6231 by Marc Foley)
- No override config.yaml in google/fonts family directory
- Branch discrepancy: METADATA.pb says "main" but upstream uses "master"

## Confidence
**Medium-High**: The repository URL is confirmed. The commit hash is the fontc_crater target (current HEAD), not the original onboarding commit. The actual fonts came from a release archive corresponding to tag `1.020` (commit b1dca64). The config.yaml is present and valid. The branch field in METADATA.pb says "main" but should be "master".

## Open Questions
- The branch field in METADATA.pb says "main" but the upstream repo's default branch is "master". This should be corrected to "master".
- The commit 009740f is newer than the onboarding date. For strict traceability, the commit should arguably be `b1dca64c3ceeaa3c274f69fae5a6f508b9a4dcc4` (release tag 1.020). However, since the only changes between the two are build script updates, the current value works for fontc_crater.
