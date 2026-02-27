# Investigation: Amiri Quran

## Summary

| Field | Value |
|-------|-------|
| Family Name | Amiri Quran |
| Slug | amiri-quran |
| License Dir | ofl |
| Repository URL | https://github.com/aliftype/amiri |
| Commit Hash | 480bb746e99ea700bb0d6b4dbf96302d58192103 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/aliftype/amiri"
  commit: "480bb746e99ea700bb0d6b4dbf96302d58192103"
  archive_url: "https://github.com/aliftype/amiri/releases/download/1.003/Amiri-1.003.zip"
  files {
    source_file: "Amiri-1.003/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Amiri-1.003/AmiriQuran-Regular.ttf"
    dest_file: "AmiriQuran-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The Amiri Quran font was added to google/fonts in stages. The most recent binary update was at commit `3c5672f8a` (July 16, 2025, "push version 1.003"), authored by Emma Marichal, followed by a filename normalization commit `2e4388d44` (July 17, 2025, "file name") that renamed `AmiriQuran.ttf` to `AmiriQuran-Regular.ttf`.

The METADATA.pb source block uses `archive_url` pointing to the 1.003 release archive (`https://github.com/aliftype/amiri/releases/download/1.003/Amiri-1.003.zip`). The `commit` field `480bb746e99ea700bb0d6b4dbf96302d58192103` corresponds to the "1.003" commit in the aliftype/amiri repo, dated June 13, 2025. This commit was verified in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/aliftype/amiri/`.

The upstream Amiri repo uses a Makefile build system (not gftools-builder natively), with sources in `sources/Amiri.glyphspackage`. There is no `config.yaml` in the upstream repo. However, an override `config.yaml` exists in `ofl/amiriquran/` within google/fonts, containing:

```yaml
sources:
  - sources/Amiri.glyphspackage
familyName: Amiri Quran
buildStatic: true
buildOTF: false
```

Per project policy, since the override `config.yaml` exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb `source { }` block (google-fonts-sources auto-detects local overrides).

## Conclusion

Status is complete. The METADATA.pb has `repository_url`, `commit`, and `archive_url` all correctly set. An override `config.yaml` exists in the google/fonts family directory. No action needed.
