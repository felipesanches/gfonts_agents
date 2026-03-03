# Investigation: Bowlby One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bowlby One |
| Slug | bowlby-one |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/bowlbyone |
| Commit Hash | 3aca9b57cf9c7b9688b635d5dcfb6d53948e26a2 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/bowlbyone"
  commit: "3aca9b57cf9c7b9688b635d5dcfb6d53948e26a2"
}
```

## Investigation

Bowlby One is a display typeface by Vernon Adams, added to Google Fonts on 2011-07-13. It is an archival font with no active upstream development since 2014.

### Git History

The font TTF was last updated in google/fonts commit `5df13fc14` (2017-08-07, "hotfix-bowlbyone: v1.001 added", PR #864 by Marc Foley). Prior to that, commit `efb2eb034` (2015-04-27) applied nbspace and fsType fixes. The initial commit was `90abd17b4`.

The source block was added by google/fonts commit `6e2cc4405` ("Bowlby One: add source block to METADATA.pb"), which documented:
- Repo: librefonts/bowlbyone
- Commit: 3aca9b57
- Config: none (SFD-only sources)
- Status: missing_config
- Confidence: HIGH

### Upstream Repository

The repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/bowlbyone/`. The repository has only 11 commits, all from 2014. Commit `3aca9b57` is the tip of master (2014-10-17, "update .travis.yml").

The upstream repo contains only SFD (FontForge) and VFB (FontLab) source files:
- `src/BowlbyOne-Regular-TTF.sfd`
- `src/BowlbyOne-Regular.vfb`

Neither of these formats is compatible with gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` files present.

The 2017 hotfix (v1.001) was performed by Marc Foley independently without updating the upstream repository. The upstream repo has not been updated since 2014.

### Verification

- Repository URL: Confirmed — `librefonts/bowlbyone` is accessible on GitHub
- Commit hash: Confirmed — `3aca9b57` is the tip of master (2014-10-17, "update .travis.yml")
- Config YAML: Cannot be created (SFD/VFB sources only, not compatible with gftools-builder)
- Source files: SFD and VFB only

## Conclusion

The METADATA.pb source block correctly records the repository URL and commit hash. No config.yaml can be created for this family because the upstream repo contains only SFD and VFB source files that are incompatible with gftools-builder. This family should remain with `status: missing_config` permanently unless the sources are converted to a gftools-builder-compatible format (`.glyphs`, `.ufo`, or `.designspace`). The 2017 v1.001 update by Marc Foley was performed outside the upstream repo with no corresponding source update.
