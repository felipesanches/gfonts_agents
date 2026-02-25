#!/bin/bash
# Sync beads issues to data/beads_issues.json for the dashboard
# Also regenerates investigations index

set -e

cd "$(dirname "$0")/.."

# Export beads issues
bd list --json > data/beads_issues.json
echo "Synced beads issues to data/beads_issues.json"

# Regenerate investigations index
python3 -c "
import json, os, re
from datetime import datetime

reports = []
inv_dir = 'data/investigations'
for fname in sorted(os.listdir(inv_dir)):
    if not fname.endswith('.md'):
        continue
    path = os.path.join(inv_dir, fname)
    with open(path) as f:
        content = f.read()
    title_match = re.search(r'^# (.+)', content, re.MULTILINE)
    title = title_match.group(1) if title_match else fname
    date_match = re.search(r'\*\*Date\*\*:\s*(.+)', content)
    date = date_match.group(1).strip() if date_match else ''
    fam_match = re.search(r'\*\*Famil(?:y|ies)\*\*:\s*(.+)', content)
    families = fam_match.group(1).strip() if fam_match else ''
    issue_match = re.search(r'\*\*Issue\*\*:\s*(.+)', content)
    issue = issue_match.group(1).strip() if issue_match else ''
    reports.append({
        'filename': fname,
        'title': title,
        'date': date,
        'families': families,
        'issue': issue,
        'content': content
    })

output = {
    'generated_at': datetime.now().isoformat(),
    'count': len(reports),
    'reports': reports
}
with open('data/investigations/index.json', 'w') as f:
    json.dump(output, f, indent=2)
print(f'Regenerated investigations index ({len(reports)} reports)')
"
