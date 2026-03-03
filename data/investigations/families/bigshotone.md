# Investigation: Bigshot One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bigshot One |
| Slug | bigshot-one |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/bigshotone |
| Commit Hash | b8d1fa459ee9a43fbe1d7fd07b570878206bd6d5 |
| Config YAML | none (no config.yaml in repo; UFO source present but no config) |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/bigshotone"
  commit: "b8d1fa459ee9a43fbe1d7fd07b570878206bd6d5"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/librefonts/bigshotone` is already documented in METADATA.pb. The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/bigshotone`.

### Commit Hash

The METADATA.pb records commit `b8d1fa459ee9a43fbe1d7fd07b570878206bd6d5`. The upstream repo shows:

```
b8d1fa4 update .travis.yml
```

This is a shallow clone with one visible commit. The commit `b8d1fa4` matches the hash in METADATA.pb. The font was last updated in google/fonts via commit `c49ea1306` ("hotfix-bigshotone: v1.001 added (#857)") dated 2017-08-07.

### Source Files

The upstream repo contains a mix of source formats in `src/`:

- `src/BigshotOne.ufo/` — UFO format (gftools-compatible)
- `src/BigshotOne-TTF.sfd` — FontForge SFD format
- `src/BigshotOne-TTF.vfb` — FontLab VFB format
- `src/BigshotOne.vfb` — FontLab VFB format
- Various TTX decomposition files and OTF TTX files

A UFO source file is present (`BigshotOne.ufo`), which is supported by gftools-builder. However, there is no `config.yaml` in the repository to configure the build.

### Config YAML

No `config.yaml` exists in the upstream repo and no override exists in the google/fonts family directory. While the UFO source could be used with gftools-builder, no configuration file is present.

## Conclusion

The source block in METADATA.pb has repository URL and commit hash. A UFO source file exists in the upstream repo that could potentially be built with gftools-builder, but no `config.yaml` is present to configure the build. Status is `missing_config`. An override `config.yaml` could be created in the google/fonts family directory to enable building from `src/BigshotOne.ufo`.
