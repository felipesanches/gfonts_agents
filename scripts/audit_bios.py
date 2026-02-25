#!/usr/bin/env python3
"""Audit all designer bio.html files against the Editorial Guide."""

import glob
import json
import os
import re
import sys
from html.parser import HTMLParser


GFONTS_DIR = "/mnt/shared/google/fonts"
CATALOG_DIR = os.path.join(GFONTS_DIR, "catalog", "designers")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "bio_audit.json")

# Promotional / superlative patterns
PROMOTIONAL_PATTERNS = [
    (r'\bleading\b', '"leading"'),
    (r'\bworld-renowned\b', '"world-renowned"'),
    (r'\blegendary\b', '"legendary"'),
    (r'\bthe best\b', '"the best"'),
    (r'\bpioneering\b', '"pioneering"'),
    (r'\binnovative\b', '"innovative"'),
    (r'\bcutting[- ]edge\b', '"cutting-edge"'),
    (r'\bgroundbreaking\b', '"groundbreaking"'),
    (r'\bunparalleled\b', '"unparalleled"'),
    (r'\bworld[- ]class\b', '"world-class"'),
    (r'\brenowned\b', '"renowned"'),
    (r'\bprestigious\b', '"prestigious"'),
    (r'\baward[- ]winning\b', '"award-winning"'),
    (r'\bvisionary\b', '"visionary"'),
    (r'\bexceptional\b', '"exceptional"'),
    (r'\bextraordinary\b', '"extraordinary"'),
    (r'\bpassion(?:ate)?\b', '"passion/passionate"'),
    (r'\bunique(?:ly)?\b', '"unique/uniquely"'),
    (r'\bmaster(?:ful|ly)?\b', '"master/masterful"'),
    (r'\bbrilliant\b', '"brilliant"'),
    (r'\btalented\b', '"talented"'),
    (r'\bexpert\b', '"expert"'),
    (r'\bbest[- ]known\b', '"best-known"'),
    (r'\bhighly[- ]regarded\b', '"highly-regarded"'),
    (r'\bdeep expertise\b', '"deep expertise"'),
    (r'\bsharp\b', '"sharp"'),
    (r'\bexclusive\b', '"exclusive"'),
]

# First-person patterns
FIRST_PERSON_PATTERNS = [
    (r'\bI am\b', '"I am"'),
    (r'\bI have\b', '"I have"'),
    (r'\bI was\b', '"I was"'),
    (r'\bI work\b', '"I work"'),
    (r'\bI design\b', '"I design"'),
    (r'\bI founded\b', '"I founded"'),
    (r'\bI studied\b', '"I studied"'),
    (r'\bI graduated\b', '"I graduated"'),
    (r"(?<!['\"])\\bI\\b(?!['\"])", None),  # skip this complex one
    (r'\bOur work\b', '"Our work"'),
    (r'\bOur mission\b', '"Our mission"'),
    (r'\bOur team\b', '"Our team"'),
    (r'\bOur focus\b', '"Our focus"'),
    (r'\bWe are\b', '"We are"'),
    (r'\bWe have\b', '"We have"'),
    (r'\bWe create\b', '"We create"'),
    (r'\bWe design\b', '"We design"'),
    (r'\bWe offer\b', '"We offer"'),
    (r'\bWe specialize\b', '"We specialize"'),
    (r'\bWe believe\b', '"We believe"'),
    (r'\bMy work\b', '"My work"'),
    (r'\bMy design\b', '"My design"'),
    (r'\bMy typeface\b', '"My typeface"'),
]

# Vague filler patterns
FILLER_PATTERNS = [
    (r'\bover \w+ (?:years|decades) of experience\b', 'vague experience claim'),
    (r'\blarge catalogue\b', '"large catalogue"'),
    (r'\bextensive background\b', '"extensive background"'),
    (r'\bwide range\b', '"wide range"'),
    (r'\bbroad interests\b', '"broad interests"'),
    (r'\bvarious (?:projects|clients|companies)\b', '"various projects/clients"'),
    (r'\bnumerous (?:projects|awards|clients)\b', '"numerous..."'),
    (r'\bmany (?:years|projects|clients)\b', '"many..."'),
    (r'\ba number of\b', '"a number of"'),
    (r'\bkeeps thinking about\b', '"keeps thinking about"'),
]

# Arctic Code Vault
ARCTIC_PATTERN = re.compile(r'arctic\s+code\s+vault', re.IGNORECASE)

# Email pattern
EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')


class BioHTMLParser(HTMLParser):
    """Parse bio.html and extract structural information."""

    def __init__(self):
        super().__init__()
        self.tags_used = set()
        self.tag_stack = []
        self.paragraphs = []
        self.current_text = ""
        self.links = []
        self.in_p = False
        self.in_a = False
        self.current_link = {}
        self.html_errors = []
        self.all_text = ""

    def handle_starttag(self, tag, attrs):
        self.tags_used.add(tag)
        attrs_dict = dict(attrs)

        if tag == 'p':
            self.in_p = True
            self.current_text = ""
        elif tag == 'a':
            self.in_a = True
            self.current_link = {
                'href': attrs_dict.get('href', ''),
                'target': attrs_dict.get('target', ''),
                'text': '',
            }

        # Check for self-closing tags
        if tag not in ('br', 'hr', 'img', 'input', 'meta', 'link', 'col', 'area', 'base', 'embed', 'source', 'track', 'wbr'):
            self.tag_stack.append(tag)

    def handle_endtag(self, tag):
        if tag == 'p':
            self.in_p = False
            self.paragraphs.append(self.current_text.strip())
        elif tag == 'a':
            self.in_a = False
            if self.current_link:
                self.links.append(self.current_link)
                self.current_link = {}

        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
        elif tag in self.tag_stack:
            self.html_errors.append(f'Mismatched closing tag: </{tag}>')

    def handle_data(self, data):
        self.all_text += data
        if self.in_p:
            self.current_text += data
        if self.in_a and self.current_link:
            self.current_link['text'] += data


def get_designer_name_from_info(designer_id):
    """Try to read the designer's full name from info.pb."""
    info_path = os.path.join(CATALOG_DIR, designer_id, "info.pb")
    if not os.path.exists(info_path):
        return None
    try:
        with open(info_path) as f:
            content = f.read()
        match = re.search(r'designer:\s*"([^"]+)"', content)
        if match:
            return match.group(1)
    except Exception:
        pass
    return None


def count_words(text):
    """Count words in text, stripping HTML-like content."""
    clean = re.sub(r'<[^>]+>', '', text)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return len(clean.split()) if clean else 0


def check_link_text(link):
    """Check if link text follows conventions (domain for websites, platform name for social)."""
    issues = []
    text = link['text'].strip()
    href = link['href'].strip()

    # Known platform names
    platforms = {
        'instagram': 'Instagram',
        'x.com': 'X',
        'linkedin': 'LinkedIn',
        'behance': 'Behance',
        'github': 'GitHub',
        'facebook': 'Facebook',
        'dribbble': 'Dribbble',
        'youtube': 'YouTube',
        'mastodon': 'Mastodon',
        'threads': 'Threads',
    }

    # Check for generic link text
    generic_texts = ['website', 'homepage', 'webpage', 'site', 'link', 'url', 'click here', 'here']
    if text.lower() in generic_texts:
        issues.append(f'Generic link text "{text}" instead of domain name or platform name')

    href_lower = href.lower()
    
    # Check for outdated Twitter links
    if 'twitter.com' in href_lower:
        issues.append('Twitter links should use x.com')
        if text.lower() == 'twitter':
            issues.append('Link text should be "X" instead of "Twitter"')

    # Check capitalization for known platforms
    for platform_key, platform_name in platforms.items():
        if platform_key in href_lower:
            if text != platform_name and text.lower() == platform_name.lower():
                issues.append(f'Link text "{text}" should be "{platform_name}" (capitalization)')
            break

    return issues


def audit_bio(designer_id, bio_path):
    """Audit a single bio.html file. Returns dict of issues found."""
    with open(bio_path) as f:
        raw_html = f.read()

    issues = []
    info_items = []

    # Parse HTML
    parser = BioHTMLParser()
    try:
        parser.feed(raw_html)
    except Exception as e:
        issues.append(f'HTML parsing error: {e}')
        return {'designer_id': designer_id, 'issues': issues, 'info': info_items, 'severity': 'error'}

    # Get designer's full name from info.pb
    full_name = get_designer_name_from_info(designer_id)

    # --- Checklist checks ---

    # 1. Check for forbidden HTML tags (only <p> and <a> allowed)
    forbidden_tags = parser.tags_used - {'p', 'a'}
    if forbidden_tags:
        issues.append(f'Forbidden HTML tags: {", ".join(sorted(forbidden_tags))}')

    # 2. Check for broken HTML
    if parser.html_errors:
        for err in parser.html_errors:
            issues.append(f'HTML error: {err}')

    # Check for unclosed <p> tags (common error: <p> instead of </p>)
    open_p_count = raw_html.count('<p')
    close_p_count = raw_html.count('</p>')
    if open_p_count != close_p_count:
        issues.append(f'Mismatched <p> tags: {open_p_count} opening vs {close_p_count} closing')

    # Check for malformed href attributes (missing quotes)
    if re.search(r'href=[^"\s>][^\s>]*', raw_html):
        issues.append('Malformed href attribute (missing quotes)')

    # 3. Check links for target="_blank"
    for link in parser.links:
        if link['target'] != '_blank':
            issues.append(f'Link missing target="_blank": {link["href"][:60]}')

    # 4. Check for HTTP instead of HTTPS
    for link in parser.links:
        href = link['href'].strip()
        if href.startswith('http://'):
            issues.append(f'HTTP instead of HTTPS: {href[:60]}')

    # 5. Check link text format
    for link in parser.links:
        link_issues = check_link_text(link)
        issues.extend(link_issues)

    # 6. Check for first-person voice
    text = parser.all_text
    for pattern, label in FIRST_PERSON_PATTERNS:
        if label is None:
            continue
        if re.search(pattern, text):
            issues.append(f'First-person voice: {label}')

    # 7. Check for promotional/superlative language
    for pattern, label in PROMOTIONAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(f'Promotional language: {label}')

    # 8. Check for vague filler
    for pattern, label in FILLER_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(f'Vague filler: {label}')

    # 9. Check for Arctic Code Vault
    if ARCTIC_PATTERN.search(text):
        issues.append('Contains Arctic Code Vault mention')

    # 10. Check for email addresses
    if EMAIL_PATTERN.search(text):
        issues.append('Contains email address')

    # 11. Check word count (body text only, excluding links paragraph)
    body_paragraphs = parser.paragraphs[:-1] if len(parser.paragraphs) > 1 else parser.paragraphs
    body_text = ' '.join(body_paragraphs)
    word_count = count_words(body_text)
    if word_count > 150:
        issues.append(f'Over word limit: {word_count} words (max ~150)')
    info_items.append(f'Word count: {word_count}')

    # 12. Check if links paragraph exists
    has_links = len(parser.links) > 0
    if not has_links:
        info_items.append('No links paragraph')

    # 13. Check for links inside body paragraphs (not final paragraph)
    # Look for <a> tags in raw HTML of body paragraphs
    # Simple heuristic: check if there are links before the last <p> block
    p_blocks = re.split(r'</?p[^>]*>', raw_html)
    p_blocks = [b.strip() for b in p_blocks if b.strip()]
    if len(p_blocks) > 1:
        for block in p_blocks[:-1]:
            if '<a ' in block:
                issues.append('Links embedded in body paragraph (should be in separate final paragraph)')
                break

    # 14. Check link paragraph uses pipe separators
    if has_links and len(parser.links) > 1:
        # Check the last paragraph of raw HTML for pipe separators
        last_p_match = re.findall(r'<p[^>]*>(.*?)</p>', raw_html, re.DOTALL)
        if last_p_match:
            last_p = last_p_match[-1]
            if '<a ' in last_p and '|' not in last_p:
                issues.append('Multiple links not separated by pipe ( | )')

    # Determine severity
    if not issues:
        severity = 'pass'
    elif len(issues) <= 2 and all('target="_blank"' in i or 'link text' in i.lower() for i in issues):
        severity = 'minor'
    elif len(issues) <= 2:
        severity = 'minor'
    else:
        severity = 'major'

    return {
        'designer_id': designer_id,
        'designer_name': full_name or designer_id,
        'issues': issues,
        'info': info_items,
        'severity': severity,
        'issue_count': len(issues),
        'word_count': word_count,
        'has_links': has_links,
        'link_count': len(parser.links),
    }


def main():
    bio_files = sorted(glob.glob(os.path.join(CATALOG_DIR, "*", "bio.html")))
    print(f"Found {len(bio_files)} bio.html files")

    results = []
    for bio_path in bio_files:
        designer_id = os.path.basename(os.path.dirname(bio_path))
        result = audit_bio(designer_id, bio_path)
        results.append(result)

    # Compute summary statistics
    total = len(results)
    passing = sum(1 for r in results if r['severity'] == 'pass')
    minor = sum(1 for r in results if r['severity'] == 'minor')
    major = sum(1 for r in results if r['severity'] == 'major')
    error = sum(1 for r in results if r['severity'] == 'error')

    # Count issue types
    issue_counts = {}
    for r in results:
        for issue in r['issues']:
            # Normalize issue to category
            if 'target="_blank"' in issue:
                cat = 'missing_target_blank'
            elif 'HTTP instead of HTTPS' in issue:
                cat = 'http_not_https'
            elif 'Promotional language' in issue:
                cat = 'promotional_language'
            elif 'First-person voice' in issue:
                cat = 'first_person'
            elif 'Vague filler' in issue:
                cat = 'vague_filler'
            elif 'Forbidden HTML' in issue:
                cat = 'forbidden_html_tags'
            elif 'HTML error' in issue or 'Mismatched <p>' in issue or 'Malformed href' in issue:
                cat = 'html_errors'
            elif 'Arctic Code Vault' in issue:
                cat = 'arctic_code_vault'
            elif 'email address' in issue:
                cat = 'email_address'
            elif 'Over word limit' in issue:
                cat = 'over_word_limit'
            elif 'link text' in issue.lower() or 'Generic link text' in issue:
                cat = 'link_text_format'
            elif 'Links embedded' in issue:
                cat = 'links_in_body'
            elif 'pipe' in issue.lower():
                cat = 'missing_pipe_separator'
            else:
                cat = 'other'
            issue_counts[cat] = issue_counts.get(cat, 0) + 1

    # Count bios with each issue type (not total occurrences)
    bios_with_issue = {}
    for r in results:
        cats_seen = set()
        for issue in r['issues']:
            if 'target="_blank"' in issue:
                cat = 'missing_target_blank'
            elif 'HTTP instead of HTTPS' in issue:
                cat = 'http_not_https'
            elif 'Promotional language' in issue:
                cat = 'promotional_language'
            elif 'First-person voice' in issue:
                cat = 'first_person'
            elif 'Vague filler' in issue:
                cat = 'vague_filler'
            elif 'Forbidden HTML' in issue:
                cat = 'forbidden_html_tags'
            elif 'HTML error' in issue or 'Mismatched <p>' in issue or 'Malformed href' in issue:
                cat = 'html_errors'
            elif 'Arctic Code Vault' in issue:
                cat = 'arctic_code_vault'
            elif 'email address' in issue:
                cat = 'email_address'
            elif 'Over word limit' in issue:
                cat = 'over_word_limit'
            elif 'link text' in issue.lower() or 'Generic link text' in issue:
                cat = 'link_text_format'
            elif 'Links embedded' in issue:
                cat = 'links_in_body'
            elif 'pipe' in issue.lower():
                cat = 'missing_pipe_separator'
            else:
                cat = 'other'
            cats_seen.add(cat)
        for cat in cats_seen:
            bios_with_issue[cat] = bios_with_issue.get(cat, 0) + 1

    summary = {
        'total_bios': total,
        'passing': passing,
        'minor_issues': minor,
        'major_issues': major,
        'parse_errors': error,
        'issue_type_counts': issue_counts,
        'bios_with_issue_type': bios_with_issue,
    }

    output = {
        'summary': summary,
        'results': results,
    }

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nSummary:")
    print(f"  Total bios: {total}")
    print(f"  Passing: {passing} ({100*passing//total}%)")
    print(f"  Minor issues: {minor} ({100*minor//total}%)")
    print(f"  Major issues: {major} ({100*major//total}%)")
    print(f"  Parse errors: {error}")
    print(f"\nIssue types (bios affected):")
    for cat, count in sorted(bios_with_issue.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count} ({100*count//total}%)")
    print(f"\nResults written to {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
