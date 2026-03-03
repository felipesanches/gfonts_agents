# Investigation: Almendra SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Almendra SC |
| Slug | almendra-sc |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/almendrasc |
| Commit Hash | 35906cd6a26df27bef8081669638fbae0382c7fc |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/almendrasc"
  commit: "35906cd6a26df27bef8081669638fbae0382c7fc"
}
```

## Investigation

### google/fonts commit history

The most recent modification to the TTF files was commit `c5730ef6c912f2466b8f57ea937c4e8c94e7d745`, dated 2017-08-07, authored by Marc Foley with message "hotfix-almendrasc: v1.002 added (#758)". This PR updated `AlmendraSC-Regular.ttf`, removed Bold, BoldItalic, and Italic variants from the catalog, and updated METADATA.pb.

The `source {}` block was added later, in commit `5f69e9bffcf2bc95abc6d19871a7e2e6d2666edb` (authored by Felipe Sanches, dated 2026-02-26), along with `upstream_info.md`. This was part of PR #10271 to document upstream source metadata.

### Upstream repository

The upstream repo `https://github.com/librefonts/almendrasc` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/almendrasc/`. The repository has only a single commit:

- `35906cd6a26d` — "update .travis.yml" (2014-10-17, by hash3g)

This matches exactly the commit recorded in METADATA.pb.

### Source file types and config.yaml status

The `src/` directory contains (for 4 styles):
- `AlmendraSC-Regular-TTF.sfd` — FontForge source (TTF variant)
- `AlmendraSC-Bold-TTF.sfd` — FontForge source (Bold TTF variant)
- `AlmendraSC-BoldItalic-TTF.sfd` — FontForge source (BoldItalic TTF variant)
- `AlmendraSC-Regular-OTF.vfb`, `AlmendraSC-Bold-OTF.vfb`, `AlmendraSC-BoldItalic-OTF.vfb` — FontLab sources
- Various `.ttx` and original `.otf` files

Note: The current google/fonts directory only ships `AlmendraSC-Regular.ttf`. The Bold, BoldItalic, and Italic variants were removed in the 2017 hotfix commit (#758).

The primary buildable sources are `.sfd` (FontForge) format. FontForge SFD files are **not compatible with gftools-builder**. The `.vfb` files are also not compatible. No `config.yaml` exists in the repository. No override `config.yaml` has been added to the google/fonts family directory `ofl/almendrasc/`.

Designer: Ana Sanfelippo (anasanfe@gmail.com).

## Conclusion

The `source {}` block in METADATA.pb is complete with correct `repository_url` and `commit` (both verified). No `config.yaml` can be provided because the upstream sources are in FontForge (.sfd) format, which gftools-builder cannot process. Status remains `missing_config`. No further action is possible without source format conversion by the original designer (Ana Sanfelippo).
