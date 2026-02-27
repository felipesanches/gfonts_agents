# Investigation: Be Vietnam Pro

## Summary

| Field | Value |
|-------|-------|
| Family Name | Be Vietnam Pro |
| Slug | be-vietnam-pro |
| License Dir | ofl |
| Repository URL | https://github.com/bettergui/BeVietnamPro |
| Commit Hash | 804e62d81abbbcdcce5686069c69b41b8c245192 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/bettergui/BeVietnamPro"
  commit: "804e62d81abbbcdcce5686069c69b41b8c245192"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/BeVietnamPro-Black.ttf"
    dest_file: "BeVietnamPro-Black.ttf"
  }
  [... 17 total font files ...]
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Be Vietnam Pro has a two-commit history in google/fonts:
1. `659c177cd` - Version 1.000 added (PR #3456) — initial addition
2. `1cfe4cb46` (2021-08-27) - Version 1.002; ttfautohint (v1.8.3) added (PR #3771) — last TTF modification

The last commit that modified the TTF files is `1cfe4cb46` by Rosalie Wagner. The commit message from the gftools-packager update (PR #3771) explicitly states:

> "Be Vietnam Pro Version 1.002; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/bettergui/BeVietnamPro at commit https://github.com/bettergui/BeVietnamPro/commit/804e62d81abbbcdcce5686069c69b41b8c245192."

The upstream commit `804e62d` is verified locally in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/bettergui/BeVietnamPro`. The commit message is: "fix(sources): Update winAscent in Master". This is the HEAD of the main branch, confirming the repo has not been updated since onboarding.

The config.yaml at commit `804e62d` in `sources/config.yaml` contains:

```yaml
sources:
  - BeVietnamPro.glyphs
  - BeVietnamPro-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Be Vietnam Pro
```

The METADATA.pb source block is fully populated with `repository_url`, `commit`, `config_yaml: "sources/config.yaml"`, `branch: "main"`, and explicit `files{}` mappings for all 18 TTF files (9 weights × 2 styles).

## Conclusion

The source metadata is complete. The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` — all correct and verified against the local cached upstream repo. No action needed.
