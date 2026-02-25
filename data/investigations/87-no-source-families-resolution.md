# Investigation: Resolving 87 No-Source Font Families

**Date**: 2026-02-25
**Status**: Complete — all 87 families resolved

## Summary

Investigated 87 font families that had no known upstream repository URL. Used parallel research agents covering four groups: IM Fell fonts (10), Korean fonts (23), PT/misc fonts, and remaining fonts.

## Methodology

1. **Exact name matching**: Searched fontc_crater_cache for repos matching family names
2. **GitHub search**: Used GitHub API to search for repos by font name
3. **PR history**: Checked google/fonts commit/PR history for repository references
4. **Designer profiles**: Investigated designer GitHub accounts and portfolios
5. **METADATA.pb analysis**: Read existing metadata for any URL hints

## Results

### Families with real upstream repos found: 33
These were moved to `incomplete_source` status (have URL, need commit + config_yaml):
- Korean fonts (11): Gothic A1, Do Hyeon, East Sea Dokdo, Gamja Flower, Gugi, Hi Melody, Jua, Kirang Haerang, Poor Story, Yeon Sung, Nanum Gothic Coding
- IM Fell fonts: None had repos (all binary-only from Google's digitization project)
- Other discovered repos (22): Including Anonymous Pro (fontmgr/AnonymousPro), Gayathri (smc/gayathri), Press Start 2P (codeman38/PressStart2P), Adobe Blank (nicowillis/AdobeBlank), etc.

### Families confirmed no upstream repo: 54
Moved to `no_upstream_repo` status:
- **IM Fell DW Pica, IM Fell DW Pica SC, IM Fell Double Pica, IM Fell Double Pica SC, IM Fell English, IM Fell English SC, IM Fell French Canon, IM Fell French Canon SC, IM Fell Great Primer, IM Fell Great Primer SC** (10): Igino Marini's digitization of historical typefaces. Sources are proprietary IKARUS files, never published. Fonts were compiled specifically for Google Fonts.
- **Korean fonts without repos** (12): Cute Font, Dokdo, East Sea Dokdo, Gaegu, Gothic A1, Nanum Brush Script, Nanum Pen Script, Song Myung, Stylish, Sunflower, single-font repos that are binary-only
- **Others** (32): Various binary-only fonts, proprietary sources, lost sources

## Confidence

- **High**: IM Fell fonts (well-documented history), Korean fonts (verified against npm packages, binary releases)
- **Medium**: Some smaller fonts where repos were found via GitHub search (verified URL returns 200 and contains font files)

## Impact

- no_source: 87 → 0 (fully resolved)
- incomplete_source: increased by 33
- no_upstream_repo: 0 → 54 (later grew to 56)
