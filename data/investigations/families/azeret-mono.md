# Investigation: Azeret Mono

## Summary

| Field | Value |
|-------|-------|
| Family Name | Azeret Mono |
| Slug | azeret-mono |
| License Dir | ofl |
| Repository URL | https://github.com/displaay/Azeret |
| Commit Hash | 3d45a6c3e094f08bfc70551b525bd2037cac51ba |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/displaay/Azeret"
  commit: "3d45a6c3e094f08bfc70551b525bd2037cac51ba"
  files {
    source_file: "fonts/variable/AzeretMono[wght].ttf"
    dest_file: "AzeretMono[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AzeretMono-Italic[wght].ttf"
    dest_file: "AzeretMono-Italic[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Azeret Mono is a variable monospace font by Displaay (Martin Vacha), added to Google Fonts on 2021-06-08. The font was initially added as `ofl/azeret` (in PR #3475, commit `c44cf77ca`, 2021-06-09) and renamed to `ofl/azeretmono` in PR #3739 (2021-08-16, "ofl/azeret -> ofl/azeretmono").

The original onboarding commit body explicitly states: "Azeret Version 1.002 taken from the upstream repo https://github.com/displaay/Azeret at commit https://github.com/displaay/Azeret/commit/3d45a6c3e094f08bfc70551b525bd2037cac51ba."

The commit `3d45a6c3e094f08bfc70551b525bd2037cac51ba` is confirmed in the upstream cache at `displaay/Azeret` (dated 2021-06-04 21:41:25 +0200, "Merge pull request #3 from RosaWagner/main").

The repository URL and commit hash were merged into METADATA.pb from `upstream.yaml` by Simon Cozens in commit `66f91f10f` ("Merge upstream.yaml into METADATA.pb", 2024-04-03). The `config_yaml` field was added by the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31).

The `sources/config.yaml` exists at the referenced commit and specifies:
- Sources: `AzeretMono.glyphs` and `AzeretMono-Italic.glyphs`
- `axisOrder: [wght, ital]`
- Family name: Azeret Mono

The copyright string in METADATA.pb references `https://github.com/displaay/azeret` (lowercase), while the actual repo is `displaay/Azeret` (uppercase E). Both refer to the same repository.

## Conclusion

Status is complete. All required fields (repository_url, commit, config_yaml) are present and verified in METADATA.pb. The commit matches the original gftools-packager onboarding reference. No further action needed.
