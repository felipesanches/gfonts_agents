# Investigation: Andada Pro

## Summary

| Field | Value |
|-------|-------|
| Family Name | Andada Pro |
| Slug | andada-pro |
| License Dir | ofl |
| Repository URL | https://github.com/huertatipografica/Andada-Pro |
| Commit Hash | a0b87b947003dee6c615809d3eebc8c1334dc575 |
| Config YAML | sources/build.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/huertatipografica/Andada-Pro"
  commit: "a0b87b947003dee6c615809d3eebc8c1334dc575"
  config_yaml: "sources/build.yaml"
  files {
    source_file: "fonts/variable/AndadaPro[wght].ttf"
    dest_file: "AndadaPro[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AndadaPro-Italic[wght].ttf"
    dest_file: "AndadaPro-Italic[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
```

## Investigation

The most recent binary update to google/fonts was at commit `4898fcbdc` (August 12, 2021, "Andada Pro: Version 3.003 added (#3693)"), authored by Rosalie Wagner. The commit message confirms: "Andada Pro Version 3.003 taken from the upstream repo https://github.com/huertatipografica/Andada-Pro at commit https://github.com/huertatipografica/Andada-Pro/commit/a0b87b947003dee6c615809d3eebc8c1334dc575."

The commit hash `a0b87b947003dee6c615809d3eebc8c1334dc575` was verified in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/huertatipografica/Andada-Pro/`. The commit message is "add fonts" (August 5, 2021), one week before the google/fonts PR merged. This confirms it is the correct onboarding commit.

The `commit` and `config_yaml` fields were added to METADATA.pb by @felipesanches at commit `6e59217d1` (April 2, 2025, "sources info for Andada Pro (PR #3693)").

The `sources/build.yaml` exists in the upstream repo. Its content has unusual indentation (4 spaces before each key) but contains valid build configuration:

```yaml
    sources:
      - AndadaPro.glyphs
      - AndadaPro-Italic.glyphs
    axisOrder:
      - wght
      - ital
    familyName: Andada Pro
```

The file was verified at the referenced commit `a0b87b947003dee6c615809d3eebc8c1334dc575` using `git show`. The Glyphs source files `AndadaPro.glyphs` and `AndadaPro-Italic.glyphs` are present in the `sources/` directory.

## Conclusion

Status is complete. All required fields (`repository_url`, `commit`, `config_yaml`) are correctly populated in METADATA.pb. The commit hash matches the onboarding commit referenced in the google/fonts PR #3693 commit message. No action needed.
