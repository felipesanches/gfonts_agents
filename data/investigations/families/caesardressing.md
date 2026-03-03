# Investigation: Caesar Dressing

## Summary

| Field | Value |
|-------|-------|
| Family Name | Caesar Dressing |
| Slug | caesar-dressing |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/caesardressing |
| Commit Hash | fb212a606bc3f65a2b3d210c88e938f6090cff15 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/caesardressing"
  commit: "fb212a606bc3f65a2b3d210c88e938f6090cff15"
}
```

## Investigation

The source block was added to METADATA.pb in google/fonts commit `b4c724343` ("Caesar Dressing: add source block to METADATA.pb", Felipe Sanches, 2026-02-26). The commit metadata records: "Config: none (VFB-only sources), Status: missing_config, Confidence: HIGH".

The upstream repository URL `https://github.com/librefonts/caesardressing` is from the `librefonts` GitHub organization, which hosts archived copies of early Google Fonts source projects. The repository is cached at `upstream_repos/fontc_crater_cache/librefonts/caesardressing/`.

The commit `fb212a606bc3f65a2b3d210c88e938f6090cff15` is the **only commit** in the repository (message: "update .travis.yml", by hash3g, 2014-10-17). Since there is only one commit, the identification is trivially unambiguous.

Caesar Dressing was part of the initial commit (`90abd17b4`) in the google/fonts repository, making it one of the earliest families. The librefonts repository is an archive of the original source material.

The source files in the repository are:
- `src/CaesarDressing-Regular-TTF.vfb` (FontLab VFB format)
- TTX decompositions of the font tables in the root directory
- Standard metadata files (DESCRIPTION, FONTLOG, OFL, METADATA.json)

VFB is a proprietary binary format from FontLab 5 that is not compatible with gftools-builder. No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory.

## Conclusion

The source metadata (repository_url and commit) is present and correct in METADATA.pb. The status is `missing_config` because only a VFB source file exists, which cannot be built with gftools-builder. No override config.yaml is possible without first converting the sources to a gftools-compatible format (`.glyphs`, `.ufo`, or `.designspace`). No further action needed unless source conversion is planned.
