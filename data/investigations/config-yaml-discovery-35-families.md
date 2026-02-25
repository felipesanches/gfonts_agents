# Investigation: Config.yaml Discovery for 35 Font Families

**Date**: 2026-02-25
**Status**: Complete

## Summary

Checked upstream repositories for config.yaml files to resolve the `missing_config` status. Found config.yaml in 35 families across two phases.

## Methodology

### Phase 1: Initial 44 families (from beads issue gfonts_agents-4i9)
- Checked each upstream repo's local cache for config.yaml at the repo root, `sources/`, and `source/` directories
- Verified file existence at the recorded commit hash using `git ls-tree`

### Phase 2: Remaining 636 families
- Batch-checked all 614 cached repos using `git ls-tree -r --name-only <commit>` to find any file ending in `config.yaml`
- Checked 45 non-cached repos via GitHub API (`repos/{owner}/{repo}/git/trees/{commit}`)
- Also checked repos at HEAD for config.yaml added after the recorded commit

## Results

### Phase 1: 12 families found
From the original 44 missing_config families (those that previously had no URL/commit):
- Families with config.yaml in upstream: 12 (various repos)
- Families without: 32 (documented as genuinely missing)

### Phase 2: 23 families found at recorded commit
| Family | Config Path | Repo |
|--------|------------|------|
| Chiron GoRound TC | scripts/config.yaml | nicowillis/ChironGoRoundTC |
| Khmer | sources/config.yaml | notofonts/khmer |
| Noto Sans Arabic UI | sources/config.yaml | notofonts/arabic |
| Noto Sans Bengali UI | sources/config.yaml | notofonts/bengali |
| Noto Sans Devanagari UI | sources/config.yaml | notofonts/devanagari |
| Noto Sans Display | sources/config.yaml | notofonts/latin-greek-cyrillic |
| Noto Sans Gujarati UI | sources/config.yaml | notofonts/gujarati |
| Noto Sans Gurmukhi UI | sources/config.yaml | notofonts/gurmukhi |
| Noto Sans Kannada UI | sources/config.yaml | notofonts/kannada |
| Noto Sans Khmer UI | sources/config.yaml | notofonts/khmer |
| Noto Sans Lao UI | sources/config.yaml | notofonts/lao |
| Noto Sans Malayalam UI | sources/config.yaml | notofonts/malayalam |
| Noto Sans Myanmar UI | sources/config.yaml | notofonts/myanmar |
| Noto Sans Oriya UI | sources/config.yaml | notofonts/oriya |
| Noto Sans Sinhala UI | sources/config.yaml | notofonts/sinhala |
| Noto Sans Tamil UI | sources/config.yaml | notofonts/tamil |
| Noto Sans Telugu UI | sources/config.yaml | notofonts/telugu |
| Noto Sans Thai UI | sources/config.yaml | notofonts/thai |
| Noto Serif Display | sources/config.yaml | notofonts/latin-greek-cyrillic |
| Noto Serif Myanmar | sources/config.yaml | notofonts/myanmar |
| Rubik Mono One | sources/config.yaml | googlefonts/rubik |
| Rubik One | sources/config.yaml | googlefonts/rubik |
| Signika Negative SC | sources/config.yaml | googlefonts/signika |

### Additional findings
- 0 repos had config.yaml added after the recorded commit (only 2 had `shaping-config.yaml` test files)
- 45 non-cached repos: 0 had config.yaml via GitHub API

## Confidence

**High**: All config.yaml paths were verified by checking file existence at the exact recorded commit hash using `git ls-tree`.

## Impact

- 35 families moved from `missing_config` to `complete`
- Remaining 636 missing_config categorized by source type
