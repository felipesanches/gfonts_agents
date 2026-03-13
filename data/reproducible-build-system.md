# Investigation: Reproducible Font Build System

**Date**: 2026-03-13
**Status**: Batch 1 complete — 63 families processed (1,266 buildable total)
**Model**: Claude Opus 4.6

## Summary

With 100% upstream_info.md coverage across all 1,975 ofl/ families now complete, we built a system to validate that `METADATA.pb` source stanzas (repository_url, commit) are correct by actually building fonts from upstream sources and comparing them to the binaries shipped in google/fonts.

The system downloads source snapshots from GitHub at the exact commit recorded in METADATA.pb, builds them with `gftools-builder`, and performs a multi-level comparison: SHA256 hash, TTX table-by-table diff, mismatch categorization, and deep structural analysis (ttfautohint version detection, per-glyph coordinate comparison, advance width and line metrics reflow risk assessment).

## Batch 1 Results (63 of 1,266 families)

### Status Breakdown

| Status | Count | % | Meaning |
|--------|-------|---|---------|
| **yes** (byte-identical) | 9 | 14% | Rebuilt font is bit-for-bit identical to google/fonts |
| **compiler-version** | 30 | 48% | Differences from fontmake/fontTools/ttfautohint version |
| **build-failure** | 22 | 35% | gftools-builder failed |
| **name-table** | 1 | 2% | Only name table metadata differs |
| **timestamp-diff** | 1 | 2% | Only head timestamps differ |

### Byte-Identical Families (9)

These families rebuild to **exactly the same binary** as what's in google/fonts:

- aboreto, abyssinicasil, afacad, afacadflux, akatab, akayakanadaka, akayatelivigala, akshar, albertsans

This confirms their METADATA.pb source stanzas are 100% correct AND the current gftools toolchain produces identical output. These families are fully reproducible.

### Near-Identical Families (2)

- **alansans**: only name table metadata differs (likely version string)
- **alyamama**: only head timestamps differ (cosmetically meaningless)

These are effectively correct builds — the differences are trivial and don't affect rendering.

### Root Cause Breakdown (non-identical font files)

| Root Cause | Font Files | Description |
|-----------|-----------|-------------|
| compiler-output-diff | 18 | fontmake/glyphsLib produces slightly different outlines |
| ttfautohint-version + other | 17 | ttfautohint version change plus minor outline diffs |
| metadata-only | 15 | Only name/head metadata differs, glyphs identical |
| ttfautohint-version | 12 | Pure ttfautohint version difference |

Key insight: **15 font files have metadata-only differences** — zero glyph changes. These families are functionally identical to the google/fonts binaries and safe to rebuild.

### Build Failure Analysis (22 families, 35%)

| Failure Type | Count | Families |
|-------------|-------|----------|
| Designspace compatibility | 5 | amaranth, amaticsc, amiri, amiriquran, fraunces |
| Missing source files | 3 | abhayalibre, amarna, amethysta |
| Glyph processing errors | 3 | alegreyasans, alegreyasanssc, worksans |
| Missing Python modules | 1 | alegreya (ufo2ft.filters.addExtremes) |
| Cyclical component refs | 1 | alegreyasc |
| Feature compilation | 1 | amita |
| Other fontmake errors | 4 | alkatra, alumnisansinlineone, alumnisanspinstripe, adventpro |
| Unknown/no config | 4 | 42dotsans, amiko, cabin, poppins |

The **35% build failure rate** is significant. Main causes:
1. **Designspace compatibility**: current fontmake is stricter about master compatibility than the version used to originally build these fonts
2. **Missing source files**: config.yaml references files not present at the recorded commit
3. **Module/API changes**: newer fontmake/glyphsLib has removed or renamed APIs

## Reflow Risk Analysis

### Why this matters

The fonts in google/fonts are what billions of users see via the Google Fonts API. If we ever need to rebuild a font from source (to fix a bug, add glyphs, update metadata), and the rebuild produces different metrics, we risk **text reflow** on existing websites — buttons overflow, text wraps differently, headings shift.

### What we measure

1. **Advance widths (hmtx)** — the horizontal width of each glyph. If these change for any cmap-reachable glyph, text reflows.
2. **Line metrics (hhea + OS/2)** — ascent, descent, lineGap. If these change, line spacing changes.

We distinguish between:
- **Shared-glyph width diffs**: same glyph, different advance width = actual reflow risk
- **Glyph name changes**: glyph exists in only one font (renamed by newer glyphsLib) = NOT a reflow risk

### Results

| Risk Level | Font Files | Meaning |
|------------|-----------|---------|
| **none** | 61 | Safe to rebuild — advance widths and line metrics identical |
| **high** | 1 | Alkalami: 19 shared glyphs have different advance widths |

**Alkalami** is the first family flagged with genuine reflow risk. 19 glyphs (including `approxequal`, `greater`, `greaterequal`) have different advance widths (max delta: 28 units). Rebuilding this family with the current toolchain would cause text reflow.

### Risks to Monitor When Rebuilding

| Difference Type | Visual Impact | Reflow Impact |
|----------------|--------------|---------------|
| ttfautohint version | Possible subtle hinting changes on Windows at small sizes | None |
| Glyph coordinate rounding (<=1 unit) | Invisible | None |
| Glyph name changes | None (internal only) | None |
| Head timestamps | None | None |
| Name table version strings | None | None |
| OS/2 panose values | None (classification metadata) | None |
| **Advance width changes** | **Character spacing changes** | **HIGH — text reflows** |
| **Line metric changes** | **Line spacing changes** | **HIGH — all text reflows** |

## Key Insights

1. **14% byte-identical rate is encouraging.** As more recently onboarded families are tested, this rate should increase.

2. **The 35% build failure rate needs investigation.** Many failures are from toolchain version incompatibilities. The `"custom"` isolation mode (pinned venv) could resolve some.

3. **Reflow risk is rare but real.** Only 1 of 62 font files shows actual advance width changes. The assessment caught Alkalami, which would cause layout breakage if rebuilt naively.

4. **15 font files with "metadata-only" root cause are functionally reproducible** — zero glyph changes, differences are purely cosmetic.

## Architecture

### Build Pipeline (per family)

1. **Parse METADATA.pb** — extract `source.repository_url`, `source.commit`, `source.files`, `source.config_yaml`
2. **Download source snapshot** — GitHub tarball (avoids full git clone)
3. **Resolve config.yaml** — checks google/fonts override first, then METADATA.pb path, then fallbacks
4. **Run `gftools-builder`** — invokes via subprocess using the shared gftools venv
5. **Compare binaries** — SHA256 hash first; if mismatch, TTX table-by-table diff
6. **Deep analysis** — ttfautohint version, per-glyph coords, advance widths, line metrics
7. **Categorize** — table-level category + structural root cause + reflow risk
8. **Update registry** — write result back to `build_registry.json`
9. **Write report** — per-family JSON report in workspace cache

### Cache Policy

Build artifacts in `/mnt/shared/gfonts-repro-builds/` serve as a cache. Families with existing results are always skipped unless `--force` is explicitly used. Never rebuild a family that already has results — only use `--force` when the analysis code itself has changed.

### CLI

```bash
python build_tools/reproducible_build.py --family alata       # Build one family
python build_tools/reproducible_build.py --all                 # Build all enabled in registry
python build_tools/reproducible_build.py --batch --limit 50    # Auto-discover and build next 50
python build_tools/reproducible_build.py --family alata --force # Force rebuild
```
