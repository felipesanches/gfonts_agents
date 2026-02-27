# Investigation: Bitcount Ink

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Ink |
| Slug | bitcount-ink |
| License Dir | ofl |
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit Hash | 89e7994f73b7f5ced80e7cf493d40be9e66ff82f |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "89e7994f73b7f5ced80e7cf493d40be9e66ff82f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb.

The font file history in google/fonts shows commits `c020967df` ("Bitcount Ink: Version 1.001 added") and `50712b8cc` ("Bitcount: Version 1.0 added"). The commit `c020967df` body confirms: "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/89e7994f73b7f5ced80e7cf493d40be9e66ff82f." This matches the METADATA.pb commit hash.

Commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` exists in the upstream repo cache (`/mnt/shared/upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount`), dated September 5, 2025 (merging "Fix ligatures" PR #37 from petrvanblokland/TYPETR-Bitcount).

The upstream `sources/config.yaml` only contains `familyName: Bitcount`. An override `config.yaml` is present in the google/fonts family directory (`ofl/bitcountink/config.yaml`):
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Ink
buildVariable: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists in the google/fonts directory, the `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb source block is complete. The commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` is confirmed as the onboarding commit. An override `config.yaml` is present in the google/fonts family directory. No action needed.
