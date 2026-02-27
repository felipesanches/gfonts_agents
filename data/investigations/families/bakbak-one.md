# Investigation: Bakbak One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bakbak One |
| Slug | bakbak-one |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/bakbak |
| Commit Hash | b53b9c31c16f0021b7c206a57a8f04a4d382bc67 |
| Config YAML | sources/builder.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/bakbak"
  commit: "b53b9c31c16f0021b7c206a57a8f04a4d382bc67"
  files {
    source_file: "fonts/ttf/BakbakOne-Regular.ttf"
    dest_file: "BakbakOne-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
  config_yaml: "sources/builder.yaml"
}
```

## Investigation

### Git History in google/fonts

The TTF files have two commits:

- `10e8b3d30` — "Bakbak Version 1.003 (#4176)" (most recent) — commit message: "Version 1.003" + "Update METADATA.pb"
- `338bebe14` — "Bakbak One: Version 1.002; ttfautohint (v1.8.3) added (#3810)"

The 1.002 onboarding commit (`338bebe14`) says:

> Bakbak One Version 1.002; ttfautohint (v1.8.3) taken from the upstream repo
> https://github.com/googlefonts/bakbak.git at commit
> https://github.com/googlefonts/bakbak/commit/8308b62b527659d7be4a2890c5f07e2d1db1496b.

The METADATA.pb records `b53b9c31c16f0021b7c206a57a8f04a4d382bc67`, which is the commit used for the 1.003 update (the most recent version in google/fonts). The 1.003 PR (#4176) updated the METADATA.pb to reflect the new upstream commit.

### Commit Verification

Inspecting the upstream repo at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/bakbak`:

- Commit `b53b9c31c16f0021b7c206a57a8f04a4d382bc67` (2021-12-16) — "Added fractions" — confirmed present in the cache.

The local cache has only this single commit (shallow or single-commit history), but the commit itself is verified to exist.

### Config YAML Verification

The `builder.yaml` at `sources/builder.yaml` in the upstream repo contains:

```yaml
sources:
  - Bakbak.glyphs
familyName: "Bakbak One"
buildTTF: true
buildOTF: false
buildWebfont: false
buildVariable: false
```

This is a valid gftools-builder configuration (note: named `builder.yaml` rather than `config.yaml`, which is an accepted variant). The `config_yaml: "sources/builder.yaml"` field in METADATA.pb correctly references this file.

### Repository Cache

The upstream repo is cached at:
`/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/bakbak`

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path (pointing to `sources/builder.yaml`) are all verified. No action required.
