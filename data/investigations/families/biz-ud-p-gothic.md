# Investigation: BIZ UDPGothic

## Summary

| Field | Value |
|-------|-------|
| Family Name | BIZ UDPGothic |
| Slug | biz-ud-p-gothic |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/morisawa-biz-ud-gothic |
| Commit Hash | 18934af56b9c003ca58c54bffbf226848cb11032 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/morisawa-biz-ud-gothic"
  commit: "18934af56b9c003ca58c54bffbf226848cb11032"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/BIZUDPGothic-Regular.ttf"
    dest_file: "BIZUDPGothic-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/BIZUDPGothic-Bold.ttf"
    dest_file: "BIZUDPGothic-Bold.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb, but an override `config.yaml` is present in the google/fonts family directory.

The font was last updated in google/fonts commit `7da950f21` ("[gftools-packager] BIZ UDPGothic: Version 1.051 added"). The commit body confirms: "BIZ UDPGothic Version 1.051 taken from the upstream repo https://github.com/googlefonts/morisawa-biz-ud-gothic at commit https://github.com/googlefonts/morisawa-biz-ud-gothic/commit/18934af56b9c003ca58c54bffbf226848cb11032." This matches the commit hash in the current METADATA.pb.

Commit `18934af56b9c003ca58c54bffbf226848cb11032` is confirmed in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/morisawa-biz-ud-gothic` (dated September 6, 2023, merging PR #23 "Update to the UDPGothic Regular / Bold").

Note: BIZ UDPGothic has a different (more recent) commit hash compared to BIZ UDGothic (`38953aa0`), because BIZ UDPGothic received an additional update (Version 1.051) after the shared Version 1.05 update.

An override `config.yaml` is present in the google/fonts family directory (`ofl/bizudpgothic/config.yaml`):
```yaml
sources:
  - sources/extensions/BIZ-UDPGothicExt.glyphs
familyName: BIZ UDPGothic
buildStatic: true
buildOTF: false
```

The extension Glyphs file `sources/extensions/BIZ-UDPGothicExt.glyphs` exists in the upstream repository at the referenced commit.

## Conclusion

The METADATA.pb source block has a valid repository URL and correct commit hash. An override `config.yaml` is present in the google/fonts family directory. No action needed.
