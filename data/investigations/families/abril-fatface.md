# Investigation: Abril Fatface

## Summary

| Field | Value |
|-------|-------|
| Family Name | Abril Fatface |
| Slug | abril-fatface |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/abrilfatface |
| Commit Hash | 5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/abrilfatface"
  commit: "5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f"
}
```

## Investigation

### Git History

The TTF files in `ofl/abrilfatface/` have only one commit in google/fonts:

```
90abd17b4 Initial commit
```

This "Initial commit" (dated 2015-03-07) was part of the initial google/fonts repository setup. The font was added to Google Fonts on 2011-08-31 per METADATA.pb `date_added`, predating the current google/fonts git history.

### Source Block Status

The METADATA.pb currently has a `source {}` block with `repository_url` and `commit` fields. The upstream repo (`librefonts/abrilfatface`) is cloned at `upstream_repos/fontc_crater_cache/librefonts/abrilfatface/`.

### Upstream Repository

The `librefonts/abrilfatface` repository on GitHub is a legacy TTX-decomposed mirror created by Dave Crossland. It contains:
- `src/AbrilFatface-Regular-TTF.sfd` (FontForge SFD format)
- `src/AbrilFatface-Regular.vfb` (FontLab VFB format)
- `src/AbrilFatface-Regular.ttf.*.ttx` (TTX decomposed TTF tables)
- `src/AbrilFatface-Regular.otf.*.ttx` (TTX decomposed OTF tables)
- `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt`

This is **not** the original design source repository. TypeTogether (the credited designer) created the font, and `librefonts/abrilfatface` is an archival/reproducibility mirror created years after the original font production.

### Commit Verification

The upstream repo has exactly one commit: `5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f` (dated 2014-10-17, message: "update .travis.yml"). This is the only commit and represents the complete state of this single-commit repository. The commit predates the google/fonts Initial commit (2015-03-07) and post-dates the reported `date_added` (2011-08-31).

### Config YAML Assessment

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in `ofl/abrilfatface/` in google/fonts. The source formats available (SFD, VFB, TTX) are **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` sources. A config.yaml cannot be meaningfully created without first converting the sources to a modern format.

## Conclusion

The source block in METADATA.pb is partially complete (repo URL and commit are set). However, no `config_yaml` can be set because the upstream repo only contains legacy source formats (SFD/VFB/TTX) incompatible with gftools-builder. Status is `no_config_possible`. If TypeTogether has modern sources (`.glyphs` or `.ufo`), those would need to be contributed upstream first. No further action is needed for the metadata documentation effort unless modern sources become available.
