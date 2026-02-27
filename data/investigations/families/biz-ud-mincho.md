# Investigation: BIZ UDMincho

## Summary

| Field | Value |
|-------|-------|
| Family Name | BIZ UDMincho |
| Slug | biz-ud-mincho |
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
    source_file: "fonts/ttf/BIZUDMincho-Regular.ttf"
    dest_file: "BIZUDMincho-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/BIZUDMincho-Bold.ttf"
    dest_file: "BIZUDMincho-Bold.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb, but an override `config.yaml` is present in the google/fonts family directory.

The font was last updated in google/fonts commit `63833b7d1` (PR #5697), titled "BIZ UDPMincho: Version 1.06 added; BIZ UDMincho: Version 1.06 added". The commit body confirms: "BIZ UDMincho Version 1.06 taken from the upstream repo https://github.com/googlefonts/morisawa-biz-ud-mincho.git at commit https://github.com/googlefonts/morisawa-biz-ud-mincho/commit/c30a6221b1f3d09afae9137ffe73c7cbec649947." This matches the commit hash in the current METADATA.pb.

Commit `c30a6221b1f3d09afae9137ffe73c7cbec649947` is confirmed in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/morisawa-biz-ud-mincho` (dated December 6, 2022, merging PR #17 "Updating requirements document").

The upstream repository uses a custom build script (`sources/build.py`) for the full font build, but extension Glyphs files are available at `sources/extensions/BIZ-UDMinchoExt.glyphs`.

An override `config.yaml` is present in the google/fonts family directory (`ofl/bizudmincho/config.yaml`):
```yaml
sources:
  - sources/extensions/BIZ-UDMinchoExt.glyphs
familyName: BIZ UDMincho
buildStatic: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists, the `config_yaml` field is correctly omitted from METADATA.pb.

BIZ UDMincho and BIZ UDPMincho share the same upstream repository and commit hash `c30a6221b1f3d09afae9137ffe73c7cbec649947`, both updated in the same PR #5697.

## Conclusion

The METADATA.pb source block has a valid repository URL and correct commit hash. An override `config.yaml` is present in the google/fonts family directory. No action needed.
