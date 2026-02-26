# Investigation Report: Cedarville Cursive

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Cedarville Cursive |
| **Designer** | Kimberly Geswein |
| **License** | OFL |
| **Date Added** | 2011-06-08 |
| **Repository URL** | https://github.com/librefonts/cedarvillecursive |
| **Commit Hash** | `cd212b0e2dc2364a3012ef43a3b9155c7ed0d352` |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | missing_config (VFB-only sources) |

## How URL Was Found

The repository URL `https://github.com/librefonts/cedarvillecursive` is a well-known librefonts archive repository. The cached clone at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/cedarvillecursive/` confirms the remote URL matches.

## How Commit Was Determined

The upstream repository has only a single commit:
- `cd212b0e2dc2364a3012ef43a3b9155c7ed0d352` - "update .travis.yml"

Since there is only one commit in the entire repository, this is the only possible commit to reference. The librefonts archive was created as a snapshot of existing fonts.

## Config YAML Status

**No config.yaml exists and none is possible.** The upstream repo contains only a VFB (FontLab binary) source file:
- `src/Cedarville-Cursive.vfb`

VFB is a proprietary FontLab format that is not compatible with gftools-builder. Building from this source would require FontLab Studio, not the standard Google Fonts build toolchain.

Other files in the repo are TTX decompositions of the compiled font and standard metadata files (DESCRIPTION, METADATA.json, OFL.txt).

**No override config.yaml** exists in `/mnt/shared/google/fonts/ofl/cedarvillecursive/`.

## Verification

- **Repository accessible**: Yes, cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/cedarvillecursive/`
- **Commit exists**: Yes, it is the only commit in the repo
- **Font file history in google/fonts**: The TTF file was part of the initial commit (`90abd17b4`) and was only touched once more by a fsType fix (`8ccda7bf7` by Dave Crossland in August 2015, which modified the file in-place)
- **METADATA.pb** does not have a source block (only basic metadata)
- **No source block**: The METADATA.pb has no source { } block at all

## Confidence Level

**HIGH** - The repository URL and commit are unambiguous. Single commit repo, VFB-only source. The status of "missing_config" is correct but expected since VFB sources cannot use gftools-builder.

## Open Questions

None. This is a legacy font with VFB-only sources. A config.yaml would only be possible if the font were to be converted to a gftools-builder-compatible format (e.g., .glyphs or .ufo). The librefonts archive serves as a reference/backup but cannot be used for rebuilding the font with modern tools.
