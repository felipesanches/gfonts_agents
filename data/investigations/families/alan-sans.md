# Investigation: Alan Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alan Sans |
| Slug | alan-sans |
| License Dir | ofl |
| Repository URL | https://github.com/alan-eu/Alan-Sans |
| Commit Hash | 425d3a0674a49f0ad6bc6ceef5ca0c557b520838 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/alan-eu/Alan-Sans"
  commit: "425d3a0674a49f0ad6bc6ceef5ca0c557b520838"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AlanSans[wght].ttf"
    dest_file: "AlanSans[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Alan Sans was added to google/fonts in commit `1b91df7f5cb3c1018f1d279af8aa3e5671cd4e08` ("Alan Sans: Version 1.000 added"). The commit message confirms:

> Taken from the upstream repo https://github.com/alan-eu/Alan-Sans at commit https://github.com/alan-eu/Alan-Sans/commit/425d3a0674a49f0ad6bc6ceef5ca0c557b520838.

The METADATA.pb was set correctly from the start, including the `config_yaml: "sources/config.yaml"` field.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/alan-eu/Alan-Sans/`. The local cache appears to be a shallow clone containing only the latest commit (`11bb823f`, dated 2026-01-20), while the METADATA.pb references commit `425d3a0674a49f0ad6bc6ceef5ca0c557b520838` which is not present in the local cache. However, the commit hash is directly confirmed by the google/fonts commit message.

The `sources/config.yaml` exists in the current cache:
```yaml
sources:
  - AlanSans.glyphs
familyName: "Alan Sans"
cleanUp: true
stat:
  AlanSans[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: Light
      value: 300
    ...
```

The config references `AlanSans.glyphs` as the source, with appropriate stat table configuration for the variable weight axis.

## Conclusion

METADATA.pb is complete and correct: repository URL, commit hash, and config_yaml path are all present and consistent with the google/fonts onboarding commit. No action needed.
