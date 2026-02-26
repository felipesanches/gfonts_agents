# Investigation Report: Big Shoulders

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders |
| Designer | Patric King |
| License | OFL |
| Date Added | 2025-02-06 |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | `8ba99c9e347396d828b263b8b818269cb99eb27c` |
| Branch | master |
| Config YAML | `Big-Shoulders/sources/config.yml` |
| Status | **Complete** |

## How URL Found

The repository URL is documented in the copyright field ("Copyright 2019 The Big Shoulders Project Authors (https://github.com/xotypeco/big_shoulders)"), in the commit message of the font addition, and in the related issue #7830.

## How Commit Determined

The commit hash was determined from the **commit message** of `7f99323ac` in google/fonts, authored by Yanone on 2025-02-07:

> "Big Shoulders: Version 2.002 added. Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/8ba99c9e347396d828b263b8b818269cb99eb27c. Resolves #7830"

**Cross-verification**: Commit `8ba99c9` is the HEAD of the master branch in the upstream repository ("Update README.md"). This is the latest commit, which is consistent with this being a very recent addition (February 2025). The font file `Big-Shoulders/fonts/variable/BigShoulders[opsz,wght].ttf` exists at this commit.

**Note**: Big Shoulders is a variable font with both `opsz` (optical size, 10-72) and `wght` (weight, 100-900) axes. This is the "parent" family that was added in 2025, while the split Display/Text variants have been in Google Fonts since 2019.

## Config YAML Status

The file `Big-Shoulders/sources/config.yml` exists at commit `8ba99c9` in the upstream repository. It contains a valid gftools-builder configuration for the BigShoulders variable font with `opsz` and `wght` axes, including STAT table definitions.

Key details:
- Source: `BigShoulders.glyphs`
- Axis order: opsz, wght
- Includes STAT table definitions for both axes
- Autohint OTF disabled

## Verification

- **Commit exists in upstream repo**: Yes (HEAD of master)
- **Config YAML exists at commit**: Yes (`Big-Shoulders/sources/config.yml`)
- **Font file exists at commit**: Yes (`Big-Shoulders/fonts/variable/BigShoulders[opsz,wght].ttf`)
- **Source block in METADATA.pb**: Complete with repository_url, commit, config_yaml, files mapping, and branch
- **Issue reference**: Resolves #7830 ("Update Big Shoulders families with `opsz` axis")

## Google Fonts History

1. `7f99323ac` - "Big Shoulders: Version 2.002 added" by Yanone (2025-02-07) - initial addition of the combined opsz+wght variable font
2. `cd53d4b52` - "Update METADATA.pb" (added menu subset)
3. `18f7f3d41` - "Update METADATA.pb date added"
4. `9d1b67ff5` - "Update OFL.txt - link"
5. `34926685b` - "Add config_yaml to METADATA.pb for 15 font families" (added config_yaml field)

## Confidence Level

**High** - All data is fully verified. The commit hash is explicitly referenced in the google/fonts commit message, verified to be HEAD of the upstream master branch, and the config.yml is present at that commit.

## Open Questions

None. This family is fully documented and verified.
