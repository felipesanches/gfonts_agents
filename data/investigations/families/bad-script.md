# Bad Script

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Gaslight
**METADATA.pb path**: `ofl/badscript/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/alexeiva/badscript |
| Commit | `dca2962433a2b5817f1e716d6731a743440fbd79` |
| Config YAML | `sources/config.yaml` |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/alexeiva/badscript` is documented in the METADATA.pb `source` block and in the font copyright string. The google/fonts commit body also explicitly references this repo. The repository owner `alexeiva` is Alexei Vanyashin, the original designer (Gaslight is the design studio name).

## How the Commit Hash Was Identified

The commit `dca2962433a2b5817f1e716d6731a743440fbd79` is referenced in the google/fonts commit `0827c33` (by Emma Marichal, 2024-11-08): "Taken from the upstream repo https://github.com/alexeiva/badscript at commit dca2962433a2b5817f1e716d6731a743440fbd79."

Cross-verification:
- The upstream commit is dated 2024-11-08 18:10:45 +0500 (a merge of PR #6 from emmamarichal/master).
- The google/fonts commit is dated 2024-11-08 14:13:45 +0100 (same day, adjusting for timezones this is 18:13 +0500 -- just 3 minutes after the upstream merge).
- The upstream PR #6 was by Emma Marichal herself, with the message "So sorry, I totally forgot to push the fonts... Here they are!" -- this was exporting the rebuilt fonts after fixing outline issues in PR #5.
- The previous upstream PR #5 (also by Emma Marichal) fixed outline issues and updated v-metrics.
- This commit was pushed directly to google/fonts (not via a PR), which is consistent with the tight timeline.
- The commit is HEAD of the upstream master branch -- no newer commits exist.

This represents a Version 2.000 update of Bad Script, originally added to Google Fonts in 2011.

## How Config YAML Was Resolved

The upstream repo contains `sources/config.yaml` at the referenced commit with the following content:

```yaml
sources:
  - BadScript.glyphs
familyName: Bad Script
cleanUp: true
```

This is a valid gftools-builder configuration. The METADATA.pb correctly records the path as `sources/config.yaml`. No override config.yaml exists in the google/fonts family directory.

Note: The upstream repo uses `master` as its default branch (not `main`), and this is correctly reflected in the METADATA.pb `branch` field.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-11-08 18:10:45 +0500
- Commit message: "Merge pull request #6 from emmamarichal/master"
- Commit author: Alexei Vanyashin (merge commit)
- Source files at commit: `sources/BadScript.glyphs`, `sources/config.yaml`, `fonts/ttf/BadScript-Regular.ttf`
- Commit is HEAD of upstream master branch: Yes (no newer commits)
- Default branch: master (not main)

## Confidence

**High**: The commit hash is consistently referenced in the google/fonts commit body and METADATA.pb. The extremely tight timing between upstream merge and google/fonts commit (3 minutes) confirms the hash was used immediately. Emma Marichal authored both the upstream PR and the google/fonts commit. The config.yaml path is verified and the commit is the latest.

## Open Questions

None. The font was originally added in 2011 and received a major update (Version 2.000) in November 2024 with outline fixes and updated metrics by Emma Marichal.
