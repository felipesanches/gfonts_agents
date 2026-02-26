# Cormorant Garamond - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Cormorant Garamond |
| **Designer** | Christian Thalmann |
| **Repository URL** | https://github.com/CatharsisFonts/Cormorant |
| **Commit** | `6d210fd3550b7358ca62d6ba3e354ec1ec940813` |
| **Branch** | master |
| **Config YAML** | `sources/config-garamond.yaml` |
| **Date Added** | 2017-01-18 |
| **License** | OFL |
| **Status** | Complete |

## How URL Found

The repository URL `https://github.com/CatharsisFonts/Cormorant` is the shared upstream repo for all Cormorant variants. It is documented in:

1. METADATA.pb source block
2. Copyright strings: "Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant)"
3. PR #4890 (v4.000): "taken from the upstream repo https://github.com/CatharsisFonts/Cormorant"
4. PR #8593 (v4.001): "Taken from the upstream repo https://github.com/CatharsisFonts/Cormorant"

## How Commit Determined

The commit `6d210fd3550b7358ca62d6ba3e354ec1ec940813` is explicitly referenced in:

1. **METADATA.pb source block**: `commit: "6d210fd3550b7358ca62d6ba3e354ec1ec940813"`
2. **google/fonts commit 93473babe** (by Simon Cozens): "Cormorant Garamond: Version 4.001 added ... Taken from the upstream repo https://github.com/CatharsisFonts/Cormorant at commit https://github.com/CatharsisFonts/Cormorant/commit/6d210fd3550b7358ca62d6ba3e354ec1ec940813"
3. **PR #8593 body**: Same explicit reference

### Update History

- **v4.000** (PR #4890, 2022-07-05, by m4rc1e): Used commit `cc1bfb51ce6568cb3abf9199ab718d543f6fa189`
- **v4.001** (PR #8593, 2024-11-26, by simoncozens): Updated to commit `6d210fd3550b7358ca62d6ba3e354ec1ec940813` - converted from static to variable fonts

The v4.001 update was a significant change: it converted Cormorant Garamond from 10 static .ttf files to 2 variable font files (`CormorantGaramond[wght].ttf` and `CormorantGaramond-Italic[wght].ttf`).

Commit `6d210fd` is "Merge pull request #75 from simoncozens/vf-and-gf" with description "Build variable fonts for Google Fonts". This is the current HEAD of the upstream repo.

## Config YAML Status

At commit `6d210fd`, the file `sources/config-garamond.yaml` exists and contains a valid gftools-builder config:
```yaml
sources:
  - generated/CormorantGaramond.glyphs
  - generated/CormorantGaramond-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Cormorant Garamond
buildStatic: False
buildWebfont: True
buildSmallCap: False
...
```

This config was added as part of the vf-and-gf branch (PR #75 in the upstream repo). No override config.yaml exists in the google/fonts family directory.

## Verification

- **Upstream repo cached**: Yes, at `/mnt/shared/upstream_repos/fontc_crater_cache/CatharsisFonts/Cormorant/`
- **Commit exists**: Yes, it is the current HEAD of the repo
- **Config file exists at commit**: Yes, `sources/config-garamond.yaml` is present at 6d210fd
- **Font files match**: METADATA.pb maps `fonts/variable/CormorantGaramond[wght].ttf` and `fonts/variable/CormorantGaramond-Italic[wght].ttf`
- **Repository accessible**: Yes

## Confidence Level

**HIGH** - All data is explicitly documented in commit messages, PR bodies, and METADATA.pb. Multiple independent confirmations exist.

## Open Questions

None. This family is fully documented and verified.
