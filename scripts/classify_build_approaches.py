#!/usr/bin/env python3
"""Classify upstream font repositories by build approach and source formats.

Scans all repos in the fontc_crater_cache and classifies each by:
- Primary build system (mutually exclusive, priority-based)
- Source formats detected (non-exclusive)

Outputs data/build_approaches.json with summary stats and per-repo entries.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

CACHE_DIR = Path("/mnt/shared/upstream_repos/fontc_crater_cache")
SOURCES_FILE = Path(__file__).parent.parent / "data" / "gfonts_library_sources.json"
OUTPUT_FILE = Path(__file__).parent.parent / "data" / "build_approaches.json"

# Directories to skip when walking for source files
SKIP_DIRS = {".git", "venv", "node_modules", "__pycache__", ".venv", "env", ".tox"}

# Maximum directory depth for source file detection
MAX_DEPTH = 4

# Build category definitions (priority order)
CATEGORIES = [
    ("gftools_builder", "gftools-builder (config.yaml)"),
    ("gftools_builder_makefile", "gftools-builder via Makefile"),
    ("fontmake_direct", "fontmake (direct)"),
    ("custom_build_py", "Custom Python build script"),
    ("custom_build_sh", "Custom Shell build script"),
    ("makefile_other", "Makefile (other)"),
    ("travis_ci_only", "Travis CI only"),
    ("github_actions_only", "GitHub Actions only"),
    ("source_no_build", "Source only (no build system)"),
    ("prebuilt_only", "Pre-built binaries only"),
    ("unknown", "Unknown / empty"),
]

CATEGORY_DESCRIPTIONS = {
    "gftools_builder": (
        "Repositories using gftools-builder with a config.yaml file. This is the "
        "modern, recommended approach for Google Fonts. The config.yaml specifies "
        "source files and build options, and gftools-builder orchestrates the "
        "compilation pipeline (typically using fontmake under the hood)."
    ),
    "gftools_builder_makefile": (
        "Repositories that invoke gftools-builder through a Makefile rather than "
        "using config.yaml directly. This was a transitional pattern before "
        "config.yaml became standard."
    ),
    "fontmake_direct": (
        "Repositories that call fontmake directly (via Makefile, build.sh, or "
        "build.py) without going through gftools-builder. fontmake compiles "
        ".glyphs, .ufo, and .designspace sources into binary font files."
    ),
    "custom_build_py": (
        "Repositories with a custom build.py script that uses tools other than "
        "fontmake or gftools-builder. These may use specialized pipelines or "
        "custom compilation steps."
    ),
    "custom_build_sh": (
        "Repositories with a custom build.sh shell script that uses tools other "
        "than fontmake or gftools-builder. Similar to custom Python builds but "
        "implemented as shell scripts."
    ),
    "makefile_other": (
        "Repositories with a Makefile that doesn't invoke gftools-builder or "
        "fontmake. These may use other font compilation tools or have non-standard "
        "build processes."
    ),
    "travis_ci_only": (
        "Repositories where the only build configuration is a .travis.yml file "
        "with no local build scripts. The build was handled entirely by Travis CI, "
        "which is now deprecated."
    ),
    "github_actions_only": (
        "Repositories where the only build configuration is in GitHub Actions "
        "workflow files, with no local build scripts. The build runs entirely in CI."
    ),
    "source_no_build": (
        "Repositories that contain font source files (.glyphs, .ufo, .designspace, "
        ".sfd) but have no build system configured. These fonts were likely "
        "compiled manually or using a process not captured in the repository."
    ),
    "prebuilt_only": (
        "Repositories that contain compiled font binaries (.ttf, .otf) but no "
        "source files or build system. These may be distribution-only repos or "
        "repos where the source is maintained elsewhere."
    ),
    "unknown": (
        "Repositories that don't match any known pattern. These may be empty, "
        "contain only documentation, or use an unrecognized project structure."
    ),
}

SOURCE_FORMAT_LABELS = {
    "glyphs": ".glyphs (Glyphs app)",
    "glyphspackage": ".glyphspackage (Glyphs 3 package)",
    "ufo": ".ufo (Unified Font Object)",
    "designspace": ".designspace (Variable font designspace)",
    "sfd": ".sfd (FontForge)",
}


def find_source_formats(repo_path):
    """Detect source file formats present in a repository."""
    formats = set()
    repo_path = Path(repo_path)

    try:
        _walk_for_sources(repo_path, formats, depth=0)
    except OSError:
        # Fallback: check if common source directories exist, then try to
        # infer format from config.yaml content or known patterns
        _probe_source_formats(repo_path, formats)

    return sorted(formats)


def _walk_for_sources(path, formats, depth=0):
    """Walk directory tree looking for font source files."""
    if depth > MAX_DEPTH:
        return
    entries = list(path.iterdir())  # May raise OSError

    for entry in entries:
        name = entry.name
        if name in SKIP_DIRS:
            continue

        try:
            if entry.is_dir():
                lower = name.lower()
                if lower.endswith(".glyphspackage"):
                    formats.add("glyphspackage")
                elif lower.endswith(".ufo"):
                    formats.add("ufo")
                else:
                    _walk_for_sources(entry, formats, depth + 1)
            elif entry.is_file():
                lower = name.lower()
                if lower.endswith(".glyphs"):
                    formats.add("glyphs")
                elif lower.endswith(".glyphspackage"):
                    formats.add("glyphspackage")
                elif lower.endswith(".designspace"):
                    formats.add("designspace")
                elif lower.endswith(".sfd"):
                    formats.add("sfd")
        except OSError:
            continue


def _probe_source_formats(repo_path, formats):
    """Probe for source formats when directory walking is unavailable.

    Reads config.yaml to infer source formats from the sources: entries.
    Also checks common source directory existence.
    """
    # Try reading config.yaml content to find source references
    config_paths = [
        repo_path / "config.yaml",
        repo_path / "sources" / "config.yaml",
        repo_path / "source" / "config.yaml",
        repo_path / "sources" / "config_variable.yaml",
    ]

    for config_path in config_paths:
        content = read_file_safe(str(config_path))
        if not content:
            continue
        content_lower = content.lower()
        if ".glyphs" in content_lower and ".glyphspackage" not in content_lower:
            formats.add("glyphs")
        if ".glyphspackage" in content_lower:
            formats.add("glyphspackage")
        if ".ufo" in content_lower:
            formats.add("ufo")
        if ".designspace" in content_lower:
            formats.add("designspace")
        if ".sfd" in content_lower:
            formats.add("sfd")

    # If still no formats found, try probing known common source file paths
    if not formats:
        # Check if common source directories exist
        for src_dir in ["sources", "source", "src"]:
            try:
                if (repo_path / src_dir).is_dir():
                    # Try common source file patterns inside this dir
                    # We can't list the dir, but we can stat specific paths
                    # Unfortunately we can't guess exact filenames
                    break
            except OSError:
                continue


def infer_source_formats_from_config(config_yaml_value):
    """Infer source formats from the config_yaml field in METADATA.pb.

    The config_yaml field often includes the path to config.yaml which
    hints at the project structure, and the config.yaml itself often
    references source file types.
    """
    if not config_yaml_value:
        return set()
    formats = set()
    lower = config_yaml_value.lower()
    if "variable" in lower or "vf" in lower:
        # Variable font configs typically use .glyphs or .designspace
        pass  # Can't determine format from path alone
    return formats


def has_font_binaries(repo_path):
    """Check if repo contains compiled font files (top 3 levels)."""
    repo_path = Path(repo_path)

    def walk_limited(path, depth=0):
        if depth > 3:
            return False
        try:
            entries = list(path.iterdir())
        except (PermissionError, OSError):
            return False

        for entry in entries:
            name = entry.name
            if name in SKIP_DIRS:
                continue
            try:
                if entry.is_file():
                    lower = name.lower()
                    if lower.endswith((".ttf", ".otf")):
                        return True
                elif entry.is_dir():
                    if walk_limited(entry, depth + 1):
                        return True
            except OSError:
                continue
        return False

    return walk_limited(repo_path)


def read_file_safe(path, max_bytes=50000):
    """Read a file safely, returning empty string on error."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read(max_bytes)
    except (OSError, IOError):
        return ""


def is_gftools_config(config_path):
    """Check if a config.yaml is a gftools-builder config.

    When the file can be read, verifies it contains 'sources:' key.
    When reading fails (e.g. open files limit), assumes True if the
    file exists - config.yaml in a font repo is almost always gftools config.
    """
    content = read_file_safe(config_path)
    if content:
        return bool(re.search(r"^\s*sources?\s*:", content, re.MULTILINE))
    # Can't read the file - if it exists, assume it's a gftools config
    try:
        return Path(config_path).is_file()
    except OSError:
        return False


def find_config_yaml(repo_path):
    """Find config.yaml files in the repo.

    Uses two strategies:
    1. Walk the tree (fast when filesystem is healthy)
    2. Probe known common locations (fallback when opendir fails)
    """
    configs = []
    repo_path = Path(repo_path)

    # Try walking first
    try:
        _walk_for_config(repo_path, configs, depth=0)
    except OSError:
        # Fallback: probe known common locations via stat
        COMMON_CONFIG_PATHS = [
            "config.yaml",
            "sources/config.yaml",
            "source/config.yaml",
            "sources/config_variable.yaml",
            "sources/config_static.yaml",
        ]
        for rel_path in COMMON_CONFIG_PATHS:
            candidate = repo_path / rel_path
            try:
                if candidate.is_file():
                    configs.append(candidate)
            except OSError:
                continue

    return configs


def _walk_for_config(path, configs, depth=0):
    """Walk directory tree looking for config.yaml files."""
    if depth > 3:
        return
    entries = list(path.iterdir())  # May raise OSError

    for entry in entries:
        name = entry.name
        if name in SKIP_DIRS:
            continue
        try:
            if entry.is_file() and name.lower() == "config.yaml":
                configs.append(entry)
            elif entry.is_dir():
                _walk_for_config(entry, configs, depth + 1)
        except OSError:
            continue


def classify_repo(repo_path):
    """Classify a single repository by build approach.

    Returns (category_key, config_path_relative, details_dict).
    """
    repo_path = Path(repo_path)
    details = {}

    def safe_is_file(path):
        try:
            return path.is_file()
        except OSError:
            return False

    def safe_is_dir(path):
        try:
            return path.is_dir()
        except OSError:
            return False

    # Detect build files
    has_makefile = safe_is_file(repo_path / "Makefile")
    has_build_sh = safe_is_file(repo_path / "build.sh")
    has_build_py = safe_is_file(repo_path / "build.py")
    has_travis = safe_is_file(repo_path / ".travis.yml")
    has_actions = safe_is_dir(repo_path / ".github" / "workflows")

    # Check for config.yaml (gftools-builder)
    config_files = find_config_yaml(repo_path)
    gftools_configs = [c for c in config_files if is_gftools_config(c)]

    config_path_relative = None
    if gftools_configs:
        # Pick the one closest to root
        gftools_configs.sort(key=lambda c: len(c.parts))
        best = gftools_configs[0]
        config_path_relative = str(best.relative_to(repo_path))

    # Read build file contents for keyword detection
    makefile_content = read_file_safe(repo_path / "Makefile") if has_makefile else ""
    build_sh_content = read_file_safe(repo_path / "build.sh") if has_build_sh else ""
    build_py_content = read_file_safe(repo_path / "build.py") if has_build_py else ""
    can_read_files = bool(makefile_content or build_sh_content or build_py_content
                          or not (has_makefile or has_build_sh or has_build_py))

    # Detect source formats
    source_formats = find_source_formats(repo_path)

    # Check for font binaries
    has_binaries = has_font_binaries(repo_path)

    # Priority 1: gftools-builder via config.yaml
    if gftools_configs:
        return "gftools_builder", config_path_relative, source_formats, details

    # When we can read file contents, do detailed keyword matching
    if can_read_files:
        # Priority 2: gftools-builder via Makefile
        all_build_content = makefile_content + build_sh_content + build_py_content
        if has_makefile and re.search(r"gftools\s+builder", makefile_content, re.IGNORECASE):
            return "gftools_builder_makefile", None, source_formats, details

        # Priority 3: fontmake direct
        fontmake_in_makefile = has_makefile and re.search(r"fontmake", makefile_content, re.IGNORECASE)
        fontmake_in_sh = has_build_sh and re.search(r"fontmake", build_sh_content, re.IGNORECASE)
        fontmake_in_py = has_build_py and re.search(r"fontmake", build_py_content, re.IGNORECASE)

        if fontmake_in_makefile or fontmake_in_sh or fontmake_in_py:
            gftools_in_any = re.search(r"gftools\s+builder", all_build_content, re.IGNORECASE)
            if not gftools_in_any:
                return "fontmake_direct", None, source_formats, details

    # Priority 4: Custom Python build script
    if has_build_py:
        return "custom_build_py", None, source_formats, details

    # Priority 5: Custom Shell build script
    if has_build_sh:
        return "custom_build_sh", None, source_formats, details

    # Priority 6: Makefile (other)
    if has_makefile:
        return "makefile_other", None, source_formats, details

    # Priority 7: Travis CI only
    if has_travis and not has_actions:
        return "travis_ci_only", None, source_formats, details

    # Priority 8: GitHub Actions only
    if has_actions:
        # Verify there are actual workflow files
        workflows_dir = repo_path / ".github" / "workflows"
        try:
            yml_files = [f for f in workflows_dir.iterdir()
                         if f.suffix in (".yml", ".yaml")]
        except (PermissionError, OSError):
            yml_files = []
        if yml_files:
            return "github_actions_only", None, source_formats, details

    # Priority 9: Source only (no build)
    if source_formats:
        return "source_no_build", None, source_formats, details

    # Priority 10: Pre-built only
    if has_binaries:
        return "prebuilt_only", None, source_formats, details

    # Priority 11: Unknown
    return "unknown", None, source_formats, details


def load_family_mapping():
    """Load gfonts_library_sources.json and create URL-to-families mapping."""
    mapping = {}
    if not SOURCES_FILE.exists():
        return mapping

    with open(SOURCES_FILE, "r") as f:
        data = json.load(f)

    for family in data.get("families", []):
        url = family.get("repository_url", "")
        if not url:
            continue
        # Normalize URL
        normalized = url.lower().rstrip("/")
        if normalized.endswith(".git"):
            normalized = normalized[:-4]
        family_name = family.get("family_name", "")
        if family_name:
            mapping.setdefault(normalized, []).append(family_name)

    return mapping


def repo_url_from_path(repo_path):
    """Extract the GitHub URL from a cached repo path."""
    repo_path = Path(repo_path)
    parts = repo_path.relative_to(CACHE_DIR).parts
    if len(parts) >= 2:
        owner = parts[0]
        repo = parts[1]
        return f"https://github.com/{owner}/{repo}"
    return None


def discover_repos_from_sources():
    """Derive repo paths from gfonts_library_sources.json URLs.

    Fallback when the cache directory can't be listed (e.g. open files limit).
    """
    if not SOURCES_FILE.exists():
        return []

    with open(SOURCES_FILE, "r") as f:
        data = json.load(f)

    seen = set()
    repos = []
    for family in data.get("families", []):
        url = family.get("repository_url", "")
        if not url or "github.com" not in url:
            continue
        # Extract owner/repo
        path_part = url.rstrip("/")
        if path_part.endswith(".git"):
            path_part = path_part[:-4]
        path_part = path_part.replace("https://github.com/", "").replace("http://github.com/", "")
        parts = path_part.split("/")
        if len(parts) < 2:
            continue
        owner_repo = f"{parts[0]}/{parts[1]}"
        if owner_repo in seen:
            continue
        seen.add(owner_repo)

        repo_path = CACHE_DIR / parts[0] / parts[1]
        if repo_path.is_dir() and (repo_path / ".git").is_dir():
            repos.append(repo_path)

    return sorted(repos)


def discover_repos_by_scanning():
    """Scan the cache directory to find all repos."""
    repos = []
    for owner_dir in sorted(CACHE_DIR.iterdir()):
        if not owner_dir.is_dir() or owner_dir.name.startswith("."):
            continue
        for repo_dir in sorted(owner_dir.iterdir()):
            if not repo_dir.is_dir():
                continue
            if (repo_dir / ".git").exists():
                repos.append(repo_dir)
    return repos


def main():
    if not CACHE_DIR.exists():
        print(f"Error: Cache directory not found: {CACHE_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning repos in {CACHE_DIR}...")

    # Load family mapping
    family_mapping = load_family_mapping()

    # Find all repos - try directory scanning first, fall back to sources JSON
    try:
        repos = discover_repos_by_scanning()
        print(f"Found {len(repos)} repositories (by directory scan)")
    except OSError as e:
        print(f"Directory scan failed ({e}), falling back to sources JSON...")
        repos = discover_repos_from_sources()
        print(f"Found {len(repos)} repositories (from sources JSON)")

    # Classify each repo
    results = []
    category_counts = {key: 0 for key, _ in CATEGORIES}
    source_format_counts = {"glyphs": 0, "glyphspackage": 0, "ufo": 0,
                            "designspace": 0, "sfd": 0, "none": 0}

    errors = 0
    for i, repo_path in enumerate(repos):
        if (i + 1) % 100 == 0:
            print(f"  Classified {i + 1}/{len(repos)}...")

        try:
            category, config_path, source_formats, details = classify_repo(repo_path)
        except OSError as e:
            errors += 1
            if errors <= 5:
                print(f"  Warning: Error classifying {repo_path}: {e}")
            category = "unknown"
            config_path = None
            source_formats = []
            details = {}

        # Get repo identifier
        rel = repo_path.relative_to(CACHE_DIR)
        repo_id = str(rel)

        # Map to font families
        url = repo_url_from_path(repo_path)
        normalized_url = url.lower().rstrip("/") if url else ""
        if normalized_url.endswith(".git"):
            normalized_url = normalized_url[:-4]
        families = family_mapping.get(normalized_url, [])

        entry = {
            "repo": repo_id,
            "url": url,
            "category": category,
            "source_formats": source_formats,
            "families": families,
        }
        if config_path:
            entry["config_path"] = config_path

        results.append(entry)
        category_counts[category] += 1

        if source_formats:
            for fmt in source_formats:
                source_format_counts[fmt] += 1
        else:
            source_format_counts["none"] += 1

    # Determine if we're in degraded mode
    source_formats_detected = sum(1 for r in results if r["source_formats"])
    degraded = source_formats_detected < len(repos) * 0.05  # Less than 5% have formats

    if errors > 0:
        print(f"\n  Errors during classification: {errors}")
    if degraded:
        print(f"\n  WARNING: Running in degraded mode (filesystem open files limit)")
        print(f"  Source format detection is limited. Re-run when filesystem recovers.")

    # Build output
    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_repos": len(repos),
        "degraded_mode": degraded,
        "errors": errors,
        "notes": ("Source format detection limited due to filesystem open files limit. "
                  "Build category detection uses stat-only probing. Re-run when filesystem "
                  "recovers for full accuracy.") if degraded else None,
        "summary": {
            "by_category": [
                {
                    "key": key,
                    "label": label,
                    "description": CATEGORY_DESCRIPTIONS[key],
                    "count": category_counts[key],
                }
                for key, label in CATEGORIES
            ],
            "by_source_format": [
                {
                    "key": key,
                    "label": SOURCE_FORMAT_LABELS.get(key, key),
                    "count": count,
                }
                for key, count in sorted(source_format_counts.items(),
                                         key=lambda x: -x[1])
            ],
        },
        "repos": results,
    }

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults written to {OUTPUT_FILE}")
    print(f"\nSummary:")
    print(f"  Total repos: {len(repos)}")
    print(f"  By category:")
    for key, label in CATEGORIES:
        count = category_counts[key]
        if count > 0:
            pct = count / len(repos) * 100
            print(f"    {label}: {count} ({pct:.1f}%)")

    print(f"  By source format:")
    for key, count in sorted(source_format_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            label = SOURCE_FORMAT_LABELS.get(key, key)
            print(f"    {label}: {count}")


if __name__ == "__main__":
    main()
