# Investigation: Bpmf Huninn

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bpmf Huninn |
| Slug | bpmf-huninn |
| License Dir | ofl |
| Repository URL | https://github.com/ButTaiwan/bpmfvs |
| Commit Hash | 20f741c18bb917b63576293906c01e82ddfce032 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/ButTaiwan/bpmfvs"
  commit: "20f741c18bb917b63576293906c01e82ddfce032"
}
```

## Investigation

Bpmf Huninn is a Traditional Chinese font with Bopomofo phonetic annotations, designed by But Ko and justfont, added to Google Fonts on 2026-01-30. It is one of three Bpmf family variants (alongside Iansui and Zihi Kai Std) from the same upstream repository.

### Git History

The font was initially added by google/fonts commit `423e25002` (2026-01-30) via PR #10171 by Aaron Bell. The font binary was later updated by commit `15555bd43` (2026-02-09, "Update BpmfHuninn-Regular.ttf - Updating with various fixes"). Further metadata-only fixes followed (`d0ec3026e`, `cc204af75`, `d6f37786b`, `308c0a0a5`).

The source block was added by google/fonts commit `928c4bbe9` ("Bpmf Huninn: add source block to METADATA.pb"), which also added an `upstream_info.md` file documenting the investigation.

The commit hash `20f741c18bb917b63576293906c01e82ddfce032` was added by automation commit `9a14639f3` (2026-02-25).

### Upstream Repository

The bpmfvs repo (`ButTaiwan/bpmfvs`) is not cached locally (not found in `/mnt/shared/upstream_repos/fontc_crater_cache/ButTaiwan/`). The fonts were actually built in Aaron Bell's fork at `https://github.com/aaronbell/bpmfvs`, with the intent to transition back to `ButTaiwan/bpmfvs` after other fonts are updated.

The recorded commit `20f741c18bb` is the HEAD of `ButTaiwan/bpmfvs` from 2025-12-13 ("Update build-ttf.yml"). However, the actual font binary was built from a commit in `aaronbell/bpmfvs` from around 2026-02-09 — at least 2 months later. The recorded commit hash is therefore incorrect for the actual binary.

### Build System

The Bpmf project uses a custom Ruby-based build system (`make_font.rb`). The build process:
1. Takes base font TTFs as input (Huninn base from `github.com/justfont/Huninn`)
2. Uses `otfccdump`/`otfccbuild` to manipulate font data
3. Adds Bopomofo phonetic annotations via IVS (Ideographic Variation Sequences)

This is fundamentally incompatible with gftools-builder. No config.yaml can be created for this family.

### Verification

- Repository URL: Correct as canonical upstream (but fonts were actually built from Aaron Bell's fork)
- Commit hash: Incorrect — `20f741c` predates the actual build by ~2 months; the correct commit is in `aaronbell/bpmfvs` around 2026-02-09
- Config YAML: Cannot be created (custom Ruby build system, incompatible with gftools-builder)
- Local cache: Neither `ButTaiwan/bpmfvs` nor `aaronbell/bpmfvs` is cached locally

## Conclusion

The repository URL points to the canonical upstream but is not the repo from which the fonts were actually built. The commit hash is incorrect — the actual build was performed in Aaron Bell's fork (`aaronbell/bpmfvs`) from a commit around 2026-02-09. Aaron Bell should be asked to confirm the exact commit used. No config.yaml can ever be created for this family due to its custom Ruby-based build system. The status should remain `missing_config` permanently.
