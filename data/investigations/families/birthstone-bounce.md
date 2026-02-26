# Investigation Report: Birthstone Bounce

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Birthstone Bounce |
| Designer | Robert Leuschke |
| License | OFL |
| Repository URL | https://github.com/googlefonts/birthstone-bounce |
| Commit | `db48de44b60017495c71a024aa2c079d70869225` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| Date Added | 2021-09-02 |
| Status | Complete |

## How URL Found

The repository URL `https://github.com/googlefonts/birthstone-bounce` was first added by Simon Cozens in commit `f7455d788` ("Populate source.repository_url", August 2023). The copyright field in METADATA.pb also references this URL. The gftools-packager commit message for PR #3793 confirms this URL.

## How Commit Determined

The commit hash `db48de44b60017495c71a024aa2c079d70869225` was sourced from the fontc_crater targets list, ported to METADATA.pb in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list").

### Cross-verification with gftools-packager

The gftools-packager commit `8bd4436fd` (PR #3793, by Viviana Monsalve, September 2021) references a different commit: `f45812daabb656a9d1d8c19c211fc19c26c95c07`. However, this commit does not exist in the upstream repo.

The repo has been squashed to a single commit (`db48de4`, "outline fixes in acute and ring") which is the HEAD and only commit on the `main` branch. This follows the same pattern as the sibling Birthstone repo -- googlefonts repositories that underwent history cleanup.

The fontc_crater targets list uses `db48de4` as the reference commit, which is the only available commit in the repository and therefore the correct one to use.

### Verification that fonts match

The METADATA.pb source block maps two font files from the upstream repo:
- `fonts/ttf/BirthstoneBounce-Regular.ttf`
- `fonts/ttf/BirthstoneBounce-Medium.ttf`

Both files exist at commit `db48de4`.

## Config YAML Status

**Found in upstream at `sources/config.yaml`**

The config at commit `db48de4` contains:
```yaml
sources:
    - BirthstoneBounce.glyphs
familyName: Birthstone Bounce
outputDir: "../fonts"
buildVariable: false
```

This builds static fonts only from `BirthstoneBounce.glyphs`, producing the Birthstone Bounce family with Regular and Medium weights.

## History

1. **2021-09-02**: Birthstone Bounce added to google/fonts (date_added)
2. **2021-09-08**: Added via gftools-packager (commit `8bd4436fd`, PR #3793 by Viviana Monsalve), Version 1.010
3. **2023-08-15**: repository_url added by Simon Cozens (commit `f7455d788`)
4. **2025-03-31**: Commit hash and additional source metadata added from fontc_crater targets list (commit `19cdcec59`)

## Verification

- [x] Repository URL is valid and accessible
- [x] Commit hash exists in upstream repo (HEAD and only commit on main)
- [x] Config YAML exists at `sources/config.yaml` at the recorded commit
- [x] Source block in METADATA.pb is complete with files mapping and branch
- [x] Font files `BirthstoneBounce-Regular.ttf` and `BirthstoneBounce-Medium.ttf` exist at the recorded commit

## Confidence Level

**High** -- All data is verified. The commit hash is the only available commit in the squashed repo and matches fontc_crater's reference. The config.yaml and font files are confirmed present.

## Open Questions

None. The repo history was squashed (common for googlefonts repos), but the current HEAD commit serves as the definitive reference.
