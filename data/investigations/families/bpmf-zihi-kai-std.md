# Investigation: Bpmf Zihi Kai Std

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bpmf Zihi Kai Std |
| Slug | bpmf-zihi-kai-std |
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

Bpmf Zihi Kai Std is a Traditional Chinese standard-script font with Bopomofo phonetic annotations, designed by But Ko, added to Google Fonts on 2026-01-30. It is one of three Bpmf family variants (alongside Huninn and Iansui) from the same upstream repository. Unlike the other two variants, Zihi Kai Std is described as a "New project" (not based on an existing GF font).

### Git History

The font was initially added by google/fonts commit `f91754e81` (2026-01-30, "Adding Bpmf Zihi Kai Std") via PR #10173 by Aaron Bell. This family had the most font binary updates of the three Bpmf variants:
1. First binary: `f91754e81` (2026-01-30) — initial addition
2. Formatting/METADATA: `44d5c78d8`, `c27a727d9`
3. First binary update: `8090ba2c9` (2026-01-30, "Update BpmfZihiKaiStd-Regular.ttf")
4. Second binary update: `72cd1d1f6` (2026-02-09, "Updating with various fixes")
5. Third binary update: `f55b8f2bb` (2026-02-09, "Update BpmfZihiKaiStd-Regular.ttf")
6. Further metadata fixes: `f56ed21ec` (copyright/license URLs), `26417436c` (newline), `3b5debf6e` (URL formatting)

The source block was added by google/fonts commit `96e87d79a` ("Bpmf Zihi Kai Std: add source block to METADATA.pb"), which also added an `upstream_info.md` file.

The commit hash `20f741c18bb917b63576293906c01e82ddfce032` was added by automation commit `9a14639f3` (2026-02-25).

### Upstream Repository

Same situation as the other Bpmf families. The bpmfvs repo (`ButTaiwan/bpmfvs`) is not cached locally. The fonts were built in Aaron Bell's fork (`aaronbell/bpmfvs`). The recorded commit `20f741c18bb` predates the actual build by over a month.

The source of the base ZihiKaiStd font is not documented in `upstream_sources.json` within the bpmfvs repo (unlike Huninn, which comes from `justfont/Huninn`, and Iansui, which comes from `ButTaiwan/iansui`). The base font may be an original creation or sourced separately.

### Build System

Same as all Bpmf families — a custom Ruby-based build system (`make_font.rb`) that is incompatible with gftools-builder. No config.yaml can be created.

### Verification

- Repository URL: Correct as canonical upstream (but fonts were built from Aaron Bell's fork)
- Commit hash: Incorrect — `20f741c` predates the actual build; the last binary update was `f55b8f2bb` (2026-02-09), so the correct commit in `aaronbell/bpmfvs` is from around that date
- Config YAML: Cannot be created (custom Ruby build system)
- Local cache: Neither `ButTaiwan/bpmfvs` nor `aaronbell/bpmfvs` is cached locally
- This family had 3 binary updates (vs 1 each for Huninn and Iansui), suggesting more iteration was needed

## Conclusion

Same fundamental situation as the other Bpmf families. The repository URL points to the canonical upstream but the fonts were built from Aaron Bell's fork. The commit hash is incorrect — the final binary was updated on 2026-02-09 via commit `f55b8f2bb` in google/fonts. Aaron Bell should be asked to confirm the exact commit in `aaronbell/bpmfvs` that produced that binary. No config.yaml can be created. The source of the base ZihiKaiStd font should also be clarified. The status should remain `missing_config` permanently.
