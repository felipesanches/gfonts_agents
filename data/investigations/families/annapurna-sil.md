# Investigation: Annapurna SIL

## Summary

| Field | Value |
|-------|-------|
| Family Name | Annapurna SIL |
| Slug | annapurna-sil |
| License Dir | ofl |
| Repository URL | https://github.com/silnrsi/font-annapurna |
| Commit Hash | 5bd915dff1934cf36041d7766784347713c812a3 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/silnrsi/font-annapurna"
  commit: "5bd915dff1934cf36041d7766784347713c812a3"
  archive_url: "https://github.com/silnrsi/font-annapurna/releases/download/v2.000/AnnapurnaSIL-2.000.zip"
  files {
    source_file: "AnnapurnaSIL-2.000/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "AnnapurnaSIL-2.000/AnnapurnaSIL-Regular.ttf"
    dest_file: "AnnapurnaSIL-Regular.ttf"
  }
  files {
    source_file: "AnnapurnaSIL-2.000/AnnapurnaSIL-Bold.ttf"
    dest_file: "AnnapurnaSIL-Bold.ttf"
  }
  branch: "master"
}
```

## Investigation

Annapurna SIL was added to google/fonts at commit `06fa5749a` (January 19, 2024, "[gftools-packager] Annapurna SIL: Version 2.000 added"), authored by Emma Marichal. The commit message contained an incomplete upstream reference: "taken from the upstream repo https://github.com/silnrsi/font-annapurna at commit https://github.com/silnrsi/font-annapurna/commit/." (the commit hash was empty).

The `commit` field `5bd915dff1934cf36041d7766784347713c812a3` was added later by @felipesanches at google/fonts commit `1158b8da5` (December 12, 2025, "sources info for Annapurna SIL: Version 2.000 (PR #7204)"). The same commit also added an override `config.yaml` to the google/fonts family directory.

The commit `5bd915dff` in the upstream repo (`silnrsi/font-annapurna`) is dated November 9, 2023, with message "Bumped version to 2.001; replace reference fonts with 2.000". This is the commit immediately after the `v2.000` release tag, which points to commit `76733a2ef` (November 8, 2023, "Updated version history in documentation"). The `archive_url` uses the `v2.000` release archive, so the font binaries come from the release. The commit `5bd915dff` is one step past the tag but was selected as the closest available reference point.

The upstream repo (`/mnt/shared/upstream_repos/fontc_crater_cache/silnrsi/font-annapurna/`) uses a Waf-based build system (`wscript`) and UFO/designspace sources (`source/AnnapurnaSIL-RB.designspace`). There is no `config.yaml` in the upstream repo. An override `config.yaml` exists in `ofl/annapurnasil/` within google/fonts:

```yaml
buildVariable: false
sources:
  - source/AnnapurnaSIL-RB.designspace
```

Per project policy, since the override `config.yaml` exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb `source { }` block (google-fonts-sources auto-detects local overrides).

## Conclusion

Status is complete. The METADATA.pb has `repository_url`, `commit`, and `archive_url` all set. An override `config.yaml` exists in the google/fonts family directory. No action needed.
