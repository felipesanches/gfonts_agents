# Bungee Inline

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: David Jonathan Ross
**METADATA.pb path**: ofl/bungeeinline/METADATA.pb

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/djrrb/Bungee |
| Commit | eb03cf69adab5094f6b84e95357789cdf3bfeb99 |
| Config YAML | override config.yaml in google/fonts |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/djrrb/Bungee` was already present in the METADATA.pb source block. It was added as part of the "Add more upstreams (a,b)" commit (46a7c057) on 2024-01-14 and confirmed in the Version 2.000 update commit (dccf6212) on 2024-05-30. The URL is valid and points to David Jonathan Ross's Bungee project, which contains all Bungee font variants (Regular, Inline, Outline, Shade, Hairline, Color/Spice/Tint).

## How the Commit Hash Was Identified

The commit hash `eb03cf69adab5094f6b84e95357789cdf3bfeb99` was recorded in the METADATA.pb source block. It was added in the google/fonts commit dccf6212 ("Bungee Inline: Version 2.000 added") by Viviana Monsalve on 2024-05-30. The commit message explicitly states: "Taken from the upstream repo https://github.com/djrrb/Bungee at commit https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99."

This commit was merged via PR #7797 (`google/gftools_packager_ofl_bungeeinline`) on 2024-05-31.

**Verification**: In the upstream repo, commit `eb03cf69` is tagged as `v2.000`. The commit itself ("Bump fontbakery") was authored by Just van Rossum on 2024-05-30. At this commit, the pre-built binary `fonts/Bungee_Basic/BungeeInline-Regular.ttf` existed in the repo tree and was also available via the GitHub release archive at `https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip`.

The binary SHA256 in google/fonts does not match the binary in the upstream repo tree at this commit (google/fonts: `5a07361627376971fa195e8500ec0fc5e0daf7df2f94ba8eb30d1b10ed7e0375`, upstream tree: `491dfdf230b9f3797c616bb902e72f3d4f2e6d245b62f570b7b0f09b0dbe0b7e`). This is expected because the METADATA.pb source block uses `archive_url` with a `files {}` mapping, meaning the binary was taken from the release zip rather than directly from the git tree. The release archive may contain fonts that were rebuilt or post-processed before packaging.

## How Config YAML Was Resolved

The upstream repository does not contain a `config.yaml` file. The Bungee project uses a custom build pipeline (`build.sh`) that calls Python assembly scripts and fontmake, rather than gftools-builder.

An override `config.yaml` was created in the google/fonts family directory (`ofl/bungeeinline/config.yaml`) as part of commit f6c68379a ("Add override config.yaml for 50 font families") on 2026-02-16. The config references the UFO source at the referenced commit:

```yaml
sources:
  - sources/2-build/Bungee_Basic/Bungee-Inline.ufo
familyName: Bungee Inline
buildStatic: true
buildOTF: false
```

**Important note**: The `sources/2-build/` directory was removed from the upstream repo in commit 7ffc5a64 ("remove /fonts folders and /2-build folder") on 2024-06-07, one week after the v2.000 tag. The override config.yaml is only valid when used against the referenced commit `eb03cf69`, where the UFO source still existed at `sources/2-build/Bungee_Basic/Bungee-Inline.ufo`.

Since an override config.yaml exists in the google/fonts family directory, the `config_yaml` field is omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

## Verification

- **Repository URL**: Valid, accessible, and matches the upstream for all Bungee variants.
- **Commit hash**: Matches the v2.000 tag exactly. The google/fonts commit message explicitly references this commit.
- **Branch**: `master` is correct (confirmed via `git branch -a` in the upstream repo).
- **Archive URL**: `https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip` returns HTTP 302 (redirect to CDN), which is normal for GitHub release assets.
- **Override config.yaml**: References `sources/2-build/Bungee_Basic/Bungee-Inline.ufo`, which existed at the referenced commit.
- **Source format**: UFO (sources/2-build/Bungee_Basic/Bungee-Inline.ufo at the referenced commit).
- **Upstream repo is clean**: Working tree clean, up to date with origin/master.

## Confidence

**HIGH** -- The commit hash is explicitly referenced in the google/fonts commit message, matches the v2.000 tag in the upstream repo, and was added via gftools_packager (PR #7797). The repository URL, branch, and archive URL are all verified. The override config.yaml correctly references the UFO source that existed at the tagged commit.
