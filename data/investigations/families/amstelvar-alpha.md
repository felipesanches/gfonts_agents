# Investigation: Amstelvar Alpha

## Summary

| Field | Value |
|-------|-------|
| Family Name | Amstelvar Alpha |
| Slug | amstelvar-alpha |
| License Dir | ofl |
| Repository URL | https://github.com/TypeNetwork/fb-Amstelvar |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The `ofl/amstelvaralpha/` directory in google/fonts contains no `METADATA.pb` file at all. The directory contains only: `AmstelvarAlpha-VF.ttf`, `DESCRIPTION.en_us.html`, `EARLY_ACCESS.category`, and `OFL.txt`.

The presence of `EARLY_ACCESS.category` indicates this font was added as an early access font before the current google/fonts metadata structure was established.

Git history for the font file shows three commits:
1. `d95e5ec65` (March 28, 2017) — "Add Amstelvar to Early Access (#655)" by Dave Crossland
2. `c0899f11c` (August 14, 2017) — "ofl/amstelvaralpha/AmstelvarAlpha-VF.ttf Updated" by Dave Crossland
3. `0eb39d391` (August 30, 2017) — "ofl/amstelvaralpha/AmstelvarAlpha-VF.ttf Updated (#1184)" by Dave Crossland

All commits are from 2017. None of the commit messages reference a specific upstream commit hash.

The `DESCRIPTION.en_us.html` links to `https://github.com/TypeNetwork/fb-Amstelvar` as the upstream source. The upstream repo is NOT cached in `/mnt/shared/upstream_repos/fontc_crater_cache/TypeNetwork/fb-Amstelvar/` (only `Arimo` and `Assistant` are cached under TypeNetwork).

The `OFL.txt` copyright line reads: "Copyright 2016 The Amstelvar Project Authors (info@fontbureau.com)", confirming the Font Bureau / TypeNetwork origin.

Since there is no METADATA.pb and no EARLY_ACCESS conversion has been done, this family requires:
1. Creating a METADATA.pb with a complete source block
2. Identifying the exact upstream commit used for each of the 2017 binary updates
3. Cloning the upstream repo to investigate its structure and find a config.yaml

## Conclusion

Status is `missing_url` (and also missing commit and METADATA.pb entirely). The upstream repo URL is known from the DESCRIPTION.en_us.html (`https://github.com/TypeNetwork/fb-Amstelvar`) but the repo is not cached locally. A METADATA.pb needs to be created and the upstream commit hash needs to be identified by investigating the TypeNetwork/fb-Amstelvar repository history around August 2017. Confidence is MEDIUM because the upstream URL is documented in the description but the commit is unknown.
