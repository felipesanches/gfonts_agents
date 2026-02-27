# Investigation: Autour One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Autour One |
| Slug | autour-one |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/autourone |
| Commit Hash | 10ccd1eb5ad3e7088ce2dd099debff0ac08daf1c |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/autourone"
  commit: "10ccd1eb5ad3e7088ce2dd099debff0ac08daf1c"
}
```

## Investigation

Autour One is a display font by Sorkin Type, added to Google Fonts on 2012-05-15. The font was last updated via PR #833 (`592bee48b`, "hotfix-autourone: v1.007 added", 2017-08-07) by Marc Foley. The source block in METADATA.pb was added by commit `42e01ed7f` ("Autour One: add source block to METADATA.pb", 2026-02-26), which populated the repository_url and commit from research into the librefonts archive.

The upstream repository `librefonts/autourone` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/autourone`. The repo has a single commit: `10ccd1eb5ad3e7088ce2dd099debff0ac08daf1c` (dated 2014-10-17, "update .travis.yml"). Since it is the only commit, it is the only possible reference point.

**Source file format**: The repository contains:
- `src/AutourOne-Regular-OTF.sfd` (FontForge SFD)
- `src/AutourOne-Regular-TTF.sfd` (FontForge SFD)
- `src/AutourOne-Regular.vfb` (FontLab binary)
- Multiple TTX (decompiled font table) XML files

None of these formats are compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No `config.yaml` exists in the repository or in the google/fonts family directory (`ofl/autourone/`).

The librefonts organization is a GitHub mirror of early Google Fonts families. The v1.007 hotfix in google/fonts (2017) was made 3 years after the last upstream commit (2014), suggesting binary modifications were done independently.

## Conclusion

Repository URL and commit hash are documented in METADATA.pb. No config.yaml is possible without source conversion: the only available sources are SFD (FontForge) and VFB (FontLab) files not compatible with gftools-builder. Status remains missing_config. An investigation into whether Eben Sorkin (Sorkin Type) maintains a separate, more modern source repository for Autour One may be warranted.
