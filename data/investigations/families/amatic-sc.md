# Investigation: Amatic SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Amatic SC |
| Slug | amatic-sc |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/AmaticSC |
| Commit Hash | 308846136d2dcfb6aef2160d7e927698cdaf9c05 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/AmaticSC"
  commit: "308846136d2dcfb6aef2160d7e927698cdaf9c05"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The font files were last updated in google/fonts at commit `81e5d4b23` (October 31, 2017, "amaticsc: v2.505 added. (#1271)"), authored by Marc Foley. The commit message confirms the font was taken from `https://github.com/googlefonts/AmaticSC`.

The `repository_url` and `commit` fields were added to METADATA.pb in two stages:
1. `repository_url` was added by Simon Cozens in December 2023 ("Update upstreams").
2. `commit` and `config_yaml` were added by @felipesanches in commit `19cdcec59` (March 31, 2025, "[Batch 1/4] port info from fontc_crater targets list").

The commit hash `308846136d2dcfb6aef2160d7e927698cdaf9c05` corresponds to the merge of PR #18 ("add sources/config.yaml") in the AmaticSC upstream repo, authored by @felipesanches on February 24, 2025. This was a deliberate addition to make the upstream repo gftools-builder-compatible.

The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/AmaticSC/` as a shallow clone (depth 1) at this commit. The `sources/config.yaml` exists and contains:

```yaml
sources:
  - AmaticSC.glyphs
```

This is a valid gftools-builder configuration. The referenced commit is the HEAD of the upstream repo after the config.yaml was added for fontc_crater compatibility. The actual font binaries in google/fonts predate this commit (from 2017), but the upstream source structure is correctly documented.

## Conclusion

Status is complete. All required fields (`repository_url`, `commit`, `config_yaml`) are correctly populated in METADATA.pb. The `sources/config.yaml` exists at the referenced commit in the upstream repo. No action needed.
