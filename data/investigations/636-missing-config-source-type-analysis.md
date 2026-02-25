# Investigation: Source Type Analysis of 636 Missing-Config Families

**Date**: 2026-02-25
**Status**: Complete — categorization done

## Summary

Analyzed the 636 font families with `missing_config` status to determine which have gftools-builder compatible source files and which cannot have a config.yaml.

## Methodology

### Local cache analysis (591 families)
- Used `git ls-tree -r --name-only <commit>` to list all files at the recorded commit
- Classified source files by extension:
  - gftools-compatible: `.glyphs`, `.glyphspackage`, `.ufo`, `.designspace`
  - FontForge: `.sfd`, `.sfdir`
- Deduplicated UFO/glyphspackage directories (counted directory, not individual files)

### GitHub API analysis (45 non-cached families)
- Used `gh api repos/{owner}/{repo}/git/trees/{commit}?recursive=1` to get file listings
- Applied same classification rules

## Results

| Category | Count | Description |
|---|---|---|
| gftools-buildable | 153 | Have .glyphs, .ufo, or .designspace sources |
| SFD-only | 257 | Only have FontForge .sfd/.sfdir sources |
| No buildable sources | 226 | Binary-only repos or no source files |
| **Total** | **636** | |

### gftools-buildable source type breakdown
| Source Type | Count |
|---|---|
| .glyphs | 93 |
| .ufo | 96 |
| .designspace | 37 |
| .glyphspackage | 2 |

Note: Many families have multiple source types (e.g., both .glyphs and .ufo).

### SFD-only families (257)
These use FontForge's native format. gftools-builder does not support .sfd files directly. Options:
1. Convert to .ufo using sfd2ufo (lossy)
2. Use custom build scripts
3. Accept that these cannot have gftools-builder config

### No buildable sources (226)
These repos contain only:
- Pre-compiled .ttf/.otf binaries
- Documentation, specimens, or web assets
- No font source files at all

## Implications for config.yaml

- **153 gftools-buildable**: Could potentially have config.yaml generated, but requires per-family analysis to identify the correct source file(s)
- **483 non-buildable**: config.yaml is not applicable. These families may need a different tracking status (e.g., `complete_no_config` or similar)

## Confidence

**High**: File type classification is deterministic based on file extensions. The only uncertainty is whether some repos have sources in unusual locations not captured by the extension-based search.
