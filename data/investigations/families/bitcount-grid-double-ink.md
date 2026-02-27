# Investigation: Bitcount Grid Double Ink

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Grid Double Ink |
| Slug | bitcount-grid-double-ink |
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
    source_file: "fonts/ttf/variable/BitcountGridDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountGridDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb.

The Bitcount Ink families were added to google/fonts later than the non-Ink families. The font file history shows two commits: `ce6029c68` ("Fix italic feature, fixes ots-sanitizer") and the initial addition `5d1b8f3e6` ("Bitcount Grid Double Ink: Version 1.001 added"). The commit `5d1b8f3e6` body confirms: "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/89e7994f73b7f5ced80e7cf493d40be9e66ff82f." This matches the commit hash in the current METADATA.pb.

Commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` exists in the upstream repo cache and is dated September 5, 2025 (a merge of "Fix ligatures" PR #37). This is the Ink variant family which was added separately from the non-Ink Bitcount families.

The upstream repo does have a `sources/config.yaml` file but it only contains `familyName: Bitcount`, which is insufficient as a gftools-builder config. An override `config.yaml` is present in the google/fonts family directory (`ofl/bitcountgriddoubleink/config.yaml`) with content:
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Double Ink
buildVariable: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists in the google/fonts directory, the `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb source block is complete. The commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` is confirmed as the onboarding commit. An override `config.yaml` is present in the google/fonts family directory. No action needed.
