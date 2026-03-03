# Abril Fatface

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: missing_config
**Designer**: TypeTogether
**METADATA.pb path**: `ofl/abrilfatface/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/abrilfatface |
| Commit | `5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f` |
| Config YAML | -- |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/abrilfatface` is recorded in the `source { }` block of `ofl/abrilfatface/METADATA.pb`. The source block was added by commit `5e7d9dd14` in google/fonts (dated 2026-02-26, message: "Abril Fatface: add source block to METADATA.pb").

The remote URL was verified against the cached clone at `upstream_repos/fontc_crater_cache/librefonts/abrilfatface`, which confirms `origin` points to `https://github.com/librefonts/abrilfatface`.

The `librefonts` organization on GitHub hosts TTX-decomposed mirrors of many early Google Fonts families. This is not the original design source from TypeTogether; it is an archival/reproducibility mirror created by Dave Crossland's toolchain (the single commit is authored by `hash3g <hash.3g@gmail.com>`).

## How the Commit Hash Was Identified

The upstream repository contains exactly **one commit**: `5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f` (dated 2014-10-17, message: "update .travis.yml", author: hash3g). Since this is the only commit in the entire repository (on the sole branch `master`), it trivially represents the complete state of the repo.

The font was originally added to Google Fonts on 2011-08-31 (per `date_added` in METADATA.pb). In google/fonts itself, the font binary `AbrilFatface-Regular.ttf` was added in commit `90abd17b4` (2015-03-07, "Initial commit" -- the initial bulk import of the entire google/fonts repository). The font has not been updated since.

The librefonts repo was created in 2014, well after the font's original onboarding in 2011, confirming this repo is a retroactive archive rather than the original production source.

## How Config YAML Was Resolved

No `config.yaml` exists anywhere in the upstream repository. No override `config.yaml` exists in the google/fonts family directory (`ofl/abrilfatface/`).

The upstream repo contains only legacy source formats incompatible with gftools-builder:

- `src/AbrilFatface-Regular-TTF.sfd` -- FontForge SFD format
- `src/AbrilFatface-Regular.vfb` -- FontLab VFB binary format
- `src/AbrilFatface-Regular.otf.*.ttx` -- TTX-decomposed OTF table files
- Root-level `AbrilFatface-Regular.ttf.*.ttx` -- TTX-decomposed TTF table files

There are no `.glyphs`, `.ufo`, or `.designspace` files, which are the formats required by gftools-builder. A meaningful `config.yaml` cannot be created without first converting the sources to a modern editable format. The SFD and VFB files represent legacy toolchain sources (FontForge and FontLab Studio 5 respectively).

## Verification

- **Commit exists in upstream repo**: Yes (verified with `git log`)
- **Commit date**: 2014-10-17 13:27:35 +0300
- **Commit author**: hash3g <hash.3g@gmail.com>
- **Commit message**: "update .travis.yml"
- **Total commits in repo**: 1 (single-commit repository)
- **Branch**: `master` (only branch)
- **Remote URL matches METADATA.pb**: Yes

## Confidence

**MEDIUM**: The repository URL and commit hash are verified and correct. However, `librefonts/abrilfatface` is a legacy TTX-decomposed mirror, not the original design source from TypeTogether. The font predates the repo (2011 vs 2014). The source formats (SFD/VFB) are not compatible with gftools-builder, so no config.yaml can be created without a source format conversion.

## Open Questions

- Does TypeTogether maintain an original source repository for Abril Fatface with `.glyphs` or `.ufo` sources that could serve as a more appropriate upstream?
- Since the source formats (SFD/VFB) are not gftools-builder compatible, is there a plan to convert the sources to a modern format?
- The font has been in Google Fonts since 2011 and has not been updated since the initial repository import. Is an update planned?

## Conclusion

The source block in METADATA.pb is correct: it points to `librefonts/abrilfatface` at its sole commit `5e899bfd`. The repository is a legacy TTX/SFD/VFB mirror with no gftools-builder-compatible sources and no config.yaml. The status remains `missing_config` because no config.yaml can be meaningfully created from the available source formats without a conversion to `.glyphs`, `.ufo`, or `.designspace`.
