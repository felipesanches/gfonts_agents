# Investigation Report: Bodoni Moda

## Summary

Bodoni Moda is a variable serif typeface by Owen Earl (Indestructible Type), added to Google Fonts on 2020-11-25. It features optical size (opsz) and weight (wght) axes in both roman and italic. The upstream source data is well-documented and fully verified.

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bodoni Moda |
| Designer | Owen Earl |
| Repository URL | https://github.com/indestructible-type/Bodoni |
| Commit Hash | `30ce6cdc354ef179a3b72ba0f0e71826e599348c` |
| Branch | master |
| Config YAML | `sources/config.yaml` |
| License | OFL |
| Date Added | 2020-11-25 |

## How URL Found

The repository URL `https://github.com/indestructible-type/Bodoni` is explicitly stated in:
- The copyright string in METADATA.pb
- The gftools-packager commit messages for both v2.004 and v2.005 updates
- The source block of METADATA.pb

## How Commit Determined

The commit hash `30ce6cdc354ef179a3b72ba0f0e71826e599348c` is recorded in the gftools-packager commit message for the v2.005 update:

> [gftools-packager] Bodoni Moda: Version 2.005 added
> Bodoni Moda Version 2.005 taken from the upstream repo https://github.com/indestructible-type/Bodoni at commit 30ce6cdc354ef179a3b72ba0f0e71826e599348c.

This commit was authored by Emma Marichal on 2024-02-21 in google/fonts commit `634558fcb`.

The upstream commit `30ce6cd` is a merge commit: "Merge pull request #38 from emmamarichal/master" -- indicating Emma Marichal's PR to the upstream repo was merged, and the fonts were then packaged from that exact merge commit.

### Previous Version

The previous version (v2.004) was added by Rosalie Wagner on 2020-12-09 (commit `5cbf0538b`) from upstream commit `5457e20e8f7e16b53a5604dc08aca325142c172f`.

## Config YAML Status

The config file at `sources/config.yaml` exists at the recorded commit and contains valid gftools-builder configuration:
- Sources: `BodoniModa.glyphs`, `BodoniModa-Italic.glyphs`
- Axis order: opsz, wght, ital
- Family name: Bodoni Moda
- Includes STAT table definitions for both roman and italic variable fonts
- Builds only VF (no OTF)

## Verification

- **Commit exists in upstream**: Yes, verified. `30ce6cd` is the HEAD of the master branch.
- **Config.yaml exists at commit**: Yes, `sources/config.yaml` is present and valid.
- **Source files match METADATA.pb**: The METADATA.pb references `fonts/variable/BodoniModa[opsz,wght].ttf` and `fonts/variable/BodoniModa-Italic[opsz,wght].ttf`, both of which exist at the recorded commit.
- **Branch correct**: master, confirmed.
- **Upstream repo cached**: Yes, at `/mnt/shared/upstream_repos/fontc_crater_cache/indestructible-type/Bodoni`.

## Confidence Level

**HIGH** -- The commit hash is directly stated in the gftools-packager commit message, the upstream repo confirms the commit exists, the config.yaml is present, and all source file paths are valid.

## Open Questions

None. This family's source documentation is complete and verified.
