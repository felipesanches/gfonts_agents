# Investigation: Bubbler One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bubbler One |
| Slug | bubbler-one |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/bubblerone |
| Commit Hash | be2343608e5751bca73956b02860a1758e1e29a7 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/bubblerone"
  commit: "be2343608e5751bca73956b02860a1758e1e29a7"
}
```

## Investigation

The source block was added to METADATA.pb in google/fonts commit `a417930da` ("Bubbler One: add source block to METADATA.pb", Felipe Sanches, 2026-02-26). The commit metadata records: "Config: none (SFD-only sources), Status: missing_config, Confidence: MEDIUM".

The upstream repository URL `https://github.com/librefonts/bubblerone` is from the `librefonts` GitHub organization, which hosts archived copies of early Google Fonts source projects. The repository is cached at `upstream_repos/fontc_crater_cache/librefonts/bubblerone/`.

The commit `be2343608e5751bca73956b02860a1758e1e29a7` is the **only commit** in the repository (message: "update .travis.yml", by hash3g, 2014-10-17). Since there is only one commit, the identification is unambiguous.

The font has a history of direct updates in google/fonts:
1. Initial commit `90abd17b4` (2012)
2. Hotfix PR #867 (`70a30639c`, "hotfix-bubblerone: v1.002 added")
3. Compliance fixes (`011460f75`, "Several hotfixes to bring font into compliance (mainly vertical metrics)")
4. Version bump (`078516296`, "Bumped version")

These updates were done directly in google/fonts, not by pulling from the librefonts archive. The current binary in google/fonts does NOT correspond to the SFD source in the archive.

The source file in the repository is:
- `src/BubblerOne-Regular-TTF.sfd` (FontForge SFD format)

This is a legacy format not compatible with gftools-builder. No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory.

## Conclusion

The source metadata (repository_url and commit) is present and correct in METADATA.pb. The status is `missing_config` because the upstream repo only contains SFD sources which cannot be used with gftools-builder. Additionally, the font binary in google/fonts has been updated multiple times after the librefonts archive was created, so the compiled font does not correspond to the archived sources. No override config.yaml is possible without first converting sources to a gftools-compatible format.
