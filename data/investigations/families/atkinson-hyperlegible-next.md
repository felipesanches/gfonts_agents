# Atkinson Hyperlegible Next

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Braille Institute, Applied Design Works, Elliott Scott, Megan Eiswerth, Letters From Sweden
**METADATA.pb path**: `ofl/atkinsonhyperlegiblenext/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/atkinson-hyperlegible-next |
| Commit | `7925f50f649b3813257faf2f4c0b381011f434f1` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/atkinson-hyperlegible-next` was present in METADATA.pb from the original onboarding commit (`66eef7072`, "Atkinson Hyperlegible Next: Version 2.001 added", 2025-01-07). The commit body states: "Taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible-next". The URL is also embedded in the font's copyright string in METADATA.pb.

## How the Commit Hash Was Identified

**Important note on commit hash discrepancy**: The original onboarding commit (`66eef7072`) in google/fonts referenced upstream commit `5d633f80fc654ef5fffa7cfc257528685158dcef`. However, the current METADATA.pb contains commit `7925f50f649b3813257faf2f4c0b381011f434f1` (dated 2025-02-21, message: "Fix Cairo in CI"). This change was made in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which ported data from the fontc_crater targets.json file.

The fontc_crater targets list uses commit `7925f50f` (which is newer than the original onboarding commit `5d633f80`). This means the METADATA.pb now references a commit that is more recent than the one actually used to build the fonts in google/fonts.

The original onboarding commit `5d633f80fc654ef5fffa7cfc257528685158dcef` could not be verified in the local cache because the upstream repo is a shallow clone containing only the latest commit.

PR #8813 body confirms the original reference: "Taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible-next at commit https://github.com/googlefonts/atkinson-hyperlegible-next/commit/5d633f80fc654ef5fffa7cfc257528685158dcef."

## How Config YAML Was Resolved

The `config_yaml: "sources/config.yaml"` field was added in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list"). The config.yaml exists in the upstream repository at the referenced commit (7925f50f) and contains:

- Two .glyphs source files: `AtkinsonHyperlegibleNext.glyphs` and `AtkinsonHyperlegibleNext-Italic.glyphs`
- Family name: "Atkinson Hyperlegible Next"
- `cleanUp: true`
- Full STAT table configuration for weight and italic axes

There is no override config.yaml in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (7925f50f, the current METADATA.pb value)
- Commit date: 2025-02-21 16:04:57 +0000
- Commit message: "Fix Cairo in CI"
- Source files at commit: `sources/AtkinsonHyperlegibleNext.glyphs`, `sources/AtkinsonHyperlegibleNext-Italic.glyphs`, `sources/config.yaml`, `.github/workflows/build.yaml`

## Confidence

**Medium**: The repository URL and config.yaml path are correct and verified. However, there is a commit hash discrepancy: the METADATA.pb currently records commit `7925f50f` (2025-02-21, "Fix Cairo in CI") from the fontc_crater targets list, while the original onboarding PR #8813 referenced commit `5d633f80` (which could not be verified locally due to the shallow clone). The commit `7925f50f` is newer than the font onboarding date (2025-01-07) and may include changes beyond what was actually used to build the fonts. The original commit `5d633f80` should be restored as the correct onboarding commit, or the discrepancy should be investigated further.

## Open Questions

1. Should the commit hash in METADATA.pb be reverted to the original onboarding commit `5d633f80fc654ef5fffa7cfc257528685158dcef` as referenced in PR #8813?
2. Were the font binaries rebuilt from the newer commit `7925f50f`, or does the METADATA.pb now incorrectly reference a newer commit than what was actually used?
3. The fontc_crater targets list may use a different commit for its own CI purposes -- should METADATA.pb track the original onboarding commit or the fontc_crater reference?
