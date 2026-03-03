# Investigation: Berkshire Swash

## Summary

| Field | Value |
|-------|-------|
| Family Name | Berkshire Swash |
| Slug | berkshire-swash |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/berkshireswash |
| Commit Hash | 1a4fb49d514e01ada8934472cae85cc4590efa58 |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/berkshireswash"
  commit: "1a4fb49d514e01ada8934472cae85cc4590efa58"
}
```

## Investigation

Berkshire Swash was originally added to google/fonts in an early commit `90abd17b4` ("Initial commit"), and later updated in commit `5e3cf0753` via PR #855 ("hotfix-berkshireswash: v1.001 added", 2017-08-07, by Marc Foley). PR #855 had an empty body with no additional context.

The upstream repository `https://github.com/librefonts/berkshireswash` is a librefonts mirror maintained by Marc Foley, containing decompiled font sources. The commit hash `1a4fb49d514e01ada8934472cae85cc4590efa58` is the HEAD (and latest) commit of the repo, titled "update .travis.yml", dated 2014-10-17. It is the final of 10 commits in the repository. The repo has not been updated since 2014, predating the 2017 hotfix by approximately 3 years.

The repository contains only:
- **VFB sources**: `src/BerkshireSwash-Regular-OTF.vfb`, `src/BerkshireSwash-Regular-TTF.vfb`, `src/BerkshireSwash-Regular.vfb` — proprietary FontLab Studio binary format
- **TTX-decomposed font files**: XML dumps of the compiled font tables

VFB (FontLab Studio) is a proprietary binary format that is not compatible with gftools-builder. There are no UFO, Glyphs, or DesignSpace source files. No `config.yaml` exists in the repo at any commit, and no override config.yaml exists in the google/fonts family directory.

The original designer is Brian J. Bonislawsky (Astigmatic/AOETI). The librefonts repo is not the original design source — it is a mirror of decompiled font data. There is no known modern open source format (UFO, Glyphs) available for this font.

The confidence for the commit hash is MEDIUM because the recorded hash is simply the HEAD of the librefonts repo, not explicitly tied to the onboarding event. The hotfix in 2017 was made by Marc Foley (the librefonts maintainer), suggesting the font was built from these VFB sources, but the librefonts repo was not updated after 2014.

The repo is cached at `upstream_repos/fontc_crater_cache/librefonts/berkshireswash`.

## Conclusion

Status is `no_config_possible`. The upstream repository contains only proprietary VFB sources and TTX files, which cannot be processed by gftools-builder. A config.yaml cannot be created without first converting the sources to an open format (UFO or Glyphs). This would require either access to the original designer (Brian J. Bonislawsky, Astigmatic) or an updated source from the designer. No action is feasible without new source files.
