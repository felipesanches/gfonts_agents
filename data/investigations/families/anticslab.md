# Investigation: Antic Slab

## Summary

| Field | Value |
|-------|-------|
| Family Name | Antic Slab |
| Slug | antic-slab |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/anticslab |
| Commit Hash | 64168753771367673ec5efa56c747427648d9f29 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/anticslab"
  commit: "64168753771367673ec5efa56c747427648d9f29"
}
```

## Investigation

### Repository

The upstream repository `librefonts/anticslab` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/anticslab`. The repository URL is pre-existing in METADATA.pb.

### Commit Hash

The commit `64168753771367673ec5efa56c747427648d9f29` was verified present in the cached repo: `git cat-file -t 64168753` returns `commit`. It is dated 2014-10-17 with message "update .travis.yml" by author hash3g — this is the HEAD and only recent commit in the repository.

The google/fonts TTF was last updated in commit `29d7c65b5` ("hotfix-anticslab: v1.002 added (#818)") on 2017-08-07. No upstream commit hash is referenced in the commit body.

### Source Files

Inspection of `src/` in the cached repo reveals:
- `AnticSlab-Regular.vfb` — FontLab binary
- `AnticSlab-Regular-OTF.vfb` — FontLab binary
- `AnticSlab-Regular-TTF.sfd` — FontForge SFD format
- `AnticSlab-Regular.otf.*` — exported TTX table files

The `.sfd` file is FontForge format, which is not supported by gftools-builder. The `.vfb` files are FontLab binary, also not supported.

### Config YAML

No config.yaml exists. Because the only buildable sources are `.sfd` (FontForge), which gftools-builder does not support, no config.yaml can be created.

## Conclusion

The METADATA.pb source block exists with repository URL and commit hash. Status is `missing_config` because the upstream contains only SFD (FontForge) and VFB (FontLab) sources, neither of which is supported by gftools-builder. No config.yaml is possible for this family.
