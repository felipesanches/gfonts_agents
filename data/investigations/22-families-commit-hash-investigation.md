# Investigation: Upstream Commit Hashes for 22 Font Families

**Date**: 2026-02-25
**Status**: Complete - all 22 families resolved

## Summary

Investigated 22 font families that were missing upstream commit hashes in `data/gfonts_library_sources.json`. Used a combination of strategies:
- Tag matching (version tags in upstream repos)
- Date correlation (upstream commits matching google/fonts PR merge dates)
- PR body investigation (gftools-packager commit references)
- Commit history analysis (finding "Compile" or "regenerated fonts" commits)

## Results

### 1. Amaranth
- **Upstream**: googlefonts/amaranth
- **Commit**: `f4f60a57f54a04186030913a86e3e56105bbe848`
- **Method**: Latest commit in upstream (2017-07-21), all commits are from the same day. Used for gfonts PR #759 merged 2017-08-07.

### 2. Amethysta
- **Upstream**: cyrealtype/Amethysta
- **Commit**: `10ae36bc060bec28f1c504c42ce6871b7c034add`
- **Method**: Second commit (2016-04-06, adds sample image). Font files present since initial commit (2016-01-10). Used for gfonts PR #760 merged 2017-08-07. Third commit (2024) is much later.

### 3. Arsenal
- **Upstream**: alexeiva/Arsenal
- **Commit**: `878af0840749599133561eb6579d84f5c94f58f5`
- **Method**: m4rc1e's commit "fixed copyright string" (2016-12-06) was on a branch (PR #6) used for gfonts PR #507 merged same day. Later merged to master as ec148f6 in March 2017.

### 4. Chakra Petch
- **Upstream**: m4rc1e/Chakra-Petch
- **Commit**: `6176529d05acf654f31e024daad77966319e499d`
- **Method**: Latest commit before the gfonts commit date (2018-08-23) "Updated vertical metrics to stop first line clipping". The gfonts commit was "chakrapetch: unhinted fonts" from Sep 2018.

### 5. Dela Gothic One
- **Upstream**: syakuzen/DelaGothic
- **Commit**: `da8b03e57a8977132b3d0358c48c8463374c74ab`
- **Method**: Latest commit "Updated ttf" (2021-03-29). Version 1.005 used in gfonts PR #3618 merged 2021-08-26. PR mentions designer name correction and version bump.

### 6. Fira Code
- **Upstream**: tonsky/FiraCode
- **Commit**: `8da49d55f8b5978c5f888dd85452b79aad16cca2`
- **Method**: Tag "5.2" resolves directly to this commit (2020-06-12). Gfonts PR #3786 "Updating to Fira Code 5.2" merged 2021-09-08.

### 7. Hind Guntur
- **Upstream**: itfoundry/hind-guntur
- **Commit**: `d1f95f8d9a6013297a6a63cc54e48e3885eb5813`
- **Method**: HEAD commit "Compile 1.000" (2015-10-17). The upstream repo has no v1.001 commits. The gfonts PR #892 (hotfix v1.001, 2017) and PR #2378 (re-hinting, 2020) modified fonts on the gfonts side.

### 8. Hind Madurai
- **Upstream**: itfoundry/hind-madurai
- **Commit**: `3f3bd222489daea4dfec65d5de86012ed4819b5b`
- **Method**: HEAD commit "Compile 1.000" (2015-10-17). Same situation as Hind Guntur.

### 9. Hind Siliguri
- **Upstream**: itfoundry/hind-siliguri
- **Commit**: `affb7dbd00dc554c33ecafc92cbfef5323ae5235`
- **Method**: HEAD commit "Merge branch develop" (2015-10-17) containing "Compile 1.000". Same situation as other Hind families.

### 10. Hind Vadodara
- **Upstream**: itfoundry/hind-vadodara
- **Commit**: `d1972e4ebebc3a65feef2f66823a83444469ece4`
- **Method**: HEAD commit "Compile 1.000" (2015-10-17). Same situation as other Hind families.

### 11. Jacques Francois
- **Upstream**: cyrealtype/Jacques-Francois
- **Commit**: `bc37f476a7e982327ae359c67068356597cd45aa`
- **Method**: Initial commit (2016-01-10). Font was added to google/fonts in 2012, before the upstream repo existed. The v1.100 tag (2018) was never pushed to google/fonts.

### 12. Jacques Francois Shadow
- **Upstream**: cyrealtype/Jacques-Francois-Shadow
- **Commit**: `90c9f94cc747ac7c356d882d7553c07d344992f8`
- **Method**: Initial commit (2016-01-10). Same situation as Jacques Francois.

### 13. Josefin Sans
- **Upstream**: googlefonts/josefinsans
- **Commit**: `bf6907e3a34924300dd407201262f62c2fc2a642`
- **Method**: Merge PR #22 "Updating to UFR build format" (2021-07-29). Used for gfonts PR #3664 "Josefin Sans v2.001 (stat fix)" merged 2021-08-26. PR body says "Font repro updated to the UFR format".

### 14. Lalezar
- **Upstream**: BornaIz/Lalezar
- **Commit**: `238701c4241f207e92515f845a199be9131c1109`
- **Method**: Only commit visible on default branch: Merge PR #12 from m4rc1e/gf "v1.004 mastered for GF" (2017-02-28). Used for gfonts PR #682 merged 2017-05-01.

### 15. Libre Caslon Text
- **Upstream**: thundernixon/Libre-Caslon
- **Commit**: `52200a76d723e4a8cb9a566686ed1f56a794f39a`
- **Method**: Latest commit "Make all italic styles available in VF on mac" (2020-06-10, day before PR merge). Used for gfonts PR #2432 merged 2020-06-11. PR body references this repo.

### 16. Lobster
- **Upstream**: impallari/The-Lobster-Font
- **Commit**: `0796aa8aa42f6cbc89fa61be4a2a12fdcd2b8998`
- **Method**: Commit "regenerated fonts" for v.2.100 (2017-10-27) from cyrealtype contribution. Gfonts PR #1296 says "Taken from GF Repo googlefonts/The-Lobster-Font" which has the same content (commit 2cb456902bee is the merge of cyrealtype's work). The impallari repo has the same v2.100 commits on master.

### 17. Mingzat
- **Upstream**: silnrsi/font-mingzat
- **Commit**: `bfe7e714b737d9d0b3b43ad88e3b844449175560`
- **Method**: v1.100 tag commit "Update FONTLOG release date" (2022-05-19). Gfonts PR #4721 merged 2022-06-01. The gftools-packager text had an empty commit hash field.

### 18. Nabla
- **Upstream**: justvanrossum/nabla
- **Commit**: `2a06e9f735390a7988d0ef190981ce4abf4dfd28`
- **Method**: v1.002 tag commit (2022-08-27). Both PRs #5117 (v1.000) and #5160 (v1.002) had empty commit hashes from gftools-packager. Later PRs #5245 and #5279 reprocessed the font binary but did not change the upstream source reference.

### 19. Solway
- **Upstream**: mashavp/Solway
- **Commit**: `830b85f39cc1e0ab45341d8caf262d872c8a8220`
- **Method**: Commit hash explicitly recorded in Font Bakery Dashboard PR #2252 (merged 2019-11-18). The PR body states: "commit 830b85f39cc1e0ab45341d8caf262d872c8a8220". Verified this commit exists in the upstream repo.

### 20. Staatliches
- **Upstream**: googlefonts/staatliches
- **Commit**: `34b655c4219697687bb744c2333cd67e3e85f496`
- **Method**: Merge PR #30 "specimen-update" (2018-10-29), which was HEAD of upstream when gfonts PR #1727 was merged 2018-11-15. Font binary was last changed at commit 2329fe0 (2018-10-19).

### 21. TikTok Sans
- **Upstream**: TikTok/TikTokSans
- **Commit**: `44862db3a4bf3a544b664a90245ca5daa5393571`
- **Method**: v4.000 tag (annotated) resolves to this commit "Exclude docs from release" (2025-07-09). Gfonts PR #9650 merged 2025-07-11.

### 22. Vollkorn
- **Upstream**: FAlthausen/Vollkorn-Typeface
- **Commit**: `38ab7a896bd6b163ac7f834ec696d6c68e5dedd6`
- **Method**: Explicitly recorded in gfonts PR #2443 body: "taken from the upstream repo ... at commit 38ab7a89...". PR #2960 (v5.000) and #4124 (version bump hotfix) used the same upstream base.

## Confidence Notes

- **High confidence**: Fira Code (tag match), Vollkorn (explicit in PR), Solway (explicit in PR), TikTok Sans (tag match), Mingzat (tag match), Nabla (tag match), Lobster (date/content match), Libre Caslon Text (date match), Lalezar (only commit), Josefin Sans (date match)
- **Medium confidence**: Amaranth (all commits same day, latest used), Amethysta (few commits, font in earliest), Arsenal (m4rc1e branch commit), Chakra Petch (latest before gfonts commit), Dela Gothic One (latest commit with TTF update), Staatliches (HEAD at PR time)
- **Lower confidence**: Hind family (4 repos) - upstream only has v1.000 but gfonts has v1.001; the v1.001 modifications were likely done on the gfonts side. Jacques Francois and Jacques Francois Shadow - upstream repos created after font was in gfonts, using initial commits as reference.
