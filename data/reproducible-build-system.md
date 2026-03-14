# Investigation: Reproducible Font Build System

**Date**: 2026-03-14
**Status**: 1,258 families tested, 784 with deep analysis (1,266 buildable total, 8 unreachable)
**Model**: Claude Opus 4.6

## Summary

With 100% upstream_info.md coverage across all 1,975 ofl/ families now complete, we built a system to validate that `METADATA.pb` source stanzas (repository_url, commit) are correct by actually building fonts from upstream sources and comparing them to the binaries shipped in google/fonts.

The system downloads source snapshots from GitHub at the exact commit recorded in METADATA.pb, builds them with `gftools-builder`, and performs a multi-level comparison: SHA256 hash, TTX table-by-table diff, mismatch categorization, and deep structural analysis (ttfautohint version detection, per-glyph coordinate comparison, advance width and line metrics reflow risk assessment).

## Current Results (1,258 of 1,266 families tested)

### Status Breakdown

| Status | Count | % of tested | Meaning |
|--------|-------|---|---------|
| **yes** (byte-identical) | 110 | 8.7% | Rebuilt font is bit-for-bit identical to google/fonts |
| **compiler-version** | 652 | 51.8% | Differences from fontmake/fontTools/ttfautohint version |
| **build-failure** | 471 | 37.4% | gftools-builder failed |
| **timestamp-diff** | 13 | 1.0% | Only head timestamps differ |
| **name-table** | 8 | 0.6% | Only name table metadata differs |
| **metadata-stanza-wrong** | 4 | 0.3% | METADATA.pb source stanza is incorrect |

8 families could not be downloaded (network/repository issues). Of the 1,258 families tested, 784 produced comparison reports with deep analysis. The remaining 471 failed to build (no output to compare).

### Byte-Identical Families (110)

These families rebuild to **exactly the same binary** as what's in google/fonts:

- aboreto, abyssinicasil, afacad, afacadflux, akatab, akayakanadaka, akayatelivigala, akshar, albertsans, anekbangla, anekdevanagari, anekgujarati, anekgurmukhi, anekkannada, aneklatin, anekmalayalam, antonio, assistant, average, belleza, bigshoulders, bigshouldersinline, bigshouldersstencil, blackopsone, braahone, cabin, chokokutai, cinzel, cormorantsc, cormorantunicase, courierprime, cuprum, darumadropone, dhurjati, didactgothic, eczar, edunswactfoundation, fanwoodtext, fasterone, faunaone, fjallaone, gildadisplay, goldman, gruppo, gulzar, honk, ibarrarealnova, imbue, imprima, jotione, julee, kanit, kapakana, kiteone, kiwimaru, kulimpark, lacquer, lemon, lexend, lexenddeca, lexendexa, lexendgiga, lexendmega, lexendpeta, lexendtera, lexendzetta, lilex, lindenhill, livvic, majormonodisplay, mallanna, merriweathersans, micro5charted, monofett, montserratunderline, newtegomin, niramit, notosanssyriac, notosanssyriaceastern, notosansvithkuqi, notoserifvithkuqi, offside, opensans, orienta, otomanopeeone, pathwaygothicone, petrona, pottaone, publicsans, quicksand, readexpro, redrose, rowdies, sen, signikasc, slacksideone, strait, tiltprism, tirodevanagarihindi, tirodevanagarimarathi, tirodevanagarisanskrit, trocchi, tsukimirounded, unicaone, unlock, varta, warnes, xanhmono, yrsa, yuseimagic

### Root Cause Breakdown (non-identical font files)

| Root Cause | Font Files | Description |
|-----------|-----------|-------------|
| compiler-output-diff | 380 | fontmake/glyphsLib produces slightly different outlines |
| metadata-only | 265 | Only name/head metadata differs, glyphs identical |
| ttfautohint-version + other | 207 | ttfautohint version change plus minor outline diffs |
| ttfautohint-version | 81 | Pure ttfautohint version difference |

Key insight: **265 font files have metadata-only differences** — zero glyph changes. These families are functionally identical to the google/fonts binaries and safe to rebuild.

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
| **none** | 754 | Safe to rebuild — advance widths and line metrics identical |
| **high** | 170 | Shared glyphs with different advance widths |
| **line-spacing-only** | 8 | Line metrics differ but advance widths identical |
| **minimal** | 1 | Very small advance width differences |

**Artifika** is the only family with genuine reflow risk. The non-breaking space (`uni00A0`) has width 560 in the google/fonts binary but 410 in the rebuild (delta: 150 units). The regular `space` glyph is 560 in both. This appears to be caused by `gftools-fix-font` setting NBSP width to match the source's space width (410) rather than the post-processing width (560). Since NBSP is used in real text, rebuilding Artifika would cause text reflow at every non-breaking space.

Earlier, Alkalami was incorrectly flagged as high risk — see Bug Fix section below.

### Bug Fix: Alkalami False Positive

Alkalami was initially flagged with "high" reflow risk (19 shared glyphs with different advance widths, max delta 279 units). Investigation revealed this was a **bug in the build comparison tool**, not a real issue:

- **Root cause**: The `find_built_font()` function's recursive fallback found `references/Alkalami-Regular.ttf` (a v2.000 reference font shipped in the upstream repo's `references/` directory) instead of the actual build output at `../fonts/ttf/Alkalami-Regular.ttf`.
- **Why**: gftools-builder outputs to `../fonts/ttf/` relative to its working directory, which resolves to `source_dir.parent/fonts/ttf/`. The search function only looked *inside* `source_dir`, so the recursive glob found the old v2.000 reference font first.
- **Fix**: Extended `find_built_font()` to search `source_dir.parent/fonts/` paths, and excluded `references/`, `ref/`, `old/` directories from the recursive fallback.
- **After fix**: Alkalami shows **zero** shared-glyph width diffs, zero glyph name changes, line metrics identical. Reflow risk: **none**.

This bug could affect any upstream repo that ships old reference binaries in a `references/` subdirectory. Three families had such directories (abyssinicasil, akatab, alkalami), but only Alkalami was affected because the other two were byte-identical (correct font found before the fallback triggered).

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

1. **8.7% byte-identical rate across 1,258 families.** 110 families rebuild to the exact same binary. Modern build pipelines (recently onboarded families) reproduce perfectly.

2. **37.4% build failure rate is the biggest challenge.** Many failures are from toolchain version incompatibilities (fontmake API changes, designspace compatibility), repos with their own build system, or repos shipping pre-built fonts.

3. **265 font files with "metadata-only" root cause are functionally reproducible** — zero glyph changes, differences are purely cosmetic (name table version strings, head timestamps).

4. **Prebuild support added.** Some families (42dotsans, astasans, cabin, cairo, cairoplay) require pre-build commands (glyphs2ufo, custom scripts) before gftools-builder. Prebuild support was added with auto-detection of Makefile/build.sh/build.py.

5. **Auto-discovery for missing file mappings.** When METADATA.pb has no `files {}` block, built fonts are matched to reference fonts by filename.

6. **The Alkalami false positive exposed a real bug** in how we locate built fonts. Upstream repos may ship old reference binaries that shadow the actual build output. This is now fixed.

7. **virtiofs FD accumulation mitigated.** Dropping VFS caches every 5 families prevents the ENFILE crash. Download stalls are handled with a 5-minute SIGALRM timeout.

## Infrastructure: virtiofs File Descriptor Issue

### Problem

During Batch 2 processing, the build system crashed with `OSError: [Errno 23] Too many open files in system` while extracting the Anek monorepo tarball (66,677 files). This was traced to a virtiofs/virtiofsd file descriptor accumulation issue.

### Investigation

The build environment is a QEMU/KVM virtual machine with `/mnt/shared` mounted via virtiofs:

```xml
<filesystem type="mount" accessmode="passthrough">
  <driver type="virtiofs"/>
  <source dir="/home/fsanches/devel/claude_vm_shared"/>
  <target dir="shared_from_host"/>
</filesystem>
```

**Key findings:**

- **Guest-side FD limits**: `file-max` = 9.2×10¹⁸ (effectively unlimited), only ~9,000 FDs in use at time of error. The guest kernel was NOT exhausted.
- **Host-side virtiofsd**: Each virtiofsd process has a 1,000,000 FD limit — high but finite.
- **FD leak in virtiofsd**: virtiofsd keeps a host-side FD open for every file/directory the guest accesses. This is by design (prevents TOCTOU security attacks), but FDs are only released when the guest kernel sends FUSE FORGET messages (when VFS cache entries expire).
- **Accumulation pattern**: A single `find` command scanning the Anek extraction (66k files) caused virtiofsd's FD count to jump from 4,528 to 9,774 — and it stayed at 9,774 after the command completed. Over multiple build batches extracting tens of thousands of files, virtiofsd accumulates hundreds of thousands of FDs.
- **virtiofsd version**: 1.13.2 (Debian `trixie`)
- **Host kernel**: 6.18.15+deb14-amd64
- **Guest kernel**: 6.12.73+deb13-amd64

### Root Cause

virtiofsd holds FDs open for the lifetime of the FUSE inode reference. The guest VFS cache retains inode references until memory pressure forces eviction. During font builds, the guest creates/reads tens of thousands of files but never triggers cache eviction, so virtiofsd's FD count grows monotonically. Eventually some system limit (possibly host-side kernel structures or memory) is exhausted, and the error propagates to the guest as ENFILE.

### Mitigation

**Option A (implemented)**: Drop guest VFS caches between build batches by running `echo 3 > /proc/sys/vm/drop_caches`. This triggers FUSE FORGET messages, causing virtiofsd to release accumulated FDs. Added to the build script between family processing.

**Option B (fallback)**: Extract tarballs to guest-local tmpfs (`/tmp`, 17GB RAM-backed), run the build there, and copy only results (comparison_report.json, build_log.txt) to `/mnt/shared`. This avoids virtiofsd ever seeing the intermediate files.

**Option C (last resort)**: Move entire build workspace to local disk. Requires expanding the guest's 19GB root partition.

## VM Maintenance: Resizing a qcow2 Disk Image

If the guest's local disk (19GB root partition) becomes insufficient for Option C or other needs, the qcow2 image can be resized:

```bash
# 1. Shut down the VM
virsh shutdown <vm-name>

# 2. Resize the qcow2 image (e.g., add 50GB)
qemu-img resize /path/to/disk.qcow2 +50G

# 3. Start the VM
virsh start <vm-name>

# 4. Inside the guest, extend the partition and filesystem:
#    For ext4 on the last partition (e.g., /dev/vda1):
sudo growpart /dev/vda 1        # Extend partition to fill disk
sudo resize2fs /dev/vda1        # Extend filesystem to fill partition

# 5. Verify
df -h /
```

If using LVM, use `pvresize`, `lvextend`, and `resize2fs` instead of `growpart`.

## Architecture

### Build Pipeline (per family)

1. **Parse METADATA.pb** — extract `source.repository_url`, `source.commit`, `source.files`, `source.config_yaml`
2. **Download source snapshot** — GitHub tarball (avoids full git clone), 5-minute timeout
3. **Run prebuild commands** — if configured in build_registry.json (e.g. glyphs2ufo, custom scripts)
4. **Resolve config.yaml** — checks google/fonts override first, then METADATA.pb path, then fallbacks
5. **Run `gftools-builder`** — invokes via subprocess using the shared gftools venv
6. **Find built fonts** — explicit file mappings from METADATA.pb, or auto-discovery by filename
7. **Compare binaries** — SHA256 hash first; if mismatch, TTX table-by-table diff
8. **Deep analysis** — ttfautohint version, per-glyph coords, advance widths, line metrics
9. **Categorize** — table-level category + structural root cause + reflow risk
10. **Update registry** — write result back to `build_registry.json`
11. **Write report** — per-family JSON report in workspace cache

### Cache Policy

Build artifacts in `/mnt/shared/gfonts-repro-builds/` serve as a cache. Families with existing results are always skipped unless `--force` is explicitly used. Never rebuild a family that already has results — only use `--force` when the analysis code itself has changed.

### CLI

```bash
python build_tools/reproducible_build.py --family alata       # Build one family
python build_tools/reproducible_build.py --all                 # Build all enabled in registry
python build_tools/reproducible_build.py --batch --limit 50    # Auto-discover and build next 50
python build_tools/reproducible_build.py --family alata --force # Force rebuild
```
