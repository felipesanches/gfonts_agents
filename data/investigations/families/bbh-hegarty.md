# Investigation: BBH Hegarty

## Summary

| Field | Value |
|-------|-------|
| Family Name | BBH Hegarty |
| Slug | bbh-hegarty |
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
    source_file: "fonts/ttf/BBHHegarty-Regular.ttf"
    dest_file: "BBHHegarty-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

BBH Hegarty was added to google/fonts on 2025-11-27 in commit `d62d7d2a584826eb1941451cd3046321887646d0` ("add bbh hegarty") by Emma Marichal, just 12 minutes after BBH Bogle. It shares the same upstream repository as BBH Bartle and BBH Bogle.

The commit hash `b8d40ef62b138be4c7c3dac2de117217f261b24b` was added to METADATA.pb in commit `0cdca60cf` ("BBH Hegarty: add source block to METADATA.pb", 2026-02-26). The commit was identified by binary matching: the upstream commit `b8d40ef` ("push fonts", 2025-11-26) modified `fonts/ttf/BBHHegarty-Regular.ttf` from 28,844 to 28,752 bytes. The google/fonts binary (28,752 bytes) is identical. The commit was on Emma's fork branch and merged into Studio-DRAMA/BBH main on 2025-12-04 via `5d71932`. All three BBH families were onboarded from this same upstream commit.

The `sources/config.yaml` in the upstream repo covers all three BBH families:

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

The upstream repo is cached at `upstream_repos/fontc_crater_cache/Studio-DRAMA/BBH`.

## Conclusion

Status is complete. The METADATA.pb source block has all required fields: `repository_url`, `commit`, `branch`, and `config_yaml`. No action needed.
