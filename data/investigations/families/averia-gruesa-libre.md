# Averia Gruesa Libre

**Date investigated**: 2026-02-26
**Status**: no_upstream_repo
**Designer**: Dan Sayers
**METADATA.pb path**: `ofl/averiagruesalibre/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | -- |
| Commit | -- |
| Config YAML | -- |
| Branch | -- |

## How the Repository URL Was Found

No repository URL is documented in the METADATA.pb (there is no `source { }` block). The designer Dan Sayers (i@iotic.com) has a GitHub account (IOTic) with only one unrelated repo (traccar-client-android). No font source repositories were found under his account.

A legacy `librefonts/averiagruesalibre` repo exists in the upstream cache, but it contains only TTX (decompiled font) files and metadata -- no editable source files (.glyphs, .ufo, .designspace, or .sfd). The `src/` directory contains only `METADATA_comments.txt` and `VERSIONS.txt`.

Broader GitHub searches for "averia gruesa libre" and "averiagruesalibre" yielded no relevant font source repositories.

The Averia project website at http://iotic.com/averia/ provides only font ZIP downloads, not source repositories. The Averia fonts were created through an algorithmic process of averaging all fonts on the creator's computer, using FontForge. This unique creation method means the "source" is essentially the averaging script and the input fonts, rather than traditional font design source files.

## How the Commit Hash Was Identified

N/A -- No upstream repository exists.

The last TTF-modifying commit in google/fonts is `e63e802be` ("hotfix-averiagruesalibre: v1.002 added", PR #836, by m4rc1e, merged 2017-05-08). The PR body was empty. The font was originally added in the initial commit `90abd17b4` of the google/fonts repo.

## How Config YAML Was Resolved

No `config.yaml` exists anywhere -- neither in any upstream repository nor in the google/fonts family directory. The librefonts/averiagruesalibre repo has no build-compatible source files. The font directory in google/fonts contains only the binary TTF, DESCRIPTION, FONTLOG, METADATA.pb, and OFL.txt.

According to the FONTLOG, Averia Gruesa Libre exists only in a Regular style and was created by algorithmically averaging all OFL-licensed fonts from the Google Web Fonts project as of November 9, 2011.

## Verification

- Commit exists in upstream repo: N/A
- Commit date: N/A
- Commit message: N/A
- Source files at commit: None -- no proper upstream repo exists

## Confidence

**High**: There is high confidence that no proper upstream repository with build-compatible sources exists for this font. The Averia fonts were created through an algorithmic averaging process, and the designer (Dan Sayers) has no font source repositories on GitHub. The only available repos (librefonts mirrors) contain decomposed TTX files, not editable sources.

## Open Questions

1. Does Dan Sayers still have the FontForge source files (.sfd) or averaging scripts used to generate the Averia fonts? Contact: i@iotic.com
2. The `eliheuer/averia-libre-vf` repo contains .glyphs sources for Averia Serif Libre (a related but different family) -- could a similar approach be taken for the other Averia variants?
3. Given the unique algorithmic origin of these fonts, should they be classified as "no rebuildable source" rather than "no_upstream_repo"?
