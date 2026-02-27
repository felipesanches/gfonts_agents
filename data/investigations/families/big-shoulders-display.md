# Investigation: Big Shoulders Display

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Display |
| Slug | big-shoulders-display |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 41153e6fe01d218e933919a1d08c8e45065bc8fe |
| Config YAML | override config.yaml in google/fonts (ofl/bigshouldersdisplay/config.yaml) |
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
    source_file: "Big-Shoulders/fonts/variable/display/BigShouldersDisplay[wght].ttf"
    dest_file: "BigShouldersDisplay[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb and matches the copyright string. All Big Shoulders variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `41153e6fe01d218e933919a1d08c8e45065bc8fe`. However, the font binaries in google/fonts correspond to a **different commit**.

The font was last updated to Version 2.000 via google/fonts commit `94ee6b8b9` (PR #3434, "Big Shoulders Display: Version 2.000 added"). That commit's body states:

> "Big Shoulders Display Version 2.002 taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/465a9c592f06d493841b35dca5d248c8142b75f8."

The gftools-packager was run twice during PR #3434:
1. First run (PR body): Referenced `41153e6` (dated 2021-05-20, a merge commit by Viviana Monsalve)
2. Final run (squash commit body): Referenced `465a9c592f06d493841b35dca5d248c8142b75f8` (dated 2021-08-27, the PR#39 merge that added STAT table fixes)

Per the gftools-packager hint policy, the commit in the squash merge body (`465a9c5`) is more likely to be the actual source, but the METADATA.pb currently records `41153e6`. The existing `upstream_info.md` in the google/fonts family directory confirms this discrepancy and identifies `465a9c5` as the correct commit via binary blob hash verification.

Both commit `41153e6` and `465a9c5` exist in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/xotypeco/big_shoulders`.

### Config YAML

An override `config.yaml` exists in the google/fonts family directory at `ofl/bigshouldersdisplay/config.yaml`. It uses a recipe-based build that subspaces the Big Shoulders glyphs to `opsz=72` to produce the Display variant. The `config_yaml` field is correctly omitted from METADATA.pb since the local override is auto-detected.

## Conclusion

The METADATA.pb has repository URL and commit hash, but the commit hash `41153e6` appears to be incorrect — the binary fonts correspond to commit `465a9c5`. The source block needs correction to update the commit hash from `41153e6fe01d218e933919a1d08c8e45065bc8fe` to `465a9c592f06d493841b35dca5d248c8142b75f8`. The override config.yaml in google/fonts is correctly configured.
