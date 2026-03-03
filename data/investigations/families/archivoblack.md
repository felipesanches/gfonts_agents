# Investigation: Archivo Black

## Summary

| Field | Value |
|-------|-------|
| Family Name | Archivo Black |
| Slug | archivo-black |
| License Dir | ofl |
| Repository URL | https://github.com/Omnibus-Type/ArchivoBlack |
| Commit Hash | 95df3c54d818473a3e362f30ae3059bd85b80036 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Omnibus-Type/ArchivoBlack"
  commit: "95df3c54d818473a3e362f30ae3059bd85b80036"
}
```

## Investigation

### Repository

The upstream repository `Omnibus-Type/ArchivoBlack` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/Omnibus-Type/ArchivoBlack`. The repository URL is pre-existing in METADATA.pb.

### Commit Hash

The commit `95df3c54d818473a3e362f30ae3059bd85b80036` was verified present in the cached repo: `git cat-file -t 95df3c54` returns `commit`. The commit is dated 2017-06-06 with message "Merge pull request #2 from m4rc1e/canonical" — a merge commit that added canonical filenames for fonts.

The google/fonts TTF was last updated in commit `e723d3178` ("archivoblack: v1.006 added. (#1121)") on 2017-08-07. The commit message contains no upstream commit reference. The source block was added later in commit `94a7d8131` ("Archivo Black: add source block to METADATA.pb") with the note "Commit: 95df3c54 (Merge pull request #2 from m4rc1e/canonical), Config: override config.yaml in google/fonts, Status: missing_config, Confidence: HIGH".

However, the note in that PR commit says "Status: missing_config" — subsequent investigation revealed that an override config.yaml already exists in google/fonts, making this `complete`.

### Source Files

Inspection of the upstream repo at commit `95df3c54` shows the following structure:
- `SRC/Archivo-Black.glyphs` — Glyphs format source
- `SRC/old_src/Archivo Black-Regular.ufo/` — UFO format (older source)
- `Fonts/ArchivoBlack-Regular.ttf` — compiled TTF

The primary source at the referenced commit is `SRC/Archivo-Black.glyphs`.

### Config YAML

An override `config.yaml` exists at `ofl/archivoblack/config.yaml` in google/fonts with contents:

```yaml
sources:
  - SRC/Archivo-Black.glyphs
buildVariable: false
```

This path (`SRC/Archivo-Black.glyphs`) correctly matches the source file location in the upstream repo at commit `95df3c54`. Per policy, `config_yaml` is omitted from METADATA.pb when a local override exists.

## Conclusion

All source metadata is complete. Repository URL and commit hash are present and verified. An override config.yaml exists in google/fonts referencing the correct Glyphs source path. Status is `complete` with HIGH confidence.
