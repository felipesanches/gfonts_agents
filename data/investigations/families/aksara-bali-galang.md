# Investigation: Aksara Bali Galang

## Summary

| Field | Value |
|-------|-------|
| Family Name | Aksara Bali Galang |
| Slug | aksara-bali-galang |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

(No METADATA.pb file exists in the ofl/aksarabaligalang/ directory.)

## Investigation

The `ofl/aksarabaligalang/` directory contains only three files:
- `AksaraBaliGalang-Regular.ttf`
- `DESCRIPTION.en_us.html`
- `OFL.txt`

There is no `METADATA.pb` file at all. The font was added in the "Initial commit" (`90abd17b4f`, 2015-03-07), which was a mass import of many fonts into google/fonts. It was subsequently modified in two batch maintenance commits:
- `06d9851e7` (2015-04-27): "Updating ofl/aksarabaligalang/*ttf with nbspace and fsType fixes"
- `bacec3651` (2015-08-05): "Fix fsType for 54 font files"

None of these commits reference an upstream repository URL or commit hash.

The `DESCRIPTION.en_us.html` credits the font to:
- Donny Harimurti and his sons Bemby Bantara Narendra and Dendy Narendra (Yayasan Bali Galang foundation)
- I Made Suatjana (earlier Bali Simbar font)

The OFL.txt copyright reads: "Copyright (c) 2008-2012, Bemby Bantara Narendra (bembybantara@gmail.com), Copyright (c) 2008-2012, I Madé Suatjana (62-361-427520)"

No upstream repository for this font was found in the fontc_crater cache at `upstream_repos/fontc_crater_cache/`. The font appears to have been contributed directly to Google Fonts without a publicly known upstream source repository.

This is a very old font (pre-2012 copyright) with Graphite-only rendering support, and the description indicates it was likely provided as a pre-built binary rather than compiled from maintained source files.

## Conclusion

No upstream repository URL is known. The font has no METADATA.pb at all. Investigation of the commit history yielded no repository references. This family needs further research — possibly contacting Bemby Bantara Narendra or Donny Harimurti to identify if a source repository exists.
