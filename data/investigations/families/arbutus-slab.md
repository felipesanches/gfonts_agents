# Investigation: Arbutus Slab

## Summary

| Field | Value |
|-------|-------|
| Family Name | Arbutus Slab |
| Slug | arbutus-slab |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/arbutusslab |
| Commit Hash | 2988f79c4d6965ef9fa35768ca00f02cddd5a50a |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/arbutusslab"
  commit: "2988f79c4d6965ef9fa35768ca00f02cddd5a50a"
}
```

## Investigation

### Repository

The upstream repository `librefonts/arbutusslab` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/arbutusslab`. The repository URL is pre-existing in METADATA.pb.

### Commit Hash

The commit `2988f79c4d6965ef9fa35768ca00f02cddd5a50a` was verified present in the cached repo: `git cat-file -t 2988f79c` returns `commit`. The commit is dated 2014-10-17 with message "update .travis.yml" by author hash3g — this is the HEAD and most recent commit in the repository.

The google/fonts TTF was last updated in commit `dbe413530` ("hotfix-arbutusslab: v1.002 added (#820)") on 2017-08-07. No upstream commit hash is referenced in the commit body.

### Source Files

Inspection of `src/` in the cached repo reveals:
- `ArbutusSlab-Regular.vfb` — FontLab binary
- `ArbutusSlab-Regular.ttf.sfd` — FontForge SFD format (exported from TTF)
- `ArbutusSlab-Regular.otf.sfd` — FontForge SFD format (exported from OTF)
- `ArbutusSlab-Regular.otf.*` — exported TTX table files

The `.sfd` files are FontForge format, which is not supported by gftools-builder. The `.vfb` file is FontLab binary, also not supported.

### Config YAML

No config.yaml exists. Because the only buildable sources are `.sfd` (FontForge), which gftools-builder does not support, no config.yaml can be created.

## Conclusion

The METADATA.pb source block exists with repository URL and commit hash. Status is `missing_config` because the upstream contains only SFD (FontForge) and VFB (FontLab) sources, neither of which is supported by gftools-builder. No config.yaml is possible for this family.
