# Investigation: Cabin Condensed

## Summary

| Field | Value |
|-------|-------|
| Family Name | Cabin Condensed |
| Slug | cabin-condensed |
| License Dir | ofl |
| Repository URL | https://github.com/impallari/Cabin |
| Commit Hash | 9476ee6f5459ee37cf8462452f3e4640c3a48519 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/impallari/Cabin"
  commit: "9476ee6f5459ee37cf8462452f3e4640c3a48519"
}
```

## Investigation

The repository URL `https://github.com/impallari/Cabin` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)", 2024-01-14). Both Cabin and Cabin Condensed share the same upstream repository, as they are generated from the same Glyphs source files.

The commit hash `9476ee6f5459ee37cf8462452f3e4640c3a48519` was added in google/fonts commit `be8dcf484` ("Cabin Condensed: add source block to METADATA.pb", Felipe Sanches, 2026-02-26). The commit message notes: "Config: override config.yaml in google/fonts, Status: complete, Confidence: MEDIUM".

The commit `9476ee6f` is a merge commit from 2017-02-23 with message "Merge pull request #12 from m4rc1e/master" / "sources | fonts: v2.200 update". This aligns precisely with google/fonts commit `eef4029d7` ("cabincondened: v2.200 added (#680)", merged 2017-05-01). PR #680 body explicitly states: "Same as #679, both families are generated from the same .glyphs file." The commit exists in the upstream repo, which is cached at `upstream_repos/fontc_crater_cache/impallari/Cabin/`.

Note: Cabin was later updated to v3.001 as a variable font (upstream commit `70efa8c3`), but Cabin Condensed was not updated. The Cabin Condensed static fonts still correspond to the v2.200 era. The v3.001 Cabin variable font includes a `wdth` axis (75-100) that covers condensed widths, but Cabin Condensed remains a separate family entry.

The upstream repository does not contain a `config.yaml` at any commit. An override `config.yaml` was created in the google/fonts family directory (`ofl/cabincondensed/config.yaml`) by Felipe Sanches in commit `be8dcf484`. Contents:

```yaml
sources:
  - sources/Cabin.glyphs
familyName: Cabin Condensed
buildVariable: false
```

The source file `sources/Cabin.glyphs` exists at commit `9476ee6f` and contains both regular and condensed masters. Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Conclusion

All source metadata is complete and verified. The repository URL, commit hash, and override config.yaml are all in place. Status is `complete`. The commit is well-supported by the PR cross-reference (#680 by m4rc1e at the same version that was added to google/fonts).
