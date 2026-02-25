# Investigation: Commit Hash Discovery for 94 Missing-Commit Families

**Date**: 2026-02-25
**Status**: Complete — all 94 families resolved

## Summary

Identified original upstream onboarding commit hashes for 94 font families that had `repository_url` but no `commit` in our tracking data.

## Methodology

### Phase 1: PR body extraction (28 found)
- Identified the last font-modifying commit in google/fonts for each family
- Extracted linked PR numbers from those commits
- Used `gh api` to read PR bodies looking for:
  - gftools-packager commit references (format: `taken from upstream repo ... at commit ...`)
  - Font Bakery Dashboard references (format: `commit: <hash>`)
  - Direct URL references to upstream commits

### Phase 2: Commit message body parsing (12 found)
- For families without linked PRs, examined the git commit message bodies in google/fonts
- Some commits contained explicit upstream commit hashes or version references

### Phase 3: Tag/date correlation (22 found)
- Matched version tags in upstream repos to the font version in google/fonts
- Correlated google/fonts merge dates with upstream commit timestamps
- For repos with few commits, used the latest commit before the onboarding date

### Phase 4: Manual investigation (32 found via the parallel 22-families report)
- Investigated remaining families individually
- Methods included: version tag resolution, date proximity matching, PR description analysis

## Key Findings

### gftools-packager empty commit bug
8 SIL fonts (Alkalami, Ruwudu, Dai Banna SIL, Kay Pho Du, Lisu Bosa, Namdhinggo, Narnoor, Nuosu SIL) + Noto Kufi Arabic, Noto Sans Mono had commit URLs ending with `/commit/.` (empty hash). Fixed by matching version tags in upstream repos.

### Repos with wrong cache paths
- Noto CJK: `googlefonts/noto-cjk` was empty/broken, correct path was `notofonts/noto-cjk`
- Lisu Bosa: Used `silnrsi/font-lisubosa` but correct is `silnrsi/font-lisu-bosa`

## Confidence

- **High** (60+): Commits found via explicit PR body references, version tag matches
- **Medium** (22): Commits found via date correlation (upstream HEAD at onboarding time)
- **Lower** (12): Commits found via commit message parsing or first-commit fallback

## Impact

- missing_commit: 94 → 0 (fully resolved)
