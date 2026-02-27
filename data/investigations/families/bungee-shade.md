# Bungee Shade

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: David Jonathan Ross
**METADATA.pb path**: `ofl/bungeeshade/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/djrrb/Bungee |
| Commit | `eb03cf69adab5094f6b84e95357789cdf3bfeb99` |
| Config YAML | override config.yaml in google/fonts |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/djrrb/Bungee` was already present in the METADATA.pb `source { repository_url }` field. It is confirmed by:
- The copyright string in the font files: "Copyright 2023 The Bungee Project Authors (https://github.com/djrrb/Bungee)"
- The commit message for the v2.000 update (commit `673c50cae` in google/fonts): "Taken from the upstream repo https://github.com/djrrb/Bungee at commit https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99"
- PR #7798 in google/fonts, authored by Viviana Monsalve, which confirms the same URL

## How the Commit Hash Was Identified

The commit hash `eb03cf69adab5094f6b84e95357789cdf3bfeb99` was identified from:

1. **METADATA.pb**: Already recorded in the `source { commit }` field
2. **google/fonts commit message** (`673c50cae`, 2024-05-30): Explicitly states the commit URL
3. **PR #7798** body: Confirms the same commit reference
4. **Upstream v2.000 tag**: The tag `v2.000` in the upstream repo points exactly to this commit

The referenced commit (`eb03cf69`) has the message "Bump fontbakery" and was authored by Just van Rossum on 2024-05-30. While this specific commit only changes `requirements.txt`, the v2.000 tag points to it, meaning this was the final state used for the v2.000 release.

The METADATA.pb also includes an `archive_url` pointing to the v2.000 release: `https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip`, with a `files {}` block mapping `Bungee_Basic/BungeeShade-Regular.ttf` to `BungeeShade-Regular.ttf`. This means the binary was taken from the release zip, not compiled from sources.

## Build Configuration

The upstream Bungee repository does **not** have a `config.yaml` file at the referenced commit (or at any commit). The project uses a custom `build.sh` script that calls `fontmake` directly for each UFO source, along with Python scripts (`assembleSources.py`, `assembleRotatedSources.py`, `assembleColorSources.py`) to prepare sources before building.

An override `config.yaml` exists in the google/fonts family directory (`ofl/bungeeshade/config.yaml`), added by commit `f6c68379a` ("Add override config.yaml for 50 font families"). This override config contains:

```yaml
sources:
  - sources/2-build/Bungee_Basic/Bungee-Shade.ufo
familyName: Bungee Shade
buildStatic: true
buildOTF: false
```

The source path `sources/2-build/Bungee_Basic/Bungee-Shade.ufo` exists at commit `eb03cf69` (v2.000) but was removed from the repo at commit `7ffc5a64` (2024-06-07, "remove /fonts folders and /2-build folder"), which is part of the v2.001 cycle. The override config is therefore valid for the recorded commit.

Since the override config.yaml is in the google/fonts directory, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block (google-fonts-sources auto-detects local overrides).

## Source File Formats

At commit `eb03cf69`, the Bungee Shade sources are:
- **UFO3**: `sources/2-build/Bungee_Basic/Bungee-Shade.ufo` (the build-ready source)
- **Drawing sources**: `sources/1-drawing/` contains the original drawing sources that get assembled by `scripts/assembleSources.py`

The Bungee project has a multi-stage pipeline: drawing sources are assembled into build-ready UFOs, which are then compiled to fonts.

## Relationship to Other Bungee Families

Bungee Shade shares the `djrrb/Bungee` upstream repository with several other Bungee families in Google Fonts:
- **Bungee** (`ofl/bungee`) - Regular weight
- **Bungee Color** (`ofl/bungeecolor`)
- **Bungee Hairline** (`ofl/bungeehairline`)
- **Bungee Inline** (`ofl/bungeeinline`)
- **Bungee Outline** (`ofl/bungeeoutline`)
- **Bungee Spice** (`ofl/bungeespice`)
- **Bungee Tint** (`ofl/bungeetint`)

All share the same upstream commit hash `eb03cf69` for their v2.000 onboarding.

## Timeline

- **2017-05-23**: Bungee Shade v1.001 initially added to google/fonts by Marc Foley (commit `8ec727b2c`, PR #992)
- **2024-05-30**: Version 2.000 added by Viviana Monsalve (commit `673c50cae`, PR #7798), from upstream commit `eb03cf69` (v2.000 tag)
- **2024-05-31**: PR #7798 merged by Emma Marichal

## Post-Onboarding Upstream Activity

After the v2.000 tag (commit `eb03cf69`), the upstream repo has seen significant activity:
- **v2.001** (tag at `dbf8a1c4`, 2024-06-29): Renamed "Bungee Color" to "Bungee Tint", removed `/fonts` and `/2-build` folders, added article content
- **v3.0-preview** tag also exists
- The `sources/2-build/` directory was removed in commit `7ffc5a64` (2024-06-07), meaning the override config.yaml path would not work at HEAD

These changes have NOT been incorporated into google/fonts and would require separate review.

## Issues Found

None. The METADATA.pb source block is complete and accurate:
- Repository URL is correct and verified
- Commit hash matches the v2.000 tag exactly
- Branch is correctly set to `master`
- Archive URL and file mapping are present for the pre-built binary
- Override config.yaml in google/fonts correctly references the UFO source path at the recorded commit
- No `config_yaml` field needed in METADATA.pb (auto-detected local override)
