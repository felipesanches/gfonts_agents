# Investigation: BIZ UDGothic

## Summary

| Field | Value |
|-------|-------|
| Family Name | BIZ UDGothic |
| Slug | biz-ud-gothic |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/morisawa-biz-ud-gothic |
| Commit Hash | 38953aa0afd6937b9caa899e18f4550db7298d69 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/morisawa-biz-ud-gothic"
  commit: "38953aa0afd6937b9caa899e18f4550db7298d69"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/BIZUDGothic-Regular.ttf"
    dest_file: "BIZUDGothic-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/BIZUDGothic-Bold.ttf"
    dest_file: "BIZUDGothic-Bold.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb, but an override `config.yaml` is present in the google/fonts family directory.

The font was updated in google/fonts commit `01ac47e0b` (PR #4579), titled "BIZ UDPGothic: Version 1.05 added; BIZ UDGothic: Version 1.05 added". The commit body confirms: "BIZ UDGothic Version 1.05 taken from the upstream repo https://github.com/googlefonts/morisawa-biz-ud-gothic at commit https://github.com/googlefonts/morisawa-biz-ud-gothic/commit/38953aa0afd6937b9caa899e18f4550db7298d69." This matches the commit hash in the current METADATA.pb.

Commit `38953aa0afd6937b9caa899e18f4550db7298d69` is confirmed in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/morisawa-biz-ud-gothic` (dated May 2, 2022, merging PR #9 "Extended character set and Unicode updates").

The upstream repository uses a custom build script (`sources/build.py`) that merges existing Morisawa-delivered TTF files with additional glyphs compiled from extension Glyphs files (`sources/extensions/BIZ-UDGothicExt.glyphs`, etc.). This is not a standard gftools-builder workflow.

An override `config.yaml` is present in the google/fonts family directory (`ofl/bizudgothic/config.yaml`):
```yaml
sources:
  - sources/extensions/BIZ-UDGothicExt.glyphs
familyName: BIZ UDGothic
buildStatic: true
buildOTF: false
```

This override config references the extension Glyphs source file, which exists in the upstream repository at `sources/extensions/BIZ-UDGothicExt.glyphs`. Per policy, since an override `config.yaml` exists, the `config_yaml` field is correctly omitted from METADATA.pb.

Note: BIZ UDGothic and BIZ UDPGothic share the same upstream repository but have different commit hashes (BIZ UDGothic: `38953aa0`, BIZ UDPGothic: `18934af5` — a later version).

## Conclusion

The METADATA.pb source block has a valid repository URL and correct commit hash. An override `config.yaml` is present in the google/fonts family directory referencing the extension Glyphs source. No action needed.
