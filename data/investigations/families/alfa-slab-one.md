# Investigation: Alfa Slab One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alfa Slab One |
| Slug | alfa-slab-one |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/alfaslabone |
| Commit Hash | 84a903ffba3cf8248f3b1662de782e72646e00df |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/alfaslabone"
  commit: "84a903ffba3cf8248f3b1662de782e72646e00df"
}
```

## Investigation

### google/fonts commit history

The most recent modification to the TTF file was commit `fb839dd24542f8f1b0678af6f74335553ee8e61a`, dated 2016-12-01, authored by Marc Foley with message "alfaslabone: v2.000 added (#455)". This PR updated the font binary, the FONTLOG.txt, OFL.txt, and METADATA.pb.

The `source {}` block (with `repository_url` and `commit`) was added separately in commit `ae38321d5a5ff3a2125357402dd332998e6bf41b` (authored by Felipe Sanches, dated 2026-02-26), along with `upstream_info.md`. This was part of PR #10271 to document upstream source metadata.

### Upstream repository

The upstream repo `https://github.com/librefonts/alfaslabone` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/alfaslabone/`. The repository has only a single commit:

- `84a903ffba3c` — "update .travis.yml" (2014-10-17, by hash3g)

This matches exactly the commit recorded in METADATA.pb.

### Source file types

The repo's `src/` directory contains:
- `AlfaSlabOne-Regular.vfb` — FontLab source
- `AlfaSlabOne-Regular-OTF.vfb` — FontLab source (OTF variant)
- `AlfaSlabOne-Regular-TTF.vfb` — FontLab source (TTF variant)
- Numerous `.ttx` files (decomposed binary data, not editable sources)

The only source files present are `.vfb` (FontLab proprietary format), which are **not compatible with gftools-builder**. There is no `.glyphs`, `.ufo`, `.designspace`, or `.sfd` file. No `config.yaml` exists in the repository.

### Config YAML status

No `config.yaml` present in the upstream repo. No override `config.yaml` in the google/fonts family directory `ofl/alfaslabone/`. Since the sources are in proprietary FontLab (.vfb) format, gftools-builder compilation is not possible without source format conversion.

## Conclusion

The `source {}` block in METADATA.pb is complete with correct `repository_url` and `commit`. No `config.yaml` can be provided because the upstream sources are in proprietary FontLab (.vfb) format, which gftools-builder cannot process. Status is `missing_config`. No further action is possible without source format conversion by the original designer (JM Solé).
