# Investigation: BBH Bartle

## Summary

| Field | Value |
|-------|-------|
| Family Name | BBH Bartle |
| Slug | bbh-bartle |
| License Dir | ofl |
| Repository URL | https://github.com/Studio-DRAMA/BBH |
| Commit Hash | b8d40ef62b138be4c7c3dac2de117217f261b24b |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Studio-DRAMA/BBH"
  commit: "b8d40ef62b138be4c7c3dac2de117217f261b24b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/BBHBartle-Regular.ttf"
    dest_file: "BBHBartle-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

BBH Bartle was added to google/fonts on 2025-11-27 in commit `7fd17744cf5eaccc62d832e0d171183df8768ac1` ("Add Bartle (new name)") by Emma Marichal. The METADATA.pb already included `repository_url: "https://github.com/Studio-DRAMA/BBH"`. The URL is also referenced in the copyright string.

The commit hash `b8d40ef62b138be4c7c3dac2de117217f261b24b` was added to METADATA.pb in a subsequent enrichment commit (`ec997b1d4`, 2026-02-26, "BBH Bartle: add source block to METADATA.pb"). This commit was identified by inference and binary verification: it is the last upstream commit before the google/fonts onboarding date (dated 2025-11-26, one day prior). The font binary was confirmed byte-identical between the upstream repo at `b8d40ef` and the file added to google/fonts.

The upstream repo `Studio-DRAMA/BBH` hosts all three BBH font families (Bartle, Bogle, Hegarty). The `sources/config.yaml` in the upstream repo covers all three:

```yaml
sources:
  - BBH-Bartle.glyphs
  - BBH-Bogle.glyphs
  - BBH-Hegarty.glyphs
familyName: "BBH Display"
buildVariable: false
buildStatic: true
buildTTF: true
buildOTF: true
autohintTTF: false
autohintOTF: false
includeSourceFixes: true
cleanUp: true
```

The `config_yaml` field in METADATA.pb correctly points to `sources/config.yaml`. No override config.yaml exists in the google/fonts family directory.

The upstream repo has 2 additional commits after the onboarding commit (merge commits `5d71932` and `28579a3`). The repo is cached at `upstream_repos/fontc_crater_cache/Studio-DRAMA/BBH`.

## Conclusion

Status is complete. The METADATA.pb source block has all required fields: `repository_url`, `commit`, `branch`, and `config_yaml`. No action needed.
