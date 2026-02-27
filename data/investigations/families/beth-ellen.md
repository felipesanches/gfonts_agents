# Investigation: Beth Ellen

## Summary

| Field | Value |
|-------|-------|
| Family Name | Beth Ellen |
| Slug | beth-ellen |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/BethEllen |
| Commit Hash | d6c8d9b3871c432c6abfd71660885f16ddbce3e2 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/BethEllen"
  commit: "d6c8d9b3871c432c6abfd71660885f16ddbce3e2"
}
```

## Investigation

The font was added to google/fonts on 2019-05-10 in commit `0aa5f370a` by Felipe Sanches. The commit message reads: "Add Beth Ellen (Version 2.000)" and includes the upstream commit URL `(https://github.com/googlefonts/BethEllen/commit/d6c8d9b3871c432c6abfd71660885f16ddbce3e2)`.

The repository URL `https://github.com/googlefonts/BethEllen` was confirmed by the copyright string in the font metadata: "Copyright 2019 The Beth Ellen Project Authors (https://github.com/googlefonts/BethEllen)".

The upstream commit `d6c8d9b` is verified locally in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/BethEllen`. The commit message is: "manual fixes using gftools and ttx".

The METADATA.pb source block already contains both `repository_url` and `commit` fields. There is no `config_yaml` field, which is correct because no config.yaml exists.

**Config YAML situation**: At the recorded commit `d6c8d9b`, the repository contains:
- `BethEllen-Regular.sfd` (FontForge source)
- `BethEllen-Regular.ttf` (pre-built binary)
- `BethEllen-Story.pdf`, `OFL.txt`, `README.md`
- `old/` and `prebuilt/` directories

The font source is in SFD (FontForge) format, which is not compatible with gftools-builder. No config.yaml exists either at the recorded commit or at HEAD. At HEAD, a `.glyphs` file has been added (`BethEllen-Regular.glyphs`), but still no config.yaml. No override config.yaml exists in the google/fonts family directory.

## Conclusion

The source metadata is partially complete: `repository_url` and `commit` are documented and verified. No `config_yaml` exists because the font source at onboarding was SFD (FontForge format), which is incompatible with gftools-builder. The status is `missing_config`. No further action is feasible without an upstream update adding a config.yaml for the .glyphs file that now exists at HEAD.
