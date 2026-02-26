# Averia Libre

**Date investigated**: 2026-02-26
**Status**: no_upstream_repo
**Designer**: Dan Sayers
**METADATA.pb path**: `ofl/averialibre/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | -- |
| Commit | -- |
| Config YAML | -- |
| Branch | -- |

## How the Repository URL Was Found

No repository URL is documented in the METADATA.pb (there is no `source { }` block). The designer Dan Sayers (i@iotic.com) has a GitHub account (IOTic) with only one unrelated repo. No font source repositories were found under his account.

A legacy `librefonts/averialibre` repo exists in the upstream cache. It contains TTX (decompiled font) files for all 6 styles (Regular, Italic, Light, LightItalic, Bold, BoldItalic) but no editable source files. The `src/` directory contains only `METADATA_comments.txt` and `VERSIONS.txt`.

A separate repo `eliheuer/averia-libre-vf` exists on GitHub, created in December 2018. It contains `.glyphs` sources for Averia **Serif** Libre (not Averia Libre), and represents a variable font conversion project by Eli Heuer, not the original Dan Sayers source. The source files are named `Averia-Serif-Libre-Italic.glyphs` and `Averia-Serif-Libre-Roman.glyphs`, confirming this is for a different family variant.

The Averia project website at http://iotic.com/averia/ provides ZIP downloads but no source repositories. The fonts were created by algorithmically averaging all OFL-licensed fonts from Google Web Fonts.

## How the Commit Hash Was Identified

N/A -- No upstream repository with the original sources exists.

The last TTF-modifying commit in google/fonts is `fc10731b1` ("hotfix-averialibre: v1.002 added", PR #837, by m4rc1e, merged 2017-08-07). The PR body was empty. All 6 font files were modified in this hotfix (small size changes, likely metadata fixes). The font was originally added in the initial commit `90abd17b4` of the google/fonts repo.

## How Config YAML Was Resolved

No `config.yaml` exists anywhere. The librefonts/averialibre repo has no build-compatible source files. The google/fonts family directory contains only the 6 binary TTFs, DESCRIPTION, FONTLOG, METADATA.pb, and OFL.txt.

Averia Libre is a 6-style family (Light, LightItalic, Regular, Italic, Bold, BoldItalic), all created through the averaging process described in the FONTLOG.

## Verification

- Commit exists in upstream repo: N/A
- Commit date: N/A
- Commit message: N/A
- Source files at commit: None -- no proper upstream repo exists

## Confidence

**High**: There is high confidence that no proper upstream repository with build-compatible sources exists. The Averia font family was algorithmically generated. Dan Sayers has no font repositories on GitHub. The librefonts mirrors contain only decomposed TTX files.

## Open Questions

1. Does Dan Sayers still have the FontForge source files or averaging scripts? Contact: i@iotic.com
2. Could the `eliheuer/averia-libre-vf` variable font project (which covers Averia Serif Libre) be extended to cover Averia Libre as well?
3. Should this family be classified as "no rebuildable source" given its algorithmic origin?
