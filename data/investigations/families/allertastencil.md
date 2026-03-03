# Investigation: Allerta Stencil

## Summary

| Field | Value |
|-------|-------|
| Family Name | Allerta Stencil |
| Slug | allerta-stencil |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/allerta |
| Commit Hash | 88a8c57b949cb8224f24815d5d3aa05d4950de69 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/allerta"
  commit: "88a8c57b949cb8224f24815d5d3aa05d4950de69"
}
```

## Investigation

### google/fonts commit history

The TTF file was last modified in the "Initial commit" (`90abd17b4f97671435798b6147b698aa9087612f`, dated 2015-03-07, by Dave Crossland). This initial commit added `AllertaStencil-Regular.ttf`, `DESCRIPTION.en_us.html`, `METADATA.json`, and `OFL.txt`. No PR reference is in the commit message.

The `source {}` block was added later, in commit `3f73c2eb035060c81777a3f950586bb7cdaf6cff` (authored by Felipe Sanches, dated 2026-02-26), along with `upstream_info.md`. This was part of PR #10271 to document upstream source metadata.

### Upstream repository

The upstream repo `https://github.com/librefonts/allerta` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/allerta/`. The repository has only a single commit:

- `88a8c57b949c` — "update .travis.yml" (2014-10-17, by hash3g)

This matches exactly the commit recorded in METADATA.pb.

Note: The repository name is `allerta` (not `allertastencil`). This same repo hosts sources for both the Allerta and Allerta Stencil families. The `src/` directory contains:
- `AllertaStencil-Regular.sfd` — FontForge source for Allerta Stencil
- `AllertaStencil-Regular-TTF.sfd` — FontForge source (TTF variant)
- `Allerta-Regular.sfd` and `Allerta-Regular-TTF.sfd` — FontForge sources for Allerta
- `Allerta-Regular.vfb` — FontLab source for Allerta
- Various `.ttx` files (decomposed binary data)

### Source file types and config.yaml status

The Allerta Stencil source files in this repo are `.sfd` (FontForge) format only. FontForge SFD files are **not compatible with gftools-builder**. No `config.yaml` exists in the repository. No override `config.yaml` has been added to the google/fonts family directory.

## Conclusion

The `source {}` block in METADATA.pb is complete with correct `repository_url` and `commit` (both verified). No `config.yaml` can be provided because the upstream sources are in FontForge (.sfd) format, which gftools-builder cannot process. Status remains `missing_config`. No further action is possible without source format conversion.
