# Investigation: Bitcount Grid Double

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Grid Double |
| Slug | bitcount-grid-double |
| License Dir | ofl |
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit Hash | af0818eaeb3b0839806ea19134fc18f317cdcf5a |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "af0818eaeb3b0839806ea19134fc18f317cdcf5a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf"
    dest_file: "BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb.

The font was added to google/fonts in commit `bb009d354` (January 17, 2025), titled "Bitcount Grid Double: Version 1.0 added". The commit body confirms: "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/af0818eaeb3b0839806ea19134fc18f317cdcf5a." This matches the commit hash in the current METADATA.pb.

Commit `af0818eaeb3b` exists in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount` and is dated January 13, 2025 ("Update fixAnchors.py"), just 4 days before the google/fonts addition — confirming this is the correct onboarding commit.

The upstream repo does have a `sources/config.yaml` file (content: `familyName: Bitcount`), but this is a minimal family-name-only file, insufficient as a full gftools-builder config. An override `config.yaml` is present in the google/fonts family directory (`ofl/bitcountgriddouble/config.yaml`) with proper content:
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Double
buildVariable: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists in the google/fonts directory, the `config_yaml` field is correctly omitted from METADATA.pb. The google-fonts-sources tool auto-detects the local override.

## Conclusion

The METADATA.pb source block is complete. The commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a` is confirmed as the onboarding commit. An override `config.yaml` is present in the google/fonts family directory. No action needed.
