# Investigation: Butterfly Kids

## Summary

| Field | Value |
|-------|-------|
| Family Name | Butterfly Kids |
| Slug | butterfly-kids |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/butterflykids |
| Commit Hash | 0c553b23416ad40db0b241d1d0b9165d890933b7 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/butterflykids"
  commit: "0c553b23416ad40db0b241d1d0b9165d890933b7"
}
```

## Investigation

The source block was added to METADATA.pb in google/fonts commit `c9581ea65` ("Butterfly Kids: add source block to METADATA.pb", Felipe Sanches, 2026-02-26). The commit metadata records: "Config: none (VFB-only sources), Status: missing_config, Confidence: MEDIUM".

The upstream repository URL `https://github.com/librefonts/butterflykids` is from the `librefonts` GitHub organization, which hosts archived copies of early Google Fonts source projects. The repository is cached at `upstream_repos/fontc_crater_cache/librefonts/butterflykids/`.

The commit `0c553b23416ad40db0b241d1d0b9165d890933b7` is the **only commit** in the repository (message: "update .travis.yml", by hash3g, 2014-10-17). Since there is only one commit, the identification is trivially unambiguous.

The font binary in google/fonts was last updated via PR #871 ("hotfix-butterflykids: v1.001 added"), authored by m4rc1e and merged on 2017-08-07.

The source file in the repository is:
- `src/ButterflyKids-Regular-TTF.vfb` (FontLab VFB format)

VFB is a proprietary binary format from FontLab 5 that is not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory.

## Conclusion

The source metadata (repository_url and commit) is present and correct in METADATA.pb. The status is `missing_config` because only a VFB source file exists, which cannot be built with gftools-builder. No override config.yaml is possible without first converting the sources to a gftools-compatible format. No further action needed unless source conversion is planned.
