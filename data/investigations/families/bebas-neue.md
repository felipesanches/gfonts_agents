# Investigation: Bebas Neue

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bebas Neue |
| Slug | bebas-neue |
| License Dir | ofl |
| Repository URL | https://github.com/dharmatype/Bebas-Neue |
| Commit Hash | 686d14af640c17af3691c597778f121d840d9051 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/dharmatype/Bebas-Neue"
  commit: "686d14af640c17af3691c597778f121d840d9051"
}
```

## Investigation

Bebas Neue was added to google/fonts on 2019-10-16 via Font Bakery Dashboard PR #2208 ("[Font Bakery Dashboard] create family: Bebas Neue"), committed in google/fonts as `1e42f687f`. The PR body explicitly recorded:

- **upstream**: `"https://github.com/dharmatype/Bebas-Neue"`
- **commit**: `686d14af640c17af3691c597778f121d840d9051`
- **commitDate**: `2019-10-07T22:21:38.000Z`

The upstream commit `686d14a` is titled "Update DESCRIPTION.en_us.html" and is dated 2019-10-08 (JST), consistent with the commitDate. The commit hash was later added to METADATA.pb in commit `61f595f96` ("Bebas Neue: add source block to METADATA.pb").

The upstream repository has no `config.yaml` at any commit. However, an **override config.yaml** exists in the google/fonts family directory at `ofl/bebasneue/config.yaml`:

```yaml
sources:
  - sources/BebasNeueV2.0(2018).glyphs
```

This override was added in commit `5ddf312e6` ("Add config_yaml enrichment for 82 font families"). Since the local override exists, the `config_yaml` field is correctly omitted from METADATA.pb (google-fonts-sources auto-detects local overrides).

The upstream repo contains `sources/BebasNeueV2.0(2018).glyphs` as the source file. The repo is cached at `upstream_repos/fontc_crater_cache/dharmatype/Bebas-Neue`.

The font binary in google/fonts has not been updated since the initial addition. Multiple README.md updates occurred in the upstream repo after the onboarding commit, but no font binary changes.

## Conclusion

Status is complete. The METADATA.pb source block has `repository_url` and `commit`. The `config_yaml` field is correctly omitted because a local override config.yaml exists in the google/fonts family directory. No action needed.
