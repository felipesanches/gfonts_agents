# Investigation: Agu Display

## Summary

| Field | Value |
|-------|-------|
| Family Name | Agu Display |
| Slug | agu-display |
| License Dir | ofl |
| Repository URL | https://github.com/theseunbadejo/Agu-Display |
| Commit Hash | d520ebead8de4091a82040fe3d8f94d84c38c66f |
| Config YAML | sources/config.yaml |
| Status | needs_correction |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/theseunbadejo/Agu-Display"
  commit: "d520ebead8de4091a82040fe3d8f94d84c38c66f"
  archive_url: "https://github.com/theseunbadejo/Agu-Display/releases/download/1.05/Agu-Display-1.05.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AguDisplay[MORF].ttf"
    dest_file: "AguDisplay[MORF].ttf"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

**Git history for TTF files in google/fonts:**
- `6913b3938` — "Agu Display: Version 1.103 added" (2024-11-25, authored by Nathan Willis) — only commit ever touching these TTF files

The commit message body states:
> "Taken from the upstream repo https://github.com/theseunbadejo/Agu-Display at commit https://github.com/theseunbadejo/Agu-Display/commit/17a7ce91583f40d9e8f21eab6c57870a59c1b668."

**Commit hash discrepancy:**
- **Original onboarding commit** (from google/fonts commit message): `17a7ce91583f40d9e8f21eab6c57870a59c1b668`
- **Current METADATA.pb commit**: `d520ebead8de4091a82040fe3d8f94d84c38c66f`

The original METADATA.pb at the time of onboarding (visible in `git show 6913b3938:ofl/agudisplay/METADATA.pb`) had `17a7ce91`, consistent with the commit message. The current METADATA.pb has a different commit (`d520ebea`), which was set by a subsequent batch fontc_crater update (google/fonts commit `19cdcec59`, 2025-03-31).

**Upstream repo (theseunbadejo/Agu-Display) at METADATA.pb commit:**
- Commit `d520ebea` exists in the local cache (it is the HEAD of the shallow clone)
- Date: 2025-02-10 23:52:34 +0100
- Message: "Merge pull request #35 from theseunbadejo/ghactions-cairofix"
- This commit is approximately 3 months newer than the original onboarding (November 2024)

The original onboarding commit `17a7ce91` is NOT present in the local shallow cache. It cannot be verified without unshallowing the repo.

**Config YAML:**
`sources/config.yaml` exists at the current HEAD of the upstream repo:
```yaml
sources:
  - AguDisplay.glyphs
axisOrder:
  - morf
familyName: Agu Display
autohintOTF: False
stat:
  - name: Morph
    tag: MORF
    values:
    - name: Uzo
      value: 0
    - name: Ala
      value: 30
    - name: Osisi
      value: 60
```
This is a valid gftools-builder config for a variable font with a custom MORF axis. The source file is `AguDisplay.glyphs`. The config_yaml path (`sources/config.yaml`) was added by the fontc_crater batch update commit `19cdcec59` (2025-03-31), which also changed the commit hash.

**Additional context:**
- The METADATA.pb includes an `archive_url` pointing to GitHub release v1.05, which may provide an additional reference for the original onboarding binary
- The PR #8487 that onboarded this font had an empty body; the upstream commit reference only appeared in the commit message
- The intermediate commit `d520ebea` ("ghactions-cairofix") relates to a CI fix, suggesting font sources likely did not change between `17a7ce91` and `d520ebea`, but this cannot be formally confirmed without full repo history

**Status assessment:**
The commit hash in METADATA.pb (`d520ebea`) is NOT the original onboarding commit. The original commit (`17a7ce91`) is lost from accessible shallow clone history. The config_yaml path is correct and verified. The status is `needs_correction` because the recorded commit does not match what was used for onboarding.

## Conclusion

The METADATA.pb commit hash (`d520ebea`) does not match the original onboarding commit (`17a7ce91`) documented in the google/fonts commit message. The original commit is no longer accessible in the shallow clone. The config_yaml (`sources/config.yaml`) is correct. To fully resolve, the upstream repo should be unshallowed to verify whether the original commit still exists and whether font sources changed between the two commits. If no source changes occurred (as the "ghactions-cairofix" commit message suggests), the current METADATA.pb state is functionally correct but technically inaccurate regarding the commit hash.
