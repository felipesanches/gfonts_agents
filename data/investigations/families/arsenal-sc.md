# Investigation: Arsenal SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Arsenal SC |
| Slug | arsenal-sc |
| License Dir | ofl |
| Repository URL | https://github.com/alexeiva/Arsenal |
| Commit Hash | e34db566b2f5de986eea9b36986d602015d80615 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/alexeiva/Arsenal"
  commit: "e34db566b2f5de986eea9b36986d602015d80615"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/TTF/ArsenalSC-Regular.ttf"
    dest_file: "ArsenalSC-Regular.ttf"
  }
  files {
    source_file: "fonts/TTF/ArsenalSC-Italic.ttf"
    dest_file: "ArsenalSC-Italic.ttf"
  }
  files {
    source_file: "fonts/TTF/ArsenalSC-Bold.ttf"
    dest_file: "ArsenalSC-Bold.ttf"
  }
  files {
    source_file: "fonts/TTF/ArsenalSC-BoldItalic.ttf"
    dest_file: "ArsenalSC-BoldItalic.ttf"
  }
  branch: "master"
}
```

## Investigation

The family was added to Google Fonts on 2024-05-27, when Simon Cozens committed `b2e732cec` ("Arsenal SC: Version 2.001; ttfautohint (v1.8.4.7-5d5b) added"). The commit body explicitly states: "Taken from the upstream repo https://github.com/alexeiva/Arsenal at commit https://github.com/alexeiva/Arsenal/commit/e34db566b2f5de986eea9b36986d602015d80615."

The upstream repository `alexeiva/Arsenal` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/alexeiva/Arsenal`. The commit `e34db566` is confirmed present in the cached repo (dated 2017-06-26, "updated README").

The `sources/` directory in the upstream repo contains two .glyphs source files: `Arsenal.glyphs` and `Arsenal-Italic.glyphs`. No `config.yaml` exists in the upstream repository.

An override `config.yaml` exists in the google/fonts family directory at `ofl/arsenalsc/config.yaml`. Per policy, the `config_yaml` field is omitted from METADATA.pb when an override config exists locally. The override config.yaml specifies:
- `buildVariable: false`
- Sources: `Arsenal.glyphs` and `Arsenal-Italic.glyphs`

The source block is fully populated with repository_url and commit. The absence of config_yaml in METADATA.pb is correct per the override config policy.

## Conclusion

Status is complete. The repository URL, commit hash, and override config.yaml are all established. The override config references the upstream .glyphs source files. No further action needed.
