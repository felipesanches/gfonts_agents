# Investigation Report: Bungee Spice

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: David Jonathan Ross
**METADATA.pb path**: `ofl/bungeespice/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bungee Spice |
| Repository URL | https://github.com/djrrb/Bungee |
| Commit Hash | `eb03cf69adab5094f6b84e95357789cdf3bfeb99` |
| Branch | master |
| Config YAML | Override in google/fonts (`ofl/bungeespice/config.yaml`) |
| Date Added | 2022-04-05 |
| License | OFL |
| Status | complete |
| Confidence | HIGH |

## How the Repository URL Was Found

The repository URL `https://github.com/djrrb/Bungee` is recorded in the METADATA.pb `source { repository_url }` field. It was added by Viviana Monsalve in commit `a7a9198fd` ("Bungee Spice github repo url added") during the v2.000 update cycle. The repository belongs to David Jonathan Ross (djrrb), the designer of the entire Bungee family. All Bungee variants (Bungee, Bungee Color, Bungee Hairline, Bungee Inline, Bungee Outline, Bungee Shade, Bungee Spice, Bungee Tint) share this single upstream repository. The copyright notice in METADATA.pb confirms this: "Copyright 2023 The Bungee Project Authors (https://github.com/djrrb/Bungee)".

## How the Commit Hash Was Identified

The commit `eb03cf69adab5094f6b84e95357789cdf3bfeb99` is explicitly stated in the google/fonts commit message for the v2.000 update:

```
17bae36eb Bungee Spice: Version 2.000 added
Taken from the upstream repo https://github.com/djrrb/Bungee at commit
https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99.
```

This commit was authored by Viviana Monsalve on 2024-05-30 and merged via PR #7799 on 2024-05-31, reviewed and merged by Emma Marichal.

**Cross-verification**:
- The commit `eb03cf69` exists in the upstream repo, dated 2024-05-30 07:17:37 +0200, with message "Bump fontbakery" (authored by Just van Rossum).
- The `v2.000` git tag points exactly to this commit, confirmed via `git rev-parse v2.000`.
- The METADATA.pb also references `archive_url: "https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip"`, and the v2.000 GitHub release was published on 2024-05-30.
- The same commit hash is used for Bungee, Bungee Hairline, Bungee Inline, Bungee Outline, and Bungee Shade (all updated simultaneously in PRs #7794-#7799).

### Onboarding History

Bungee Spice has a more complex history than the other "basic" Bungee variants:

- **Initial add** (2021-12-07): Added by Rod Sheeter (PR #4154, commit `e15b29728`) as an experimental COLRv1 color font.
- **Color table processing** (2022): Multiple rounds of color table manipulation using `maximum_color` from nanoemoji:
  - `e6fe96669` - Exploratory generation of additional color tables (2022-03-30)
  - `9f92199e0` - Test builds passed through nanoemoji's maximum_color (2022-04-04)
  - `10375130e` - "Drop COLR, lets see what breaks :D" (2022-04-05)
  - `ddede62c2` - Revert the COLR drop after identifying breakage (2022-04-06)
  - `12ed8f97f` - Removed CBDT, ran maximum_color when only one of COLR/SVG present (PR #4993, 2022-07-27)
  - `87ecc71a0` - Re-run maximum_color to fix colored .notdef glyph reshuffling (PR #5171, 2022-09-01)
- **v2.000 update** (2024-05-30): Updated by Viviana Monsalve (PR #7799, commit `17bae36eb`) from upstream commit `eb03cf69`.

## Config YAML Status

**No config.yaml in upstream repo** at any commit. The Bungee project uses a custom build pipeline (`build.sh`). For Bungee Spice specifically, the build process is particularly complex:
1. Assembly scripts (`scripts/assembleColorSources.py`) create color source files
2. `fontmake` compiles the UFO to TTF
3. `maximum_color` post-processes the TTF to add SVG tables, making it a full COLRv1+SVG color font

**Override config.yaml** exists in google/fonts at `ofl/bungeespice/config.yaml`, created in commit `f6c68379a` ("Add override config.yaml for 50 font families"):

```yaml
sources:
  - sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo
familyName: Bungee Spice
buildStatic: true
buildOTF: false
```

This override points to `sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo` which exists at the recorded commit `eb03cf69`. Since the override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

**Important caveats**:
1. The `sources/2-build/` directory was removed from the upstream repo in commit `7ffc5a64` (2024-06-07), one week after the v2.000 release. This override config only works with the recorded commit hash, not with later commits.
2. The override config may not fully reproduce the original binary, because Bungee Spice is a COLRv1 color font that requires additional post-processing with `maximum_color` to add SVG tables. A standard gftools-builder invocation from the UFO source alone would not produce an equivalent font.

## Source File Formats

At the recorded commit `eb03cf69`, the Bungee Spice-related sources are:

- `sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo` - The buildable UFO source (familyName: "Bungee Color")
- `sources/2-build/Bungee_Color/Bungee_Color-Regular.ttf` - A pre-built binary alongside the source
- `sources/1-drawing/Bungee-Regular.ufo` - The base drawing source (shared with other Bungee variants)

No `.glyphs` or `.designspace` files exist in the repository.

## Verification

- **Repository URL**: Valid, accessible GitHub repository at https://github.com/djrrb/Bungee
- **Commit hash exists**: Confirmed `eb03cf69` exists in the upstream repo
- **Tag alignment**: The `v2.000` tag points exactly to commit `eb03cf69`
- **Source files at commit**: `sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo` confirmed present
- **Override config**: References existing source path at the recorded commit
- **Binary source**: METADATA.pb uses `archive_url` pointing to v2.000 release zip; the binary was taken from `Bungee_Color/BungeeSpice-Regular.ttf` within the archive
- **PR provenance**: PR #7799 created by Viviana Monsalve (vv-monsalve), merged by Emma Marichal (emmamarichal) on 2024-05-31

## Confidence Level

**HIGH** - The commit hash is explicitly stated in the google/fonts commit message and confirmed in PR #7799. It aligns exactly with the upstream v2.000 release tag. The override config.yaml points to valid sources at the recorded commit. The binary was sourced from the v2.000 release archive.

## Open Questions

1. **Color font reproduction**: Can gftools-builder produce a fully equivalent Bungee Spice binary from the UFO source alone, or does it require the `maximum_color` post-processing step? The override config may produce a font without the SVG table that the current binary includes. This is relevant for fontc_crater testing.
