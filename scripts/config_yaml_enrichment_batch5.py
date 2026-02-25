#!/usr/bin/env python3
"""
Batch config_yaml enrichment for METADATA.pb and override config.yaml files.

Part 1: Add config_yaml field to METADATA.pb source blocks
Part 2: Create override config.yaml files in google/fonts family directories
"""

import os
import re
import json

GFONTS_BASE = "/mnt/shared/google/fonts/ofl"
CACHE_BASE = "/mnt/shared/upstream_repos/fontc_crater_cache"

# ============================================================
# Part 1: Add config_yaml to METADATA.pb
# ============================================================
# These families have verified gftools-builder config.yaml in upstream
PART1_FAMILIES = {
    "alansans": "sources/config.yaml",
    "bbhbartle": "sources/config.yaml",
    "bbhbogle": "sources/config.yaml",
    "bbhhegarty": "sources/config.yaml",
    "cause": "sources/config.yaml",
    "flowcircular": "Circular/sources/config.yaml",
    "flowrounded": "Rounded/sources/config.yaml",
    "lilex": "sources/Lilex/config.yaml",
    "lineseedjp": "LINESeedJP/sources/config.yaml",
    "natasans": "config.yaml",
    "playwritenzbasic": "sources/config.yaml",
    "playwritenzbasicguides": "sources/config.yaml",
    "sciencegothic": "sources/build-config.yaml",
    "zcoolkuaile": "sources/config.yaml",
}


def add_config_yaml_to_metadata(fam_dir, config_yaml_path):
    """Add config_yaml field to METADATA.pb source block."""
    meta_path = os.path.join(GFONTS_BASE, fam_dir, "METADATA.pb")

    with open(meta_path) as f:
        content = f.read()

    # Verify it doesn't already have config_yaml
    if "config_yaml:" in content:
        print(f"  SKIP {fam_dir}: already has config_yaml")
        return False

    # Find the source { } block and add config_yaml before the closing }
    # Strategy: find the last } that closes the source { block
    # We need to find "source {" and then its matching "}"

    source_match = re.search(r'^source\s*\{', content, re.MULTILINE)
    if not source_match:
        print(f"  ERROR {fam_dir}: no source block found")
        return False

    # Find the closing } for the source block
    # We need to handle nested { } blocks (like files { })
    start = source_match.end()
    depth = 1
    pos = start
    while pos < len(content) and depth > 0:
        if content[pos] == '{':
            depth += 1
        elif content[pos] == '}':
            depth -= 1
        pos += 1

    if depth != 0:
        print(f"  ERROR {fam_dir}: unmatched braces in source block")
        return False

    # pos now points to right after the closing }
    closing_brace_pos = pos - 1

    # Insert config_yaml line before the closing }
    # Find the indentation (should be 2 spaces based on existing format)
    config_yaml_line = f'  config_yaml: "{config_yaml_path}"\n'

    new_content = content[:closing_brace_pos] + config_yaml_line + content[closing_brace_pos:]

    with open(meta_path, 'w') as f:
        f.write(new_content)

    print(f"  OK {fam_dir}: added config_yaml: \"{config_yaml_path}\"")
    return True


# ============================================================
# Part 2: Create override config.yaml files
# ============================================================
# Selected families with clear, simple source structure
# Each entry: (dir_name, [source_files])
PART2_FAMILIES = {
    # Single .glyphs source - clearest cases
    "amethysta": ["sources/Amethysta-Regular.glyphs"],
    "aoboshione": ["sources/aoboshi.glyphs"],
    "baijamjuree": ["source/Baijam.glyphs"],
    "bebasneue": ["sources/BebasNeueV2.0(2018).glyphs"],
    "chakrapetch": ["source/Chakra Petch.glyphs"],
    "charmonman": ["source/Charmonman.glyphs"],
    "delagothicone": ["Sources/DelaGothic.glyphs"],
    "dotgothic16": ["sources/DotGothic16.glyphs"],
    "enriqueta": ["source/enriqueta_masters_GOOGLE.glyphs"],
    "federant": ["src/Federant-Regular.glyphs"],
    "firacode": ["FiraCode.glyphs"],
    "hachimarupop": ["sources/HachiMaruPop.glyphs"],
    "heptaslab": ["sources/HeptaSlab.glyphs"],
    "jacquesfrancois": ["sources/JacquesFrancois.glyphs"],
    "jacquesfrancoisshadow": ["sources/JacquesFrancoisShadow.glyphs"],
    "lalezar": ["sources/Lalezar.glyphs"],
    "liujianmaocao": ["sources/LiuJianMaoCao.glyphs"],
    "lobster": ["sources/Lobster.glyphs"],
    "mali": ["source/Mali-Master.glyphs"],
    "moul": ["Source/Moul.glyphs"],
    "nabla": ["sources/Nabla.glyphs"],
    "palettemosaic": ["sources/PaletteMosaic.glyphs"],
    "quicksand": ["sources/Quicksand.glyphs"],
    "rowdies": ["sources/Rowdies.glyphs"],
    "sansitaswashed": ["sources/SansitaSwashed.glyphs"],
    "sarabun": ["source/Sarabun.glyphs"],
    "shizuru": ["sources/ShizuruFont.glyphs"],
    "slacksideone": ["source/SlacksideOne.glyphs"],
    "solway": ["sources/Solway.glyphs"],
    "srisakdi": ["source/Srisakdi.glyphs"],
    "staatliches": ["sources/Staatliches-Regular.glyphs"],
    "stick": ["sources/Stick.glyphs"],
    "thasadith": ["source/Thasadith_Master.glyphs"],
    "trainone": ["sources/TrainOne.glyphs"],
    "tsukimirounded": ["sources/tsukimi_rounded.glyphs"],
    "turretroad": ["sources/turret-road.glyphs"],
    "vibes": ["vibes-typeface.glyphs"],
    "yomogi": ["sources/Yomogi.glyphs"],
    "yuseimagic": ["sources/YuseiMagic.glyphs"],
    "zenkurenaido": ["sources/Kurenaido.glyphs"],
    "zcoolqingkehuangyou": ["sources/zcool-qingke-huangyou.glyphs"],
    "zcoolxiaowei": ["sources/xiaowei.glyphs"],
    "viaodalibre": ["sources/Viaoda Libre.glyphs"],

    # Single .designspace source
    "alkalami": ["source/Alkalami.designspace"],
    "assistant": ["sources/Assistant.designspace"],
    "mingzat": ["source/Mingzat.designspace"],
    "ruwudu": ["source/Ruwudu.designspace"],

    # Two-source families (Roman + Italic pairs)
    "amaranth": ["sources/Amaranth-Roman.glyphs", "sources/Amaranth-Italic.glyphs"],
    "arsenal": ["sources/Arsenal.glyphs", "sources/Arsenal-Italic.glyphs"],
    "courierprime": ["sources/Courier Prime.glyphs", "sources/Courier Prime Italic.glyphs"],
    "dmmono": ["source/DMMono-MASTER.glyphs", "source/DMMono-Italics-MASTER.glyphs"],
    "librecaslontext": ["sources/LibreCaslonText.glyphs", "sources/LibreCaslonText-Italic.glyphs"],
    "xanhmono": ["source/XanhMono.glyphs", "source/XanhMono-Italic.glyphs"],

    # Two-source .designspace families
    "castoro": ["source/Castoro-Roman.designspace", "source/Castoro-Italic.designspace"],
    "intelonemono": ["sources/masters/IntelOneMono-Roman.designspace", "sources/masters/IntelOneMono-Italic.designspace"],
    "josefinsans": ["sources/JosefinSans.designspace", "sources/JosefinSans-Italic.designspace"],
    "merriweathersans": ["sources/MerriweatherSans.designspace", "sources/MerriweatherSans-Italic.designspace"],
    "vollkorn": ["sources/Vollkorn.designspace", "sources/Vollkorn-Italic.designspace"],

    # Hind family variants (each in own repo with single .glyphs)
    "hindcolombo": ["masters/HindColombo.glyphs"],
    "hindguntur": ["masters/HindGuntur.glyphs"],
    "hindjalandhar": ["masters/HindJalandhar.glyphs"],
    "hindkochi": ["masters/HindKochi.glyphs"],
    "hindmadurai": ["masters/HindMadurai.glyphs"],
    "hindmysuru": ["masters/HindMysuru.glyphs"],
    "hindsiliguri": ["masters/HindiSiliguri.glyphs"],
    "hindvadodara": ["masters/HindVadodara.glyphs"],

    # Shippori Antique variants (same repo, same source)
    "shipporiantique": ["sources/ShipporiAntique.glyphs"],
    "shipporiantiqueb1": ["sources/ShipporiAntique.glyphs"],
}


def create_override_config(fam_dir, source_files):
    """Create an override config.yaml in the family directory."""
    config_path = os.path.join(GFONTS_BASE, fam_dir, "config.yaml")

    if os.path.exists(config_path):
        print(f"  SKIP {fam_dir}: override config.yaml already exists")
        return False

    # Verify the family directory exists
    if not os.path.isdir(os.path.join(GFONTS_BASE, fam_dir)):
        print(f"  ERROR {fam_dir}: family directory not found")
        return False

    # Build config content
    lines = ["sources:"]
    for src in source_files:
        lines.append(f"  - {src}")

    content = "\n".join(lines) + "\n"

    with open(config_path, 'w') as f:
        f.write(content)

    print(f"  OK {fam_dir}: created override config.yaml with {len(source_files)} source(s)")
    return True


def main():
    print("=" * 60)
    print("Part 1: Add config_yaml to METADATA.pb")
    print("=" * 60)

    part1_count = 0
    for fam_dir, config_path in sorted(PART1_FAMILIES.items()):
        if add_config_yaml_to_metadata(fam_dir, config_path):
            part1_count += 1

    print(f"\nPart 1 complete: {part1_count} METADATA.pb files modified")

    print("\n" + "=" * 60)
    print("Part 2: Create override config.yaml files")
    print("=" * 60)

    part2_count = 0
    for fam_dir, sources in sorted(PART2_FAMILIES.items()):
        if create_override_config(fam_dir, sources):
            part2_count += 1

    print(f"\nPart 2 complete: {part2_count} override config.yaml files created")
    print(f"\nTotal changes: {part1_count + part2_count}")


if __name__ == "__main__":
    main()
