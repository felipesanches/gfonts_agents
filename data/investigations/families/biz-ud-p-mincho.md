# Investigation: BIZ UDPMincho

## Summary

| Field | Value |
|-------|-------|
| Family Name | BIZ UDPMincho |
| Slug | biz-ud-p-mincho |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/morisawa-biz-ud-mincho |
| Commit Hash | c30a6221b1f3d09afae9137ffe73c7cbec649947 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/morisawa-biz-ud-mincho"
  commit: "c30a6221b1f3d09afae9137ffe73c7cbec649947"
  files {
    source_file: "fonts/ttf/BIZUDPMincho-Regular.ttf"
    dest_file: "BIZUDPMincho-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/BIZUDPMincho-Bold.ttf"
    dest_file: "BIZUDPMincho-Bold.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb, but an override `config.yaml` is present in the google/fonts family directory.

The font was last updated in google/fonts commit `63833b7d1` (PR #5697), titled "BIZ UDPMincho: Version 1.06 added; BIZ UDMincho: Version 1.06 added". The commit body confirms: "BIZ UDPMincho Version 1.06 taken from the upstream repo https://github.com/googlefonts/morisawa-biz-ud-mincho.git at commit https://github.com/googlefonts/morisawa-biz-ud-mincho/commit/c30a6221b1f3d09afae9137ffe73c7cbec649947." This matches the commit hash in the current METADATA.pb.

Commit `c30a6221b1f3d09afae9137ffe73c7cbec649947` is confirmed in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/morisawa-biz-ud-mincho` (dated December 6, 2022, merging PR #17 "Updating requirements document").

BIZ UDPMincho shares the same upstream repository and commit hash as BIZ UDMincho, both updated together in PR #5697.

An override `config.yaml` is present in the google/fonts family directory (`ofl/bizudpmincho/config.yaml`):
```yaml
sources:
  - sources/extensions/BIZ-UDPMinchoExt.glyphs
familyName: BIZ UDPMincho
buildStatic: true
buildOTF: false
```

The extension Glyphs file `sources/extensions/BIZ-UDPMinchoExt.glyphs` exists in the upstream repository at the referenced commit.

## Conclusion

The METADATA.pb source block has a valid repository URL and correct commit hash. An override `config.yaml` is present in the google/fonts family directory. No action needed.
