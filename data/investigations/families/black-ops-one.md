# Black Ops One

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: James Grieshaber, Eben Sorkin
**METADATA.pb path**: `ofl/blackopsone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/SorkinType/Black-Ops |
| Commit | `c955bed3517ad3d8606a8b0105d27538309fb70d` |
| Config YAML | Override config.yaml in google/fonts |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/SorkinType/Black-Ops` was already present in the METADATA.pb `source { repository_url }` field. It is also confirmed by the copyright string in the font file ("Copyright 2022 The PinyonScript Project Authors (https://github.com/SorkinType/Black-Ops)") and by the gftools-packager commit `d50a0d29b` in google/fonts (PR #4995), which explicitly states: "taken from the upstream repo https://github.com/SorkinType/Black-Ops at commit c955bed...".

## How the Commit Hash Was Identified

The commit hash `c955bed3517ad3d8606a8b0105d27538309fb70d` is recorded in METADATA.pb and matches the gftools-packager commit message in PR #4995 (authored by Emma Marichal, 2022-07-28). The PR body states: "Black Ops One Version 1.004; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/SorkinType/Black-Ops at commit https://github.com/SorkinType/Black-Ops/commit/c955bed3517ad3d8606a8b0105d27538309fb70d."

This commit exists in the upstream repo and corresponds to "Merge pull request #1 from emmamarichal/main". The font was originally added to google/fonts much earlier (2011, commit `90abd17b4`), with an intermediate update in PR #860 (v1.003), but the current binary was taken from this v1.004 update.

## How Config YAML Was Resolved

There is no `config.yaml` in the upstream repository. An override `config.yaml` exists in the google/fonts family directory (`ofl/blackopsone/config.yaml`) with the following content:

```yaml
sources:
  - sources/BlackOpsOne.glyphs
familyName: Black Ops One
buildStatic: true
buildOTF: false
```

This override references `sources/BlackOpsOne.glyphs`, which exists in the upstream repo at the recorded commit. Since the override config.yaml is in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: Merge commit for PR #1 from emmamarichal/main
- Commit message: "Merge pull request #1 from emmamarichal/main"
- Source files at commit: `sources/BlackOpsOne.glyphs`
- Override config.yaml in google/fonts: Yes
- Binary file in METADATA.pb source block: `fonts/ttf/BlackOpsOne-Regular.ttf`

## Confidence

**High**: The repository URL and commit hash are consistently referenced across the METADATA.pb, the gftools-packager commit message, and PR #4995. The commit exists in the upstream repo. The override config.yaml in google/fonts correctly references the source file present at that commit. All data is well-corroborated.

## Open Questions

None. All data is verified and consistent.
