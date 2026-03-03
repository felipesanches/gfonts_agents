# Investigation: Bigelow Rules

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bigelow Rules |
| Slug | bigelow-rules |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/bigelowrules |
| Commit Hash | f3ba7414e96d1a940b935d4fa4d2bab47150c7fc |
| Config YAML | none (VFB/TTX-only sources, not buildable by gftools) |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/bigelowrules"
  commit: "f3ba7414e96d1a940b935d4fa4d2bab47150c7fc"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/librefonts/bigelowrules` is already documented in METADATA.pb. The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/bigelowrules`.

### Commit Hash

The METADATA.pb records commit `f3ba7414e96d1a940b935d4fa4d2bab47150c7fc`. The upstream repo has only one visible commit:

```
f3ba741 update .travis.yml
```

This is a shallow clone. The commit `f3ba741` is the only commit visible in the repo history and matches the hash in METADATA.pb. The font was last updated in google/fonts via commit `4a101fcb7` ("hotfix-bigelowrules: v1.001 added (#856)") dated 2017-08-07.

### Source Files

The upstream repo contains only compiled binary formats: TTX decomposition files (.ttx) and FontLab source files (.vfb):

- `BigelowRules-Regular.ttf.ttx` and related TTX tables (in root)
- `src/BigelowRules-Regular.vfb` (FontLab VFB format)
- `src/BigelowRules-Regular-OTF.vfb`
- `src/BigelowRules-Regular-TTF.vfb`
- `src/BigelowRules-Regular.otf.ttx` and related TTX tables

No `.glyphs`, `.ufo`, or `.designspace` files are present. The VFB format is not supported by gftools-builder. There is no `config.yaml` in the repository.

### Config YAML

No config.yaml exists in the upstream repo and no override exists in the google/fonts family directory. The source format (VFB/TTX) is not compatible with gftools-builder, so no config.yaml is possible without converting the sources to a supported format.

## Conclusion

The source block in METADATA.pb is complete with repository URL and commit hash. No config.yaml is possible because the upstream sources are in VFB format, which is not supported by gftools-builder. Status is `missing_config` due to the lack of buildable sources. No action needed unless sources are converted to a gftools-compatible format.
