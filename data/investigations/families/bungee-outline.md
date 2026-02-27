# Investigation Report: Bungee Outline

## Source Data

| Field            | Value |
|------------------|-------|
| Family Name      | Bungee Outline |
| Designer         | David Jonathan Ross |
| Repository URL   | https://github.com/djrrb/Bungee |
| Commit Hash      | `eb03cf69adab5094f6b84e95357789cdf3bfeb99` |
| Branch           | master |
| Config YAML      | Override `config.yaml` in google/fonts family directory |
| Archive URL      | https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip |
| Source File      | `Bungee_Basic/BungeeOutline-Regular.ttf` (from archive) |
| Date Added       | 2016-06-20 |
| License          | OFL |
| Status           | **complete** |
| Confidence       | **HIGH** |

## How Repository URL Was Found

The repository URL `https://github.com/djrrb/Bungee` was already present in the METADATA.pb source block at `ofl/bungeeoutline/METADATA.pb`. It is also referenced in the font copyright string: "Copyright 2023 The Bungee Project Authors (https://github.com/djrrb/Bungee)".

The URL was verified to return HTTP 200. The upstream repository at `djrrb/Bungee` is cached locally at `upstream_repos/fontc_crater_cache/djrrb/Bungee/`.

This is a monorepo hosting multiple Bungee variants: Bungee, Bungee Color, Bungee Hairline, Bungee Inline, Bungee Outline, Bungee Shade, Bungee Spice, and Bungee Tint.

## How Commit Hash Was Identified

The commit hash `eb03cf69adab5094f6b84e95357789cdf3bfeb99` was already recorded in the METADATA.pb source block. It was verified through multiple sources:

1. **google/fonts commit message**: Commit `d3d22093c` ("Bungee Outline: Version 2.000 added") by Viviana Monsalve (2024-05-30) explicitly states: "Taken from the upstream repo https://github.com/djrrb/Bungee at commit https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99."

2. **PR #7796** (`google/fonts`): "Bungee Outline: Version 2.000 added" opened by vv-monsalve, merged by emmamarichal on 2024-05-31. PR body confirms the same commit reference.

3. **Upstream tag verification**: Tag `v2.000` in the upstream repo points directly to commit `eb03cf69`. This commit is by Just van Rossum (2024-05-30) with message "Bump fontbakery" -- it bumped requirements.txt. The v2.000 release was created on 2024-05-30T05:39:24Z with the `Bungee-fonts.zip` asset.

4. **Timeline consistency**: Upstream commit `eb03cf69` on 2024-05-30, release created same day, PR #7796 created 2024-05-31 and merged same day. The timeline is consistent.

5. **Binary source**: The METADATA.pb uses `archive_url` pointing to the v2.000 release zip, with a files mapping from `Bungee_Basic/BungeeOutline-Regular.ttf` to `BungeeOutline-Regular.ttf`. The binary in google/fonts (202,152 bytes) differs from the older pre-built font in the upstream git tree's `fonts/` directory (238,148 bytes, version 1.000), confirming the font was taken from the release archive, not the git tree.

## How Config YAML Was Resolved

The upstream repository does **not** have a `config.yaml` at the referenced commit (or at any commit). It uses a custom `build.sh` script that invokes `fontmake` directly to compile UFO sources, along with Python assembly scripts (`assembleSources.py`, `assembleRotatedSources.py`, `assembleColorSources.py`).

An override `config.yaml` was added to the google/fonts family directory at `ofl/bungeeoutline/config.yaml` (commit `f6c68379a`, 2026-02-16). It contains:

```yaml
sources:
  - sources/2-build/Bungee_Basic/Bungee-Outline.ufo
familyName: Bungee Outline
buildStatic: true
buildOTF: false
```

The source path `sources/2-build/Bungee_Basic/Bungee-Outline.ufo` was verified to exist at the referenced commit `eb03cf69`.

Since the override config.yaml exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

## Verification

- **Repository URL**: Verified accessible (HTTP 200)
- **Commit hash**: Verified exists in upstream repo, matches v2.000 tag exactly
- **PR #7796**: Confirmed commit reference in both PR body and commit message
- **Source files**: UFO source at `sources/2-build/Bungee_Basic/Bungee-Outline.ufo` confirmed present at referenced commit
- **Override config.yaml**: Present in google/fonts family directory with correct source path
- **Archive URL**: Release zip at v2.000 confirmed accessible (HTTP 302 redirect, as expected for GitHub release assets)
- **Timeline**: All dates are consistent (upstream commit -> release -> PR creation -> merge)

## Confidence: HIGH

All metadata fields are complete and cross-verified through multiple independent sources. The commit hash matches the v2.000 release tag, is referenced explicitly in both the google/fonts commit message and PR #7796, and the timeline is fully consistent. The override config.yaml correctly points to the UFO source that exists at the referenced commit.

## Historical Notes

- **Original onboarding**: Commit `ca9abdfc4` by Marc Foley (2017-05-23) via PR #1002, "hotfix-bungeeoutline: v1.001 added". The original binary was 237,412 bytes.
- **Version 2.000 update**: Commit `d3d22093c` by Viviana Monsalve (2024-05-30) via PR #7796. Updated to 202,152 bytes from the v2.000 release zip.
- **Shared repository**: The upstream `djrrb/Bungee` repo is shared across 8 Bungee font families in Google Fonts.
