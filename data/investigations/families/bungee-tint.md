# Bungee Tint

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: David Jonathan Ross
**METADATA.pb path**: `ofl/bungeetint/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/djrrb/Bungee |
| Commit | `0ab742e49fc7725cd86089834d6460c489b9b2a6` |
| Config YAML | -- |
| Branch | master |
| Archive URL | https://github.com/djrrb/Bungee/releases/download/v2.001/Bungee-fonts.zip |

## How the Repository URL Was Found

The repository URL `https://github.com/djrrb/Bungee` is already documented in the METADATA.pb `source { }` block. It is confirmed by multiple sources:

- The initial onboarding commit `fff14184d` in google/fonts states: "Taken from the upstream repo https://github.com/djrrb/Bungee"
- PR #7952 body repeats the same reference
- The font copyright line in METADATA.pb reads: "Copyright 2023 The Bungee Project Authors (https://github.com/djrrb/Bungee)"

The upstream repo at `upstream_repos/fontc_crater_cache/djrrb/Bungee` confirms the remote URL matches.

## How the Commit Hash Was Identified

The commit hash `0ab742e49fc7725cd86089834d6460c489b9b2a6` is explicitly stated in both:

1. The onboarding commit message (`fff14184d`): "Taken from the upstream repo https://github.com/djrrb/Bungee at commit https://github.com/djrrb/Bungee/commit/0ab742e49fc7725cd86089834d6460c489b9b2a6."
2. The PR #7952 body, which repeats the same message.

This commit is the HEAD of the `master` branch at the time of onboarding. It is a merge commit ("Merge pull request #121 from vv-monsalve/QA-Bungee") dated 2024-07-17, which is 2 days before the google/fonts merge on 2024-07-19.

**Important context**: The actual font binary was taken from the v2.001 release archive (published 2024-06-29), not built from source at this commit. The v2.001 tag points to an earlier commit `dbf8a1c4` (2024-06-29). The commits between the tag and `0ab742e4` are all article/documentation additions (images, article templates) with no changes to font sources or binaries. The commit hash in METADATA.pb therefore references the overall repo state at onboarding time, while the `archive_url` points to the actual release containing the binary.

## How Config YAML Was Resolved

No `config.yaml` or `config.yml` exists in the upstream repository. No override `config.yaml` exists in `google/fonts/ofl/bungeetint/`.

This is expected: Bungee Tint is part of the broader Bungee family, which uses a custom build process (`build.sh`) involving:
- Custom Python scripts (`assembleSources.py`, `assembleColorSources.py`, etc.)
- `fontmake` for individual UFO compilation
- `maximum_color` for SVG table insertion in COLRv1 fonts
- `gftools fix-nonhinting` for post-processing

This is not a standard gftools-builder workflow. The font was onboarded from a pre-built release archive (`Bungee-fonts.zip` from the v2.001 release), with the binary path `Bungee_Color/BungeeTint-Regular.ttf` mapped to the google/fonts filename `BungeeTint-Regular.ttf`.

No config.yaml is needed since the source block uses `archive_url` + `files` mapping to pull a pre-built binary.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-07-17 22:24:46 -0400
- Commit message: "Merge pull request #121 from vv-monsalve/QA-Bungee"
- Commit author: David Jonathan Ross
- Source files at commit: `sources/1-drawing/Bungee-Regular.ufo`, `sources/1-drawing/Bungee_Rotated-Regular.ufo`, `sources/1-drawing/Bungee-Shade-Exceptions.ufo` (plus experimental UFOs)
- Build script: `build.sh` (custom fontmake-based pipeline, not gftools-builder)
- Release: v2.001 (tag at `dbf8a1c4`, published 2024-06-29) contains `Bungee-fonts.zip`

### Timeline

| Date | Event |
|------|-------|
| 2024-06-29 | v2.001 release published on GitHub (tag `dbf8a1c4`) |
| 2024-07-17 | Commit `0ab742e4` (HEAD of master, article/QA additions) |
| 2024-07-18 | Onboarding commit `fff14184d` by Viviana Monsalve |
| 2024-07-19 | PR #7952 merged into google/fonts |

### Other Bungee Families in google/fonts

The upstream repo `djrrb/Bungee` is the source for multiple font families: Bungee, Bungee Color, Bungee Hairline, Bungee Inline, Bungee Outline, Bungee Shade, Bungee Spice, and Bungee Tint.

## Confidence

**HIGH**: The commit hash and repository URL are explicitly documented in the onboarding commit message and PR body, both written by the onboarder (Viviana Monsalve). The commit exists in the upstream repo and its date (2024-07-17) is consistent with the google/fonts merge date (2024-07-19). The source block is already fully populated with repository_url, commit, archive_url, branch, and file mappings. No config.yaml is needed for this archive-based onboarding.
