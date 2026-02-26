# Cantora One - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cantora One |
| Designer | Impallari Type |
| License | OFL |
| Date Added | 2012-07-30 |
| Repository URL | https://github.com/librefonts/cantoraone |
| Commit Hash | 45d202afe1668a05e0afd870e124d72c2b82143c |
| Branch | master |
| Config YAML | N/A |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/cantoraone` was added as part of the batch source blocks commit (9a14639f3, "Add source blocks to 602 more METADATA.pb files"). The librefonts organization hosts mirrors of many Google Fonts projects.

The original designer is Pablo Impallari (Impallari Type). No repo was found at `impallari/Cantora-One` on GitHub. The Impallari GitHub organization does have repos for some other fonts (e.g., Cabin, Encode Sans, Libre Baskerville), but not for Cantora One. The librefonts mirror is the only known upstream.

## How Commit Determined

The commit `45d202afe1668a05e0afd870e124d72c2b82143c` is the HEAD (and only commit) of the librefonts/cantoraone repository, dated 2014-10-17. The commit message is "update .travis.yml". This is a single-commit repo.

The font binary in google/fonts was last updated in PR #5355 (commit 8c5835c11, 2022-10-07, "Cantora One: version 1.002 added HOTFIX" by Rosalie Wagner). This hotfix addressed a ligature bug (issue #3089, where "ffu" rendered as "ffh"). The fix was a manual hotfix applied directly to the binary font, not a rebuild from the upstream sources.

Since the librefonts repo has only one commit, the recorded hash is the only valid option. However, this hash does NOT correspond to the sources used for the current binary - the current binary was manually hotfixed in google/fonts.

## Config YAML Status

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in google/fonts either.

The upstream repo contains only VFB files as sources:
- `src/CantoraOne-Regular.vfb` (original source)
- `src/CantoraOne-Regular-OTF.vfb` (OTF variant)
- `src/CantoraOne-Regular-TTF.vfb` (TTF variant)

Along with TTX decomposed tables and a FONTLOG. VFB (FontLab) files are not gftools-builder compatible formats. No SFD, .glyphs, .ufo, or .designspace files are present.

## Verification

- **Commit hash verified**: The hash `45d202a` exists in the librefonts/cantoraone repository and is HEAD of master. CONFIRMED.
- **Repository accessible**: librefonts/cantoraone is a valid GitHub repository. CONFIRMED.
- **Source files**: Only VFB (FontLab) format and TTX decomposed tables. No buildable sources.
- **Single-commit repo**: Only one commit in the entire history (2014-10-17).
- **Current binary does NOT match upstream sources**: The binary was manually hotfixed in PR #5355 (Oct 2022) to fix a ligature bug, so the current font in google/fonts differs from what the upstream sources would produce.

## Confidence Level

**HIGH** for URL and commit hash accuracy. The librefonts mirror is the correct upstream, and the only commit hash is the recorded one.

**LOW** for source-to-binary correspondence. The current binary was hotfixed directly and does not correspond to a build from the upstream VFB sources.

## Open Questions

- The original designer (Pablo Impallari) may have more current source files that are not publicly available.
- No path to gftools-builder compatibility without source conversion from VFB format.
- The hotfix in PR #5355 was applied directly to the binary; the upstream repo does not reflect these changes.
