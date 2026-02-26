# Investigation Report: Bodoni Moda SC

## Summary

Bodoni Moda SC (Small Caps) is a variable serif typeface from the same upstream repository as Bodoni Moda, added to Google Fonts on 2024-05-27. It shares the same upstream repository and commit hash as Bodoni Moda but presents a notable issue: the referenced source files (BodoniModaSC variable fonts) do not exist in the upstream repository at the recorded commit.

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bodoni Moda SC |
| Designer | Owen Earl |
| Repository URL | https://github.com/indestructible-type/Bodoni |
| Commit Hash | `30ce6cdc354ef179a3b72ba0f0e71826e599348c` |
| Branch | master |
| Config YAML | `sources/config.yaml` |
| License | OFL |
| Date Added | 2024-05-27 |

## How URL Found

The repository URL is the same as Bodoni Moda. It is stated in:
- The copyright string in METADATA.pb
- The commit message by Simon Cozens adding Bodoni Moda SC: "Taken from the upstream repo https://github.com/indestructible-type/Bodoni at commit 30ce6cdc354ef179a3b72ba0f0e71826e599348c."

## How Commit Determined

The commit hash `30ce6cdc354ef179a3b72ba0f0e71826e599348c` is recorded in the commit message by Simon Cozens (google/fonts commit `c910e0d6c`, dated 2024-05-27):

> Bodoni Moda SC: Version 2.005 added
> Taken from the upstream repo https://github.com/indestructible-type/Bodoni at commit 30ce6cdc354ef179a3b72ba0f0e71826e599348c.

This is the same commit used for Bodoni Moda.

## Config YAML Status

The config file at `sources/config.yaml` exists at the recorded commit. However, there is a notable issue: the config only defines build outputs for `BodoniModa[opsz,wght].ttf` and `BodoniModa-Italic[opsz,wght].ttf` (the regular family), with `familyName: Bodoni Moda`. It does not contain a separate configuration for the SC variant.

The SC variant was likely generated through a separate build process or post-processing step (e.g., activating the small caps OpenType feature and subsetting) rather than directly from this config.yaml.

## Verification

- **Commit exists in upstream**: Yes, verified. Same commit as Bodoni Moda.
- **Config.yaml exists at commit**: Yes, but it only builds the regular (non-SC) variant.
- **Source files match METADATA.pb**: **MISMATCH**. The METADATA.pb references:
  - `fonts/variable/BodoniModaSC[opsz,wght].ttf`
  - `fonts/variable/BodoniModaSC-Italic[opsz,wght].ttf`

  These files do **not** exist in the upstream repository at the recorded commit. The `fonts/variable/` directory only contains `BodoniModa[opsz,wght].ttf` and `BodoniModa-Italic[opsz,wght].ttf`.
- **Branch correct**: master, confirmed.
- **Upstream repo cached**: Yes, at `/mnt/shared/upstream_repos/fontc_crater_cache/indestructible-type/Bodoni`.

## Confidence Level

**MEDIUM** -- The repository URL and commit hash are correctly documented and verified. However, the source file paths in METADATA.pb reference files that do not exist in the upstream repo at that commit. The SC variant was likely built from the same Glyphs sources using a different build pipeline (small caps extraction), but this is not reflected in the config.yaml. The `config_yaml` field pointing to `sources/config.yaml` is technically not the config that builds the SC variant.

## Open Questions

1. How were the BodoniModaSC variable fonts generated? They don't exist as pre-built files in the upstream repo, and the config.yaml does not define an SC build target.
2. Was a separate (undocumented) build configuration used by Simon Cozens to produce the SC variant from the same Glyphs sources?
3. Should the `config_yaml` field be removed or corrected, since the referenced config does not actually build the SC variant?
