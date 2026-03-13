# Investigation: Reproducible Font Build System — Phase 1 MVP

**Date**: 2026-03-13
**Status**: Phase 1 Complete — MVP implemented and validated with Alata
**Model**: Claude Opus 4.6

## Summary

With 100% upstream_info.md coverage across all 1,975 ofl/ families now complete, we built a system to validate that `METADATA.pb` source stanzas (repository_url, commit) are correct by actually building fonts from upstream sources and comparing them to the binaries shipped in google/fonts.

The system downloads source snapshots from GitHub at the exact commit recorded in METADATA.pb, builds them with `gftools-builder`, and performs a three-level binary comparison (SHA256 → TTX table diff → mismatch categorization) against the reference fonts in google/fonts.

## Architecture

### Components

| File | Location | Purpose |
|------|----------|---------|
| `reproducible_build.py` | `build_tools/` on `build_system` branch of `felipesanches/fonts` | Build orchestration script |
| `build_registry.json` | `build_tools/` on `build_system` branch | Family registry tracking build status and configuration |

### Workspace (transient, not committed)

```
/mnt/shared/gfonts-repro-builds/{family}/
  source/{repo}-{commit}/     # Extracted source tarball
  comparison_report.json      # Per-family diff report
  build_log.txt               # gftools-builder stdout/stderr
```

### Build Pipeline (per family)

1. **Parse METADATA.pb** — extract `source.repository_url`, `source.commit`, `source.files`, `source.config_yaml`
2. **Download source snapshot** — GitHub tarball at `https://github.com/{owner}/{repo}/archive/{commit}.tar.gz` (avoids full git clone)
3. **Resolve config.yaml** — checks google/fonts override first, then METADATA.pb path, then common fallback locations
4. **Run `gftools-builder`** — invokes via subprocess using the shared gftools venv (with PATH set correctly for fontmake/ninja)
5. **Compare binaries** — SHA256 hash first; if mismatch, TTX table-by-table diff
6. **Categorize mismatch** — classifies based on which tables differ
7. **Update registry** — writes result back to `build_registry.json`
8. **Write report** — per-family JSON report in workspace

### Binary Comparison (3 levels)

| Level | Method | Result |
|-------|--------|--------|
| 1 | SHA256 hash match | `"yes"` (byte-identical) — done |
| 2 | TTX dump per table | Identifies which tables differ |
| 3 | Table classification | Maps differing tables to mismatch category |

### Mismatch Categories

| Category | Meaning |
|----------|---------|
| `"yes"` | Byte-identical build |
| `"timestamp-diff"` | Only `head` table timestamps differ |
| `"hinting-diff"` | Hinting instructions differ (fpgm/prep/cvt) |
| `"name-table"` | Name table metadata differs |
| `"table-ordering"` | Tables semantically identical but ordered differently |
| `"dsig-diff"` | DSIG table present/absent |
| `"compiler-version"` | Broad differences suggesting different fontmake/fontTools version |
| `"source-mismatch"` | Built fonts have different glyphs/outlines |
| `"metadata-stanza-wrong"` | METADATA.pb has wrong repo/commit (e.g. 404 on download) |
| `"build-failure"` | gftools-builder failed |
| `"missing-source"` | No source block or incomplete source block in METADATA.pb |

### Isolation Strategy

- **`"shared"`** (default): uses `/mnt/shared/gftools/venv/bin/gftools-builder` directly
- **`"custom"`**: creates a one-off venv with specific pinned dependency versions (for families that need older fontmake, etc.)

## Registry Format

```json
{
  "version": 1,
  "families": {
    "alata": {
      "enabled": true,
      "isolation": "shared",
      "reproducible_build": "source-mismatch",
      "notes": "",
      "overrides": {}
    }
  }
}
```

The `overrides` field supports `commit` (use a different commit than METADATA.pb), `config_yaml_path`, and `requirements` (for custom venv pinned deps).

## Phase 1 Test: Alata

**Family**: Alata (`ofl/alata`)
- Single static TTF: `Alata-Regular.ttf`
- Source: `SorkinType/Alata` at commit `3b051d2a6181deba154717cfd6be409effe32ffa`
- Config: `sources/config.yaml` (from upstream repo)

### Results

| Metric | Value |
|--------|-------|
| Source download | Successful (GitHub tarball) |
| Build | Successful (gftools-builder with shared venv) |
| Byte-identical | No |
| Differing tables | `GDEF`, `GPOS`, `GSUB`, `glyf`, `head`, `name` |
| Category | `source-mismatch` |

### Analysis

The broad set of differing tables (glyf, GPOS, GSUB, GDEF, head, name) strongly suggests the fonts in google/fonts were built with a different version of fontmake/glyphsLib than the current gftools venv. This is expected — the Alata fonts were likely built and onboarded years ago with whatever fontmake was current at the time.

The `source-mismatch` categorization is technically correct (the glyph outlines differ at the binary level), but the cause is almost certainly compiler version differences rather than wrong source metadata. Refining this distinction is planned for Phase 2, where we can compare across many families to identify patterns.

### Key Implementation Detail

gftools-builder invokes `fontmake` and `ninja` as subprocesses. The build initially failed with `FileNotFoundError: 'fontmake'` because the gftools venv `bin/` directory was not on the subprocess's PATH. The fix was to prepend the venv bin directory to the PATH environment variable passed to the subprocess.

## Next Steps (Phase 2)

1. Enable 5–10 more families (mix of static/variable, simple/complex builds)
2. Refine mismatch categorization based on real data patterns
3. Distinguish "compiler version" from true "source mismatch" more precisely
4. Begin tracking cross-family patterns (e.g., which fontmake versions produce which differences)

## CLI Usage

```bash
# Build one family
python build_tools/reproducible_build.py --family alata

# Build all enabled families in registry
python build_tools/reproducible_build.py --all

# Force rebuild (ignore existing results)
python build_tools/reproducible_build.py --family alata --force
```

## Confidence

**High** for the pipeline mechanics — download, build, compare, and categorize all work correctly end-to-end.

**Medium** for mismatch categorization accuracy — the current heuristic maps differing table sets to categories, but needs more data points to validate. The `source-mismatch` vs `compiler-version` boundary in particular needs refinement with more families.
