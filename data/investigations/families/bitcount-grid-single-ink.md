# Investigation: Bitcount Grid Single Ink

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Grid Single Ink |
| Slug | bitcount-grid-single-ink |
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
    source_file: "fonts/ttf/variable/BitcountGridSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountGridSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb.

Bitcount Grid Single Ink is one of the Bitcount Ink variant families added to google/fonts separately from the non-Ink families. The onboarding commit for all Ink families is `89e7994f73b7f5ced80e7cf493d40be9e66ff82f`, confirmed by inspecting the initial addition commits for other Ink families (e.g., `5d1b8f3e6` for Bitcount Grid Double Ink, `c020967df` for Bitcount Ink), all of which reference the same upstream commit.

Commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` exists in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount` (dated September 5, 2025, merging "Fix ligatures" PR #37).

The upstream `sources/config.yaml` only contains `familyName: Bitcount`. An override `config.yaml` is present in the google/fonts family directory (`ofl/bitcountgridsingleink/config.yaml`):
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Single Ink
buildVariable: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists in the google/fonts directory, the `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb source block is complete. The commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` is confirmed as the onboarding commit for all Bitcount Ink families. An override `config.yaml` is present in the google/fonts family directory. No action needed.
