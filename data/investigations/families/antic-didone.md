# Investigation: Antic Didone

## Summary

| Field | Value |
|-------|-------|
| Family Name | Antic Didone |
| Slug | antic-didone |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/anticdidone |
| Commit Hash | 604bfcda35327f03964cc6c55a281540ce40b0a0 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/anticdidone"
  commit: "604bfcda35327f03964cc6c55a281540ce40b0a0"
}
```

## Investigation

### Repository

The upstream repository `librefonts/anticdidone` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/anticdidone`. The repository URL is pre-existing in METADATA.pb.

### Commit Hash

The commit `604bfcda35327f03964cc6c55a281540ce40b0a0` was verified present in the cached repo: `git cat-file -t 604bfcda` returns `commit`. It is dated 2014-10-17 with message "update .travis.yml" by author hash3g — this is the HEAD of the repository (the most recent and only commit listed in `git log`).

The google/fonts TTF was last updated in commit `64099f31b` ("hotfix-anticdidone: v2.001 added (#817)") on 2017-08-07. No upstream commit hash appears in the commit body.

### Source Files

Inspection of `src/` in the cached repo reveals:
- `AnticDidone-Regular.vfb` — FontLab binary
- `AnticDidone-Regular-OTF.vfb` — FontLab binary
- `AnticDidone-Regular-TTF.sfd` — FontForge SFD format
- `AnticDidone-Regular.otf.*` — exported TTX table files

The `.sfd` file is FontForge format, which is not supported by gftools-builder. The `.vfb` files are FontLab binary, also not supported.

### Config YAML

No config.yaml exists. Because the only buildable sources are `.sfd` (FontForge), which gftools-builder does not support, no config.yaml can be created.

## Conclusion

The METADATA.pb source block exists with repository URL and commit hash. Status is `missing_config` because the upstream contains only SFD (FontForge) and VFB (FontLab) sources, neither of which is supported by gftools-builder. No config.yaml is possible for this family.
