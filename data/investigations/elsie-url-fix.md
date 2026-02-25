# Investigation: Elsie / Elsie Swash Caps — Broken repository_url

**Date**: 2026-02-25
**Issue**: gfonts_agents-kn6
**Families**: Elsie, Elsie Swash Caps

## Problem

Elsie's METADATA.pb has `repository_url: "https://github.com/googlefonts/elsiefont (404)"`
— note the "(404)" is literally in the URL field itself, making it invalid.

Elsie Swash Caps has no source block at all.

## Investigation

### Source status

- `https://github.com/googlefonts/elsiefont` → 404 (deleted)
- `https://github.com/googlefonts/elsie` → 200 but **completely empty** (0 commits, 0 files)
- Original sources were on Bitbucket: `bitbucket.org/lassefister/old-googlefontdirectory` → also 404
- Designer Alejandro Inler has no discoverable GitHub account

### google/fonts history

- Originally onboarded in 2012 via PR #884/#885 by m4rc1e as hotfixes
- Most recent fix: PR #7522 by Yanone, who noted: "Reminder: We don't have sources"
- All modifications have been binary-level hotfixes (removing ligatures, bumping versions)

### Sources are lost

This is a case where **original font sources are genuinely lost**. The `googlefonts/elsie`
repo exists as an empty placeholder. The font was created in 2010-2012 and the original
source files (.vfb or .glyphs) are not available in any discoverable repository.

## Decision

**Remove the broken repository_url from METADATA.pb.**

The current value `"https://github.com/googlefonts/elsiefont (404)"` is not a valid URL
and provides no useful information. Options:

1. Remove the source block entirely (since there are no sources)
2. Set `repository_url` to `https://github.com/googlefonts/elsie` (the empty placeholder)

Option 1 is more honest — there are genuinely no sources available.

## Risk

None — the URL is already broken and annotated as such.

## Action

1. Remove the invalid `repository_url` from Elsie's METADATA.pb source block
2. Update tracking in gfonts_library_sources.json to status "no_source" for both
   Elsie and Elsie Swash Caps
