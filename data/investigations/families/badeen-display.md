# Investigation: Badeen Display

## Summary

| Field | Value |
|-------|-------|
| Family Name | Badeen Display |
| Slug | badeen-display |
| License Dir | ofl |
| Repository URL | https://github.com/haniadnansd/Badeen-Display |
| Commit Hash | c1370b602b4a9819c4ddce4af17962a42edb8bc3 |
| Config YAML | source/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/haniadnansd/Badeen-Display"
  commit: "c1370b602b4a9819c4ddce4af17962a42edb8bc3"
  config_yaml: "source/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/BadeenDisplay-Regular.ttf"
    dest_file: "BadeenDisplay-Regular.ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
```

## Investigation

### Git History in google/fonts

The TTF files have a single commit:

- `c31eae585` — "Badeen Display: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" (2024-11-20)

The commit message says:

> Taken from the upstream repo https://github.com/haniadnansd/Badeen-Display at commit
> https://github.com/haniadnansd/Badeen-Display/commit/c1370b602b4a9819c4ddce4af17962a42edb8bc3.
>
> Resolves #7814

This matches exactly what is recorded in METADATA.pb.

### Commit Verification

Inspecting the upstream repo at `/mnt/shared/upstream_repos/fontc_crater_cache/haniadnansd/Badeen-Display`:

- Commit `c1370b602b4a9819c4ddce4af17962a42edb8bc3` (2024-11-14) — "Update DESCRIPTION.en_us.html"

The commit is confirmed present in the cache. The upstream commit date (2024-11-14) predates the google/fonts onboarding date (2024-11-20), which is consistent.

### Config YAML Verification

The `config.yaml` at `source/config.yaml` in the upstream repo contains:

```yaml
sources:
    - BadeenDisplay.glyphs
```

This is a valid gftools-builder configuration. The `config_yaml: "source/config.yaml"` field in METADATA.pb correctly references this file.

### Repository Cache

The upstream repo is cached at:
`/mnt/shared/upstream_repos/fontc_crater_cache/haniadnansd/Badeen-Display`

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path are all verified. No action required.
