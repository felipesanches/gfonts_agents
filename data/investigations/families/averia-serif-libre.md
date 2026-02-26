# Averia Serif Libre

**Date investigated**: 2026-02-26
**Status**: no_upstream_repo
**Designer**: Dan Sayers
**METADATA.pb path**: `ofl/averiaseriflibre/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | -- |
| Commit | -- |
| Config YAML | -- |
| Branch | -- |

## How the Repository URL Was Found

No upstream repository was found. The Averia font family was created by Dan Sayers using an unusual algorithmic process: averaging all fonts on his computer to produce composite glyphs. The process is documented at http://iotic.com/averia/.

Dan Sayers has a GitHub account (`dansayers`) but only has one public repository (`dansayers/dissonance`), which is a JavaScript project unrelated to fonts. No Averia-related source repository exists on GitHub under his account.

A GitHub search for "averia font", "averia libre font", and "averia serif" yielded no legitimate upstream repositories -- only third-party projects that bundle the font files.

The copyright notice in the font files references `i@iotic.com` but does not include a repository URL. The FONTLOG.txt and DESCRIPTION.en_us.html both point to http://iotic.com/averia/ as the project page, not a source repository.

The font was originally added to Google Fonts on 2012-03-14 (initial commit `90abd17b4`), and was last updated by Marc Foley in PR #839 on 2017-08-07 with the commit message "hotfix-averiaseriflibre: v1.002 added". PR #839 has an empty body and no comments, providing no upstream reference.

The "Averia Libre" family of fonts (including Averia Serif Libre, Averia Sans Libre, Averia Libre, and Averia Gruesa Libre) are all in the same situation -- none have upstream repositories on GitHub or any other known hosting service.

## How the Commit Hash Was Identified

No commit hash is available since no upstream repository exists.

## How Config YAML Was Resolved

No config.yaml exists, either as an override in the google/fonts family directory or in any upstream repository. Since the font was created through an algorithmic averaging process and no source files (.glyphs, .ufo, .designspace) are known to exist, a gftools-builder config.yaml would not be applicable in the traditional sense.

## Verification

- Commit exists in upstream repo: N/A
- Commit date: N/A
- Commit message: N/A
- Source files at commit: N/A

## Confidence

**High**: The Averia font family was created through a unique algorithmic process (averaging all fonts on the creator's computer) rather than traditional font design. Dan Sayers' only GitHub repo is unrelated to fonts, and extensive searching across GitHub and Google yields no source repository for any of the Averia family variants. This font likely has no traditional "upstream repository" with source files.

## Open Questions

- Does Dan Sayers maintain any source files (e.g., the averaging scripts or intermediate files) that could serve as an upstream source? His contact email is i@iotic.com.
- The website http://iotic.com/averia/ may contain additional information about the source process, but it was not directly checked in this investigation.
- All four Averia Libre families (Serif, Sans, Gruesa, and base Libre) share this same situation and would benefit from a coordinated approach.
