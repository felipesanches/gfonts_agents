# Investigation: Alike Angular

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alike Angular |
| Slug | alike-angular |
| License Dir | ofl |
| Repository URL | https://github.com/cyrealtype/Alike-Angular |
| Commit Hash | 20765691758ef999907b9a20950d4f57f62de1d1 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cyrealtype/Alike-Angular"
  commit: "20765691758ef999907b9a20950d4f57f62de1d1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/AlikeAngular-Regular.ttf"
    dest_file: "AlikeAngular-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### google/fonts commit history

The most recent modification to the TTF file was commit `ba0196b69e69614fe6c0e3e88dbec9de1c3c20d9`, dated 2023-11-02, authored by Emma Marichal with message:

> [gftools-packager] Alike Angular: Version 1.300; ttfautohint (v1.8.4.7-5d5b) added
>
> Alike Angular Version 1.300; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/cyrealtype/Alike-Angular at commit https://github.com/cyrealtype/Alike-Angular/commit/20765691758ef999907b9a20950d4f57f62de1d1.

This gftools-packager commit message explicitly records both the repository URL and the exact commit hash. The METADATA.pb `source {}` block was subsequently added in commit `19cdcec59` (via "[Batch 1/4] port info from fontc_crater targets list"), and the `upstream.yaml` was merged into METADATA.pb in commit `66f91f10f`.

### Upstream repository

The upstream repo `https://github.com/cyrealtype/Alike-Angular` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/cyrealtype/Alike-Angular/`. The HEAD commit is:

- `20765691` — "Merge pull request #3 from emmamarichal/main" (2023-11-02, by cyrealtype)

This commit is a merge PR by Emma Marichal that corrected the copyright string (put back RFN). It is also the exact commit referenced in METADATA.pb and in the gftools-packager commit message.

### Source file types and config.yaml

The `sources/` directory contains:
- `AlikeAngular.glyphs` — Glyphs source file
- `config.yaml` — gftools-builder configuration

The `config.yaml` content:
```yaml
sources:
    - AlikeAngular.glyphs
familyName: Alike Angular
```

This is a valid gftools-builder config referencing the `.glyphs` source. The METADATA.pb `config_yaml` field is set to `sources/config.yaml`, which correctly points to this file.

## Conclusion

All source metadata is complete and verified. The METADATA.pb `source {}` block contains the correct `repository_url`, `commit`, `config_yaml`, and `branch`. The upstream commit is confirmed in the cached repo. The `sources/config.yaml` file exists at the referenced commit and references the `.glyphs` source file. No action needed.
