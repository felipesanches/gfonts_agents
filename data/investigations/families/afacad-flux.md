# Investigation: Afacad Flux

## Summary

| Field | Value |
|-------|-------|
| Family Name | Afacad Flux |
| Slug | afacad-flux |
| License Dir | ofl |
| Repository URL | https://github.com/Dicotype/Afacad |
| Commit Hash | b294b1f8610ff16a3846a255b1a6a2e6788a056e |
| Config YAML | sources/config_flux.yaml |
| Status | needs_correction |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Dicotype/Afacad"
  commit: "b294b1f8610ff16a3846a255b1a6a2e6788a056e"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Afacad_Flux/variable/AfacadFlux[slnt,wght].ttf"
    dest_file: "AfacadFlux[slnt,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config_flux.yaml"
}
```

## Investigation

**Git history for TTF files in google/fonts:**
- `ef30d6c39` — "Afacad Flux: Version 1.100 added" (2024-07-05, authored by Emma Marichal) — only commit ever touching these TTF files

The commit message body states:
> "Taken from the upstream repo https://github.com/Dicotype/Afacad at commit https://github.com/Dicotype/Afacad/commit/4655a472cef57467e1604ce80336ab87ea72facc."

**Commit hash discrepancy:**
- **Original onboarding commit** (from google/fonts commit message): `4655a472cef57467e1604ce80336ab87ea72facc`
- **Current METADATA.pb commit**: `b294b1f8610ff16a3846a255b1a6a2e6788a056e`

The original METADATA.pb at the time of onboarding (visible in `git show ef30d6c39:ofl/afacadflux/METADATA.pb`) also had `4655a472`, which is consistent with the commit message. The current METADATA.pb has a different commit (`b294b1f8`), which is the upstream HEAD as of the local shallow clone. This was changed by a subsequent batch update (fontc_crater port, google/fonts commit `19cdcec59`, 2025-03-31).

**Upstream repo (Dicotype/Afacad) at METADATA.pb commit:**
- Commit `b294b1f8` exists in the local cache (it is the HEAD of the shallow clone)
- Date: 2024-10-03 10:40:24 +0200
- Message: "Update README.md"
- This commit is approximately 3 months newer than the original onboarding (July 2024)

The original onboarding commit `4655a472` is NOT present in the local shallow cache (only one commit deep). It cannot be verified without unshallowing the repo.

**Config YAML:**
`sources/config_flux.yaml` exists in the upstream repo at the current HEAD. It references `AfacadFlux.glyphs` as its source file. The config path was correctly set by PR #7851 (google/fonts commit `187711d44`, 2025-05-22), which corrected a prior error where the batch update had incorrectly set `config_yaml: "sources/config.yaml"` (the config for the main Afacad family, not Afacad Flux).

**Config file contents at HEAD:**
```yaml
sources:
  - AfacadFlux.glyphs
familyName: Afacad Flux
axisOrder:
  - slnt
  - wght
stat:
  AfacadFlux[slnt,wght].ttf:
  - name: Slant
    tag: slnt
    ...
  - name: Weight
    tag: wght
    ...
outputDir: "../fonts/Afacad_Flux"
buildTTF: false
buildOTF: false
splitItalic: false
autohintTTF: false
```

**Status assessment:**
The commit hash in METADATA.pb (`b294b1f8`) is NOT the original onboarding commit. The original commit (`4655a472`) is lost from the upstream repo (possible force-push or rebase). The README-only commit `b294b1f8` is unlikely to have changed font sources, but this cannot be formally verified without unshallowing the repo. The config_yaml path (`sources/config_flux.yaml`) is correct and was fixed after initial incorrect population.

The status is `needs_correction` because the commit hash does not match what was originally used for onboarding, though the practical impact may be minimal since the intermediate commit only changed documentation.

## Conclusion

The METADATA.pb commit hash (`b294b1f8`) does not match the original onboarding commit (`4655a472`) documented in the google/fonts commit message for PR `ef30d6c39`. The original commit is no longer present in the upstream repo's accessible history (shallow clone). The config_yaml path is correct (`sources/config_flux.yaml`). To fully resolve, the upstream repo should be unshallowed to verify whether font sources changed between `4655a472` and `b294b1f8`, and ideally the METADATA.pb commit should be restored to the original onboarding commit if it still exists in full history.
