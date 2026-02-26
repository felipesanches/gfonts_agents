# Atkinson Hyperlegible Mono

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Braille Institute, Applied Design Works, Elliott Scott, Megan Eiswerth, Letters From Sweden
**METADATA.pb path**: `ofl/atkinsonhyperlegiblemono/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/atkinson-hyperlegible-next-mono |
| Commit | `154d50362016cc3e873eb21d242cd0772384c8f9` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/atkinson-hyperlegible-next-mono` was present in METADATA.pb from the original onboarding commit (`a4ccc36e5`, "Atkinson Hyperlegible Mono: Version 2.001 added", 2024-11-20). The commit body explicitly states: "Taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible-next-mono". The URL is also embedded in the font's copyright string in METADATA.pb.

## How the Commit Hash Was Identified

The commit hash `154d50362016cc3e873eb21d242cd0772384c8f9` was present in METADATA.pb from the original onboarding commit. The google/fonts commit body explicitly states: "at commit https://github.com/googlefonts/atkinson-hyperlegible-next-mono/commit/154d50362016cc3e873eb21d242cd0772384c8f9."

This was also confirmed in PR #8519 body, which contains the same reference.

## How Config YAML Was Resolved

The `config_yaml: "sources/config.yaml"` field was added in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31). The config.yaml exists in the upstream repository at the referenced commit and contains:

- Two .glyphs source files: `AtkinsonHyperlegibleMono.glyphs` and `AtkinsonHyperlegibleMono-Italic.glyphs`
- Family name: "Atkinson Hyperlegible Mono"
- `cleanUp: true`
- Full STAT table configuration for weight and italic axes

There is no override config.yaml in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-11-20 14:50:37 +0100
- Commit message: "last fixes"
- Source files at commit: `sources/AtkinsonHyperlegibleMono.glyphs`, `sources/AtkinsonHyperlegibleMono-Italic.glyphs`, `sources/config.yaml`, `.github/workflows/build.yaml`

## Confidence

**High**: The commit hash is explicitly referenced in both the google/fonts onboarding commit body and PR #8519. The commit date (2024-11-20 14:50:37) is just minutes before the google/fonts onboarding commit (2024-11-20 15:04:40), confirming this is the exact commit used. The repository is under the `googlefonts` organization and the config.yaml exists at the commit.

## Open Questions

None
