# Cantata One - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cantata One |
| Designer | Joana Correia |
| License | OFL |
| Date Added | 2012-02-29 |
| Repository URL | https://github.com/librefonts/cantataone |
| Commit Hash | 947c3dd6e969867a02166335a27c48c0a7f9123d |
| Branch | master |
| Config YAML | N/A |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/cantataone` was added as part of the batch source blocks commit (9a14639f3, "Add source blocks to 602 more METADATA.pb files"). The librefonts organization hosts mirrors of many Google Fonts projects.

The copyright notice in METADATA.pb references "Sorkin Type Co (www.sorkintype.com eben@eyebytes.com)" with Reserved Font Name "Cantata", indicating Eben Sorkin / Sorkin Type Co. as the foundry. However, no dedicated upstream repo was found outside of the librefonts mirror.

## How Commit Determined

The commit `947c3dd6e969867a02166335a27c48c0a7f9123d` is the HEAD (and only commit) of the librefonts/cantataone repository, dated 2014-10-17. The commit message is "update .travis.yml". This is a single-commit repo.

The font binary in google/fonts has never been updated since the initial commit (90abd17b4). There was a chmod fix (49fbebd3d) and a designer key update (c7c958c83), but no font file changes. The deploy commit (76adaf1d2) appears to be the initial deployment.

Since the librefonts repo has only one commit, the recorded hash is the only valid option.

## Config YAML Status

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in google/fonts either.

The upstream repo contains FontForge SFD sources (`src/CantataOne-Regular-OTF.sfd`, `src/CantataOne-Regular-TTF.sfd`) and a VFB file (`src/CantataOne-Regular.vfb`). These are not gftools-builder compatible formats.

## Verification

- **Commit hash verified**: The hash `947c3dd` exists in the librefonts/cantataone repository and is HEAD of master. CONFIRMED.
- **Repository accessible**: librefonts/cantataone is a valid GitHub repository. CONFIRMED.
- **Source files**: Only SFD and VFB formats available, no .glyphs/.ufo/.designspace sources.
- **Single-commit repo**: Only one commit in the entire history (2014-10-17).

## Confidence Level

**HIGH** - The repository URL and commit hash are correct. The librefonts mirror is the only known upstream. The font has never been updated since its initial addition to Google Fonts in 2012.

## Open Questions

- The original designer Joana Correia / Sorkin Type Co may have source files in other formats not publicly available.
- No path to gftools-builder compatibility without source conversion from SFD/VFB format.
