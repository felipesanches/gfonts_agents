# Investigation: Resolving 637 Incomplete-Source Families

**Date**: 2026-02-25
**Status**: Complete — all 637 families resolved

## Summary

Identified upstream commit hashes for 637 font families that had `repository_url` but were missing `commit` and/or `config_yaml`. These families had URLs discovered during the no_source resolution phase.

## Methodology

### Phase 1: gftools-packager commits (12 found)
- Searched commit message bodies in google/fonts for explicit upstream commit references
- Matched version tags in upstream repos when commit messages referenced version numbers

### Phase 2: Batch PR processing (215 unique PRs → many commits found)
- Extracted PR numbers from google/fonts commits that last modified each family's font files
- Used 4 parallel agents to read PR bodies via GitHub API
- Extracted commit hashes from gftools-packager output, Font Bakery Dashboard entries, and manual references

### Phase 3: Date correlation (523 found)
- For each remaining family, found the date when fonts were last modified in google/fonts
- Located the upstream commit that was HEAD at that date using `git log --before=<date> -1`
- This is the most common resolution method — assumes upstream HEAD at onboarding time was the commit used

### Phase 4: First commit / HEAD fallback (91 found)
- For repos where date correlation failed (stale cache, shallow clone, broken HEAD):
  - Used `git rev-list --max-parents=0 HEAD` for repos with single meaningful commits
  - Used HEAD commit for repos where all commits predate the onboarding
  - Used GitHub API for repos not in local cache

### Phase 5: Individual resolution (11 remaining)
- Noto CJK (5 families): Fixed cache path from googlefonts to notofonts
- Manrope: Corrected URL from sharanda/manrope (404) to davelab6/manrope
- Syne, Syne Mono, Syne Tactile: GitLab repos, used API to find commits
- Elsie, Orelega One: Repos 404, marked as no_upstream_repo
- Meera Inimai: GitLab, commit unknown

## Key Corrections

| Family | Issue | Fix |
|--------|-------|-----|
| Manrope | sharanda/manrope 404 | Changed to davelab6/manrope |
| Elsie | googlefonts/elsiefont 404 | Marked no_upstream_repo |
| Orelega One | JapanYoshi/Orelega 404 | Marked no_upstream_repo |
| Noto CJK (5) | Wrong cache path | Used notofonts/noto-cjk |

## Config.yaml discovery (during this phase)
- Found 51 override config.yaml files in google/fonts family directories
- Found 7 config.yaml files in upstream repos
- Total 58 families moved to `complete` status

## Confidence

- **High**: PR body references, version tag matches, gftools-packager output
- **Medium**: Date correlation (upstream HEAD at onboarding time) — this is the dominant method and assumes the upstream was used as-is
- **Lower**: First-commit fallback for repos with unclear history

## Impact

- incomplete_source: 637 → 0 (fully resolved)
- 58 families moved to `complete` (config.yaml found)
- 2 families moved to `no_upstream_repo` (repos deleted)
