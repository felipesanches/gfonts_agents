# Investigation: Bitcount Grid Single

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Grid Single |
| Slug | bitcount-grid-single |
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
    source_file: "fonts/ttf/variable/BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf"
    dest_file: "BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb.

Bitcount Grid Single is part of the initial batch of Bitcount non-Ink families added to google/fonts in January 2025. The git log for the TTF file shows two commits: `ce6029c68` ("Fix italic feature, fixes ots-sanitizer") and `bb009d354` ("Bitcount Grid Double: Version 1.0 added") — the latter being a bulk commit adding multiple Bitcount families simultaneously.

The commit `bb009d354` body confirms all non-Ink Bitcount families were taken from the upstream repo at commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a`. This matches the METADATA.pb commit hash.

Commit `af0818eaeb3b` exists in the upstream repo cache (`/mnt/shared/upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount`), dated January 13, 2025. It is confirmed as the onboarding commit.

The upstream `sources/config.yaml` only contains `familyName: Bitcount`. An override `config.yaml` is present in the google/fonts family directory (`ofl/bitcountgridsingle/config.yaml`):
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Single
buildVariable: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists in the google/fonts directory, the `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb source block is complete. The commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a` is confirmed as the onboarding commit. An override `config.yaml` is present in the google/fonts family directory. No action needed.
