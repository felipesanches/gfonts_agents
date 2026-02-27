# Investigation: Albert Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Albert Sans |
| Slug | albert-sans |
| License Dir | ofl |
| Repository URL | https://github.com/usted/Albert-Sans |
| Commit Hash | f7f46082233f5a29cb71d6ae1d8d0ef9c7962d6c |
| Config YAML | sources/config.yaml |
| Status | needs_correction |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/usted/Albert-Sans"
  commit: "f7f46082233f5a29cb71d6ae1d8d0ef9c7962d6c"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AlbertSans[wght].ttf"
    dest_file: "AlbertSans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AlbertSans-Italic[wght].ttf"
    dest_file: "AlbertSans-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Albert Sans was added to google/fonts via PR #4756, merged in commit `6b612533e` ("Albert Sans: Version 1.025 added"). The gftools-packager commit message states:

> Albert Sans Version 1.025 taken from the upstream repo https://github.com/usted/Albert-Sans at commit https://github.com/usted/Albert-Sans/commit/929c7d5058afd06870d1dd4ebc3a0ee98bb77420.

The original onboarding commit was `929c7d5058afd06870d1dd4ebc3a0ee98bb77420` (dated 2022-06-03, "fonts folder" — a file reorganization commit).

The METADATA.pb was later updated twice:
1. Commit `66f91f10f` (2024-04-03, "Merge upstream.yaml into METADATA.pb"): kept `929c7d50` as the commit hash, added files and branch fields.
2. Commit `19cdcec59` (2025-03-31, "[Batch 1/4] port info from fontc_crater targets list"): **changed the commit hash from `929c7d50` to `f7f46082`**, and added `config_yaml: "sources/config.yaml"`.

The commit `f7f46082233f5a29cb71d6ae1d8d0ef9c7962d6c` is the **current HEAD** of the Albert Sans repo (dated 2024-07-30), which is more than two years newer than the original onboarding (June 2022). The batch update substituted a newer commit hash from the fontc_crater targets list without verifying that the binary in google/fonts matches this newer commit.

Per project policy, gftools-packager hints must be cross-verified. The actual onboarding used commit `929c7d50`, which is the correct reference for the binary that was uploaded. The current METADATA.pb commit `f7f46082` is a later state of the upstream repository.

Both commits exist in the cached repository at `upstream_repos/fontc_crater_cache/usted/Albert-Sans/`. The `sources/config.yaml` exists at both commit points.

The `sources/config.yaml` content:
```yaml
sources:
  - AlbertSans-Roman.glyphs
  - AlbertSans-Italic.glyphs
axisOrder:
  - wght
  - wdth
familyName: Albert Sans
```

## Conclusion

The commit hash in METADATA.pb (`f7f46082`) appears to be incorrect — it references a commit from July 2024, while the fonts were onboarded from commit `929c7d50` (June 2022). The `config_yaml` field is correctly set to `sources/config.yaml`. The commit hash should be corrected back to `929c7d5058afd06870d1dd4ebc3a0ee98bb77420`. This requires a fix PR to google/fonts.
