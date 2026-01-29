#!/usr/bin/env python3
"""Fetch all designer profiles from google/fonts catalog."""

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen
from urllib.error import URLError

BASE_URL = "https://raw.githubusercontent.com/google/fonts/main/catalog/designers"

def get_designer_list():
    """Get list of designer IDs from GitHub API."""
    result = subprocess.run(
        ["gh", "api", "repos/google/fonts/git/trees/main:catalog/designers",
         "--jq", '.tree[] | select(.type == "tree") | .path'],
        capture_output=True, text=True
    )
    return [d.strip() for d in result.stdout.strip().split('\n') if d.strip()]

def parse_info_pb(content):
    """Parse info.pb protobuf text format."""
    data = {}

    # Extract designer name
    match = re.search(r'designer:\s*"([^"]*)"', content)
    if match:
        data['name'] = match.group(1)

    # Extract link
    match = re.search(r'link:\s*"([^"]*)"', content)
    if match:
        data['link'] = match.group(1) or None

    # Extract avatar filename
    match = re.search(r'file_name:\s*"([^"]*)"', content)
    if match:
        data['avatar'] = match.group(1)

    return data

def fetch_designer(designer_id):
    """Fetch data for a single designer."""
    try:
        # Fetch info.pb
        info_url = f"{BASE_URL}/{designer_id}/info.pb"
        with urlopen(info_url, timeout=10) as response:
            info_content = response.read().decode('utf-8')

        data = parse_info_pb(info_content)
        data['id'] = designer_id

        # Fetch bio.html
        try:
            bio_url = f"{BASE_URL}/{designer_id}/bio.html"
            with urlopen(bio_url, timeout=10) as response:
                data['bio'] = response.read().decode('utf-8').strip()
        except URLError:
            data['bio'] = None

        # Avatar URL
        if data.get('avatar'):
            data['avatar_url'] = f"{BASE_URL}/{designer_id}/{data['avatar']}"

        return data
    except Exception as e:
        print(f"\nError fetching {designer_id}: {e}", file=sys.stderr)
        return {'id': designer_id, 'error': str(e)}

def main():
    print("Fetching designer list...")
    designers = get_designer_list()
    print(f"Found {len(designers)} designers")

    results = []
    errors = 0

    print("Fetching designer profiles...")
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(fetch_designer, d): d for d in designers}

        for i, future in enumerate(as_completed(futures), 1):
            result = future.result()
            if 'error' in result:
                errors += 1
            else:
                results.append(result)

            # Progress indicator
            if i % 50 == 0 or i == len(designers):
                print(f"  {i}/{len(designers)} processed...")

    # Sort by ID for consistent output
    results.sort(key=lambda x: x['id'])

    # Write output
    output_file = "data/designers.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nDone! Created {output_file}")
    print(f"  - {len(results)} designers")
    print(f"  - {errors} errors")

if __name__ == "__main__":
    main()
