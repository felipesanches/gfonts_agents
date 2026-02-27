# Investigation: Big Shoulders Text SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Text SC |
| Slug | big-shoulders-text-sc |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 0b3d09a86862b19efae28eae0cd868f17c476b20 |
| Config YAML | override config.yaml in google/fonts (ofl/bigshoulderstextsc/config.yaml) |
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
    source_file: "Big-Shoulders/fonts/variable/text/BigShouldersTextSC[wght].ttf"
    dest_file: "BigShouldersTextSC[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb. All Big Shoulders variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `0b3d09a86862b19efae28eae0cd868f17c476b20`. The google/fonts commit `461776338` ("Big Shoulders Text SC: Version 2.002 added") explicitly states:

> "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/0b3d09a86862b19efae28eae0cd868f17c476b20."

The family was added on 2024-05-30 (date_added). The commit `0b3d09a` is dated 2024-02-26 in the upstream repo, predating the google/fonts addition. The commit exists in the upstream repo cache.

### Config YAML

An override `config.yaml` exists in `ofl/bigshoulderstextsc/config.yaml`. It shares the same recipe as the Text config, building the SC variant via `smcp -> ccmp` remapping and subspacing to `opsz=10`. The `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The source block in METADATA.pb is complete with correct repository URL and commit hash. The override config.yaml in google/fonts is correctly configured. Status is `complete`.
