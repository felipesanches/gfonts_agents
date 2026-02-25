# Investigation: Verification of 724 METADATA.pb Updates (PR #10270)

**Date**: 2026-02-25
**Status**: Complete — PR submitted
**PR**: https://github.com/google/fonts/pull/10270

## Summary

Prepared and verified METADATA.pb source block updates for 724 font families in the google/fonts repository. All changes add or update `repository_url`, `commit`, and `config_yaml` fields.

## Verification Methodology

### Commit hash verification
1. **Local cache verification** (1797 families): Used `git cat-file -t <commit>` against cached repos in `/mnt/shared/upstream_repos/fontc_crater_cache/`
2. **GitHub API verification** (26 families): For repos not in cache, used `gh api repos/{owner}/{repo}/commits/{commit}` to verify commit existence
3. **Spot-check sampling**: Randomly sampled 20 families from the PR changes for detailed verification

### Results
- 1797 commits verified locally
- 26 commits verified via API
- 2 commits failed verification:
  - **Red Hat Display/Mono/Text**: bghryct repos deleted (404), commits from old repos don't exist in RedHatOfficial/RedHatFont — **removed from PR**
  - **Raleway**: Commit 7b288c6f not in current repo history (possible force-push) — **not in PR** (data already in METADATA.pb)

### PR contents breakdown

| Change Type | Count |
|---|---|
| Add commit hash to existing source block | 82 |
| Add complete source block (repo URL + commit + config_yaml) | 27 |
| Add config_yaml path to existing source block | 12 |
| Add commit + config_yaml to existing source block | 4 |
| Add source block with repo URL + commit only | 599 |
| **Total** | **724** |

### What was excluded
- 3 Red Hat fonts (unverifiable commits from deleted repos)
- 56 no_upstream_repo families (no URL to add)
- 1131 families already correct in METADATA.pb
- 33 missing_config families already with complete source blocks
- 1 family (Meera Inimai) with unknown commit on GitLab

## Risk Assessment

- **Low risk** for 82 commit-only additions: Source blocks already exist and are validated
- **Medium risk** for 599 new source blocks: These use date-correlated commits which may not be exact
- **Low risk** for 27 complete source blocks: These include verified config_yaml paths

## Confidence

**High overall**: All commit hashes verified against upstream repos. The main uncertainty is whether date-correlated commits exactly match the builds deployed in google/fonts (they represent upstream HEAD at onboarding time, which is the best available approximation).
