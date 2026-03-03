# Investigation: Bilbo Swash Caps

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bilbo Swash Caps |
| Slug | bilbo-swash-caps |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/bilboswashcaps |
| Commit Hash | 7fb5653f339a4a574c26a8df75b6e7fac7db9280 |
| Config YAML | none (SFD-only sources, no gftools-compatible source format) |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/bilboswashcaps"
  commit: "7fb5653f339a4a574c26a8df75b6e7fac7db9280"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/librefonts/bilboswashcaps` is already documented in METADATA.pb. The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/bilboswashcaps`.

### Commit Hash

The METADATA.pb records commit `7fb5653f339a4a574c26a8df75b6e7fac7db9280`. The upstream repo shows:

```
7fb5653 update .travis.yml
```

This is a shallow clone with one visible commit. The commit `7fb5653` matches the hash in METADATA.pb. The font was last updated in google/fonts via commit `4c45f1981` ("hotfix-bilboswashcaps: v1.003 added (#858)") dated 2017-08-07. An earlier commit (`c7136cb84`) had done "Updating ofl/bilboswashcaps/*ttf with nbspace and fsType fixes".

### Source Files

The upstream repo contains:
- `src/BilboSwashCaps-Regular-TTF.sfd` — FontForge SFD format (primary source)
- `src/Bilbo-SwashCaps-OTF.vfb` — FontLab VFB format
- Various TTX decomposition files

The primary source format is SFD (FontForge), which is not directly supported by gftools-builder for standard builds. There is no `.glyphs`, `.ufo`, or `.designspace` file. No `config.yaml` is present in the repository.

### Config YAML

No `config.yaml` exists in the upstream repo and no override exists in the google/fonts family directory. The SFD source format is not compatible with standard gftools-builder builds.

## Conclusion

The source block in METADATA.pb is complete with repository URL and commit hash. No config.yaml is possible with the current SFD-only source format. Status is `missing_config`. No action needed unless the sources are converted to a gftools-compatible format.
