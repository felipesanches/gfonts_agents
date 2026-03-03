# Investigation: Almendra Display

## Summary

| Field | Value |
|-------|-------|
| Family Name | Almendra Display |
| Slug | almendra-display |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/almendradisplay |
| Commit Hash | b252e05aada37cc9fe9048ac25e41307b4c9198a |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/almendradisplay"
  commit: "b252e05aada37cc9fe9048ac25e41307b4c9198a"
}
```

## Investigation

### google/fonts commit history

The most recent modification to the TTF file was commit `0bec64a92bc7a492b7f385297756881602facf91`, dated 2017-08-07, authored by Marc Foley with message "hotfix-almendradisplay: v1.004 added (#757)". This PR updated the font binary and METADATA.pb.

The `source {}` block was added later, in commit `d4d0d9ca0f74b70ea98fcb82ffd77e0c659f4427` (authored by Felipe Sanches, dated 2026-02-26), along with `upstream_info.md`. This was part of PR #10271 to document upstream source metadata.

### Upstream repository

The upstream repo `https://github.com/librefonts/almendradisplay` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/almendradisplay/`. The repository has only a single commit:

- `b252e05aada3` — "update .travis.yml" (2014-10-17, by hash3g)

This matches exactly the commit recorded in METADATA.pb.

### Source file types and config.yaml status

The `src/` directory contains:
- `AlmendraDisplay-Regular-TTF.sfd` — FontForge source (TTF variant)
- `AlmendraDisplay-Regular-OTF.vfb` — FontLab source (OTF variant)
- Various `.ttx` files (decomposed binary data)

The primary buildable source is `.sfd` (FontForge) format only. FontForge SFD files are **not compatible with gftools-builder**. The `.vfb` is also not gftools-builder compatible. No `config.yaml` exists in the repository. No override `config.yaml` has been added to the google/fonts family directory `ofl/almendradisplay/`.

Designer: Ana Sanfelippo (anasanfe@gmail.com).

## Conclusion

The `source {}` block in METADATA.pb is complete with correct `repository_url` and `commit` (both verified). No `config.yaml` can be provided because the upstream sources are in FontForge (.sfd) format, which gftools-builder cannot process. Status remains `missing_config`. No further action is possible without source format conversion by the original designer (Ana Sanfelippo).
