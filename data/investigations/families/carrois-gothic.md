# Investigation: Carrois Gothic

## Summary

| Field | Value |
|-------|-------|
| Family Name | Carrois Gothic |
| Slug | carrois-gothic |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/carroisgothic |
| Commit Hash | 09bb67138894e329544a6a1e1ebf0ff516f82a0e |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/carroisgothic"
  commit: "09bb67138894e329544a6a1e1ebf0ff516f82a0e"
}
```

## Investigation

The source block was added to METADATA.pb in google/fonts commit `9c6064a3c` ("Carrois Gothic: add source block to METADATA.pb", Felipe Sanches, 2026-02-26). The commit metadata records: "Config: none (SFD-only sources), Status: missing_config, Confidence: HIGH".

The upstream repository URL `https://github.com/librefonts/carroisgothic` is from the `librefonts` GitHub organization, which hosts archived copies of early Google Fonts source projects. The repository is cached at `upstream_repos/fontc_crater_cache/librefonts/carroisgothic/`.

The commit `09bb67138894e329544a6a1e1ebf0ff516f82a0e` is the **only commit** in the repository (message: "update .travis.yml", by hash3g, 2014-10-17). Since there is only one commit, the identification is trivially unambiguous.

Carrois Gothic was part of the initial commit (`90abd17b4`) in the google/fonts repository. A hotfix was later applied in commit `29cf1c494` (PR #874, Marc Foley, 2017-05-08), updating the TTF from v1.001 to v1.002. The upstream librefonts repo was never updated to reflect this.

The source files in the repository are:
- `src/CarroisGothic-Regular.vfb`
- `src/CarroisGothic-Regular-OTF.vfb`
- `src/CarroisGothic-Regular-TTF.vfb`

All are in VFB (FontLab Studio proprietary binary format), which is not supported by gftools-builder. No SFD, Glyphs, UFO, or Designspace files are present. No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory.

## Conclusion

The source metadata (repository_url and commit) is present and correct in METADATA.pb. The status is `missing_config` because only VFB source files exist, which cannot be used with gftools-builder. The current binary in google/fonts (v1.002 from PR #874) may not match what could be built from the archived VFB sources. No override config.yaml is possible without first converting the sources to a gftools-compatible format. No further action needed unless source conversion is planned.
