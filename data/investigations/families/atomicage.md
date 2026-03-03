# Investigation: Atomic Age

## Summary

| Field | Value |
|-------|-------|
| Family Name | Atomic Age |
| Slug | atomic-age |
| License Dir | ofl |
| Repository URL | https://github.com/EbenSorkin/Atomic-Age |
| Commit Hash | bb96b179ca5c48149011237c64781fa94817e711 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/EbenSorkin/Atomic-Age"
  commit: "bb96b179ca5c48149011237c64781fa94817e711"
}
```

## Investigation

Atomic Age is a display font by James Grieshaber, published by Sorkin Type Co. It was added to Google Fonts on 2011-10-26 (initial commit `90abd17b4`) and last updated via PR #830 (`892763811`, "hotfix-atomicage: v1.008 added", 2017-08-07) by Marc Foley.

The repository URL `https://github.com/EbenSorkin/Atomic-Age` was added to METADATA.pb by Simon Cozens in commit `46a7c0576` ("Add more upstreams (a,b)", 2024-01-14). The commit hash `bb96b179ca5c48149011237c64781fa94817e711` was added in commit `862210c9f` ("Atomic Age: add source block to METADATA.pb").

The upstream repository is cached at `EbenSorkin/Atomic-Age`. The commit `bb96b179` is the latest (and effectively the final) commit in the repo, dated 2016-01-16, "Merge pull request #3 from davelab6/master". The repo has 14 commits total and has been inactive since 2016.

**Version discrepancy**: The PR #830 hotfix in google/fonts claims v1.008, but the upstream repo only contains up to v1.007 (commit `5e7452c`, "Updating to v1.007 (vertical metrics)", 2016-01-15). The v1.008 changes appear to be direct binary modifications done in google/fonts without corresponding upstream source changes.

**No config.yaml**: The only source file in the repo is `SRC/AtomicAge-Regular.vfb` (FontLab binary format). The original UFO was present and then removed (commit `7190e2a`, "Remove UFO"). No `config.yaml` exists in the upstream repository or in the google/fonts family directory (`ofl/atomicage/`). VFB format is proprietary and not compatible with gftools-builder.

## Conclusion

The repository URL and commit hash are documented in METADATA.pb. However, no config.yaml is possible because the only source file is a proprietary FontLab VFB binary, which is not compatible with gftools-builder. The family needs source file conversion (VFB to UFO or .glyphs) before a config.yaml can be created. Status remains missing_config.
