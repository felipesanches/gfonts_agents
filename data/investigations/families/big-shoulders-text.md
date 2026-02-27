# Investigation: Big Shoulders Text

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Text |
| Slug | big-shoulders-text |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 41153e6fe01d218e933919a1d08c8e45065bc8fe (recorded) / 465a9c592f06d493841b35dca5d248c8142b75f8 (correct) |
| Config YAML | override config.yaml in google/fonts (ofl/bigshoulderstext/config.yaml) |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "41153e6fe01d218e933919a1d08c8e45065bc8fe"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders/fonts/variable/text/BigShouldersText[wght].ttf"
    dest_file: "BigShouldersText[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb and confirmed by the copyright string. All Big Shoulders variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `41153e6fe01d218e933919a1d08c8e45065bc8fe`, but this is incorrect. The google/fonts commit `7f3f5f3c7` (PR #3432, "Big Shoulders Text: Version 2.000 added") states:

> "Big Shoulders Text Version 2.002 taken from the upstream repo ... at commit https://github.com/xotypeco/big_shoulders/commit/465a9c592f06d493841b35dca5d248c8142b75f8."

The existing `upstream_info.md` in `ofl/bigshoulderstext/upstream_info.md` provides detailed binary blob hash verification confirming `465a9c5` as the correct commit. It notes:

- At commit `41153e6` (May 2021), the directory `Big-Shoulders/fonts/variable/text/` does not contain `BigShouldersText[wght].ttf` — the file path in METADATA.pb would not resolve
- The file at commit `465a9c5` matches the google/fonts binary exactly

The gftools-packager ran twice during this PR: first referencing `41153e6`, then `465a9c592f06d493841b35dca5d248c8142b75f8` (August 2021, "Merge pull request #39 from vv-monsalve/master" — STAT table fixes). Both commits exist in the upstream repo cache.

### Config YAML

An override `config.yaml` exists in `ofl/bigshoulderstext/config.yaml`. It builds from `Big-Shoulders/sources/BigShoulders.glyphs`, subspaces to `opsz=10` (text), and also builds the SC variant. The `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb has repository URL and commit hash, but the commit `41153e6` is incorrect. The correct commit is `465a9c592f06d493841b35dca5d248c8142b75f8`. The source block needs correction. The override config.yaml is correctly configured.
