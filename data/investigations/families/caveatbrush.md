# Investigation Report: Caveat Brush

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Caveat Brush |
| **Designer** | Impallari Type |
| **License** | OFL |
| **Date Added** | 2015-09-23 |
| **Repository URL** | https://github.com/googlefonts/caveat |
| **Commit Hash** | `7fb0cea12be06c90398d7a6f35eafd4118d40825` (INCORRECT - see below) |
| **Branch** | N/A |
| **Config YAML** | N/A |
| **Status** | missing_config |

## How URL Was Found

The repository URL `https://github.com/googlefonts/caveat` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)") in January 2024. Caveat Brush shares its upstream repo with the Caveat family, as both fonts were created by the same designer (Pablo Impallari).

## How Commit Was Determined

**The current commit hash `7fb0cea12be06c90398d7a6f35eafd4118d40825` is INCORRECT.** This commit was added by our automated enrichment work (commit `9a14639f3` in google/fonts). However, investigation reveals this commit is the very first commit in the caveat repository, dated 2015-10-07, and contains only a README.md file:

```
7fb0cea12be06c90398d7a6f35eafd4118d40825 2015-10-07 README: Detail web fonts usage
```

At this commit, there were no source files at all - just a README. The Caveat Brush binary was added to google/fonts by Dave Crossland on 2015-09-18 (commit `b05d7ed92`), which actually predates the first commit in the caveat repo.

### Original Onboarding History

1. **2015-09-18**: Caveat Brush binary added to google/fonts by Dave Crossland (`b05d7ed92`). The font was compiled from a VFB source file outside of the current GitHub repo.
2. **2015-10-07**: First commit in googlefonts/caveat repo - only a README.md (`7fb0cea`).
3. **2017-09-01**: Marc Foley added a .glyphs conversion of Caveat Brush source to the repo (`527fdc2`), noting it was "Source provided by @davelab6". However, the same day a README note was added (`09182d3`) stating: **"Sources for Caveat Brush are not the latest. Source is kept in sources/wip until it is located."**
4. **2020-08-21**: The Caveat-Brush.glyphs file was moved from `source glyphs/wip/` to `sources/` by Denis Moyogo Jacquerye (`38fd0ee`).

The Caveat Brush binary in google/fonts was never updated after the initial add. It has never been rebuilt from the upstream repo.

## Config YAML Status

**No config.yaml exists for Caveat Brush.** The upstream repo's config.yaml (if one were created) would need to handle both Caveat and Caveat Brush as separate families, or separate configs would be needed. Currently, the repo has no config.yaml at all.

The Caveat-Brush.glyphs file exists in `sources/` at HEAD, but as noted above, it may not match the binary on Google Fonts.

**No override config.yaml** exists in `/mnt/shared/google/fonts/ofl/caveatbrush/`.

## Verification

- **Repository accessible**: Yes, cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/caveat/`
- **Commit hash is WRONG**: The tracked commit `7fb0cea` only contained a README.md - no source files at all
- **Binary was never rebuilt**: The CaveatBrush-Regular.ttf was added in the initial commit and only touched by the large deploy restructure
- **Source mismatch acknowledged**: The upstream repo README explicitly notes that Caveat Brush sources are "not the latest"
- **Copyright discrepancy**: METADATA.pb says "Copyright 2015 Google Inc." while the Caveat family says "Copyright 2014 The Caveat Project Authors"

## Confidence Level

**LOW for commit hash** - The current commit hash is definitively incorrect. The font binary predates the upstream repo entirely. There is no correct commit to reference since the font was compiled from sources outside the repo.

**MEDIUM for repository URL** - The repo does contain Caveat Brush source files (Caveat-Brush.glyphs), but these were added later and are acknowledged as not matching the Google Fonts binary.

## Open Questions

1. **The commit hash should be removed or corrected.** Since no commit in the caveat repo corresponds to the binary on Google Fonts, the commit field should either be cleared or set to a commit where the .glyphs source exists (though that source may not match the binary).
2. **Where is the original VFB source?** The original Caveat Brush binary was compiled from a VFB file provided by Dave Crossland. This source may not be available in any public repository.
3. **Should Caveat Brush be rebuilt?** If the font were to be rebuilt from the existing Caveat-Brush.glyphs source, it would be a new version that may differ from the current binary. This would require proper QA review.
