# Investigation: Bacasime Antique

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bacasime Antique |
| Slug | bacasime-antique |
| License Dir | ofl |
| Repository URL | https://github.com/docrepair-fonts/bacasime-antique-fonts |
| Commit Hash | 673db74ee28486bb370847e062a97a5f94cec2e0 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/docrepair-fonts/bacasime-antique-fonts"
  commit: "673db74ee28486bb370847e062a97a5f94cec2e0"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/BacasimeAntique-Regular.ttf"
    dest_file: "BacasimeAntique-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Git History in google/fonts

The TTF files have a single commit:

- `068ca5cdc` — "[gftools-packager] Bacasime Antique: Version 2.000 added" (2023-06-14)

The commit message says:

> Bacasime Antique Version 2.000 taken from the upstream repo
> https://github.com/docrepair-fonts/bacasime-antique-fonts at commit
> https://github.com/docrepair-fonts/bacasime-antique-fonts/commit/673db74ee28486bb370847e062a97a5f94cec2e0

This matches exactly what is recorded in METADATA.pb.

### Commit Verification

Inspecting the upstream repo at `/mnt/shared/upstream_repos/fontc_crater_cache/docrepair-fonts/bacasime-antique-fonts`:

- Commit `673db74ee28486bb370847e062a97a5f94cec2e0` (2023-06-14) — "Merge branch 'main' of https://github.com/docrepair-fonts/bacasime-antique-fonts"

The commit is confirmed present in the cache and the date matches the google/fonts onboarding date.

### Config YAML Verification

The `config.yaml` at `sources/config.yaml` in the upstream repo contains:

```yaml
buildOTF: false
buildVariable: false
familyName: Bacasime Antique
outputDir: ../fonts
sources:
  - Bacasime-Antique-Regular.designspace
```

This is a valid gftools-builder configuration. The `config_yaml: "sources/config.yaml"` field in METADATA.pb correctly references this file.

### Repository Cache

The upstream repo is cached at:
`/mnt/shared/upstream_repos/fontc_crater_cache/docrepair-fonts/bacasime-antique-fonts`

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path are all verified. No action required.
