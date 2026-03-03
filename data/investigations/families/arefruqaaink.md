# Investigation: Aref Ruqaa Ink

## Summary

| Field | Value |
|-------|-------|
| Family Name | Aref Ruqaa Ink |
| Slug | aref-ruqaa-ink |
| License Dir | ofl |
| Repository URL | https://github.com/aliftype/aref-ruqaa |
| Commit Hash | cca3d1256a7cc75a451f38e50b870d2d5c1e3ffb |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/aliftype/aref-ruqaa"
  commit: "cca3d1256a7cc75a451f38e50b870d2d5c1e3ffb"
  archive_url: "https://github.com/aliftype/aref-ruqaa/releases/download/v1.005/ArefRuqaa-1.005.zip"
  files {
    source_file: "ArefRuqaa-1.005/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ArefRuqaa-1.005/ttf/ArefRuqaaInk-Regular.ttf"
    dest_file: "ArefRuqaaInk-Regular.ttf"
  }
  files {
    source_file: "ArefRuqaa-1.005/ttf/ArefRuqaaInk-Bold.ttf"
    dest_file: "ArefRuqaaInk-Bold.ttf"
  }
  branch: "main"
}
```

## Investigation

### Repository

The upstream repository `aliftype/aref-ruqaa` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/aliftype/aref-ruqaa`. The same repo serves both Aref Ruqaa and Aref Ruqaa Ink, with different commits referenced. The repository URL is pre-existing in METADATA.pb.

Aref Ruqaa Ink is a color font (COLRv1 and SVG tables) derived from the Aref Ruqaa project.

### Commit Hash

The commit `cca3d1256a7cc75a451f38e50b870d2d5c1e3ffb` was verified present in the cached repo: `git cat-file -t cca3d125` returns `commit`. The commit is dated 2022-07-29 with message "Create FUNDING.yml" by Khaled Hosny. This is not a font release commit; it is the HEAD of the `main` branch at the time of onboarding, used as a reference point alongside the `archive_url` for the actual binary files.

The google/fonts TTF was last updated in commit `0ccdb3e32` ("Update ArefRuqaaInk to v1.005, includes both COLRv1 and SVG color tables (#5107)") on 2022-08-22. The commit body notes: "Files from https://github.com/aliftype/aref-ruqaa/releases/tag/v1.005." This confirms the release archive as the source.

Earlier commits in the google/fonts history for this file include `8fd77aa0b` (color onboarding) and `[gftools-packager] Aref Ruqaa Ink: Version 1.005 added (#4615)`.

### Source Files

At commit `cca3d1256`, the sources directory contains FontForge `.sfdir` files (same as the Aref Ruqaa family at its onboarding commit). The binary fonts were taken from a release archive (`v1.005/ArefRuqaa-1.005.zip`), not compiled from sources.

No config.yaml exists at this commit.

### Config YAML

No config.yaml is present or applicable. The Aref Ruqaa Ink fonts were onboarded from a pre-compiled release archive, not from source compilation. The sources at the referenced commit are in FontForge `.sfdir` format (not gftools-builder compatible), and the current HEAD glyphspackage sources may not produce the color font variant correctly.

## Conclusion

The METADATA.pb source block has repository URL and commit hash, and uses a release archive for the actual binary files. Status is `missing_config` because the source files at the referenced commit are FontForge `.sfdir` format (not gftools-builder compatible), and the font is a color font derived from a release archive rather than a standard gftools-builder compilation.
