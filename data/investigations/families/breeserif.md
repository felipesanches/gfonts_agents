# Investigation: Bree Serif

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bree Serif |
| Slug | bree-serif |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/breeserif |
| Commit Hash | 86684a17aaa88ce2d9d85d77f9e9ce1f64c06462 |
| Config YAML | none (SFD-only sources) |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/breeserif"
  commit: "86684a17aaa88ce2d9d85d77f9e9ce1f64c06462"
}
```

## Investigation

### Git History in google/fonts

The font has three commits in google/fonts:

1. `faaf4889d` — `hotfix-breeserif: v1.002 added (#866)`
2. `ff120e059` — `Updating ofl/breeserif/*ttf with nbspace and fsType fixes`
3. `90abd17b4` — `Initial commit`

The hotfix commit from PR #866 is the last meaningful update to the TTF files. Its commit message is minimal and does not include upstream repo/commit references. The family was added in the initial commit of the google/fonts repository, predating the gftools-packager workflow.

A separate commit `324bd0aa8` added the source block to METADATA.pb:

> Bree Serif: add source block to METADATA.pb
> - Repo: librefonts/breeserif
> - Commit: 86684a17 (only commit in repo)
> - Config: none (SFD-only sources)
> - Status: missing_config
> - Confidence: HIGH

### Upstream Repository

The repo is cached at `upstream_repos/fontc_crater_cache/librefonts/breeserif`. It contains only a single commit: `86684a17aaa88ce2d9d85d77f9e9ce1f64c06462` ("update .travis.yml", authored 2014-10-17 by hash3g).

The repository's source files are:
- `src/BreeSerif-Regular-TTF.sfd` — FontForge SFD format
- `src/BreeSerif-Regular-OTF.vfb` — FontForge VFB format
- A collection of `.ttx` decomposed font table files

These are legacy FontForge formats (SFD/VFB) that are **not compatible with gftools-builder**. No `.glyphs`, `.ufo`, or `.designspace` files are present.

### Config YAML Status

No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts `ofl/breeserif/` directory. Because the sources are in SFD/VFB format only, a valid gftools-builder `config.yaml` cannot be created. The family is correctly marked `missing_config`.

### METADATA.pb Status

The source block was added to METADATA.pb (commit `324bd0aa8` on google/fonts main) with:
- `repository_url` set correctly
- `commit` set to `86684a17...` (the only commit in the upstream repo — unambiguous)
- No `config_yaml` field (correct, since no gftools-builder config is possible)

## Conclusion

No further action needed for source metadata. The source block is complete and correct for what can be documented. The `missing_config` status reflects that the upstream sources are in legacy FontForge format and cannot be rebuilt with gftools-builder. TypeTogether (the designers) may hold more recent Glyphs/UFO sources, but they are not publicly available.
