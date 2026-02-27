# Investigation: Big Shoulders Display SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Display SC |
| Slug | big-shoulders-display-sc |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 0b3d09a86862b19efae28eae0cd868f17c476b20 |
| Config YAML | override config.yaml in google/fonts (ofl/bigshouldersdisplaysc/config.yaml) |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "0b3d09a86862b19efae28eae0cd868f17c476b20"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders/fonts/variable/display/BigShouldersDisplaySC[wght].ttf"
    dest_file: "BigShouldersDisplaySC[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb and confirmed by the copyright string. All Big Shoulders variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `0b3d09a86862b19efae28eae0cd868f17c476b20`. The google/fonts commit `203560305` ("Big Shoulders Display SC: Version 2.002 added") explicitly states:

> "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/0b3d09a86862b19efae28eae0cd868f17c476b20."

This family was added on 2024-05-30 (date_added). The commit `0b3d09a` is dated 2024-02-26 in the upstream repo ("regenerate font files"), which predates the google/fonts addition date — consistent with being the onboarding commit. The commit exists in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/xotypeco/big_shoulders`.

### Config YAML

An override `config.yaml` exists in the google/fonts family directory at `ofl/bigshouldersdisplaysc/config.yaml`. It contains the same recipe as `ofl/bigshouldersdisplay/config.yaml` and builds both the Display and Display SC variants by subspacing to `opsz=72` and applying `smcp -> ccmp` remapping for SC. The `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The source block in METADATA.pb is complete with correct repository URL and commit hash. The override config.yaml in google/fonts is correctly configured. Status is `complete`.
