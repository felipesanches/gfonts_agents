# Investigation: Architects Daughter

## Summary

| Field | Value |
|-------|-------|
| Family Name | Architects Daughter |
| Slug | architects-daughter |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/architectsdaughter |
| Commit Hash | 1a94ca0aea18288ee7685ed6aee918b58399a307 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/architectsdaughter"
  commit: "1a94ca0aea18288ee7685ed6aee918b58399a307"
}
```

## Investigation

### Repository

The upstream repository `librefonts/architectsdaughter` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/architectsdaughter`. The repository URL is pre-existing in METADATA.pb.

### Commit Hash

The commit `1a94ca0aea18288ee7685ed6aee918b58399a307` was verified present in the cached repo: `git cat-file -t 1a94ca0a` returns `commit`. The commit is dated 2014-10-17 with message "update .travis.yml" by author hash3g — this is the HEAD of the repository.

The google/fonts TTF was last updated in commit `2a0c94b33` ("hotfix-architectsdaughter: v1.003 added (#821)") on 2017-08-07. No upstream commit hash or PR reference appears in the commit body.

### Source Files

Inspection of `src/` in the cached repo reveals:
- `ArchitectsDaughter.vfb` — FontLab binary
- `ArchitectsDaughter-TTF.sfd` — FontForge SFD format

The `.sfd` file is FontForge format, which is not supported by gftools-builder. The `.vfb` file is FontLab binary, also not supported.

### Config YAML

No config.yaml exists. Because the only buildable sources are `.sfd` (FontForge), which gftools-builder does not support, no config.yaml can be created.

## Conclusion

The METADATA.pb source block exists with repository URL and commit hash. Status is `missing_config` because the upstream contains only SFD (FontForge) and VFB (FontLab) sources, neither of which is supported by gftools-builder. No config.yaml is possible for this family.
