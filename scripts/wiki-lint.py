#!/usr/bin/env python3
"""Check wiki metadata, source freshness, page reachability, and local links."""
import re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote
root = Path(__file__).resolve().parent.parent
wiki = root / 'docs/wiki'
errors = []
required = 'id title summary domain tags owner status created updated source lang sensitivity related'.split()
citation = re.compile(r'\[source: ([^\]#]+)#L([1-9][0-9]*) @([0-9a-f]{8})\]')
link = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
pages = sorted((wiki/'pages').rglob('*.md'))
index = (wiki/'index.md').read_text(encoding='utf-8')
for page in pages:
    rel = page.relative_to(wiki).as_posix(); text = page.read_text(encoding='utf-8'); lines = text.splitlines()
    def err(s): errors.append(f'{rel}: {s}')
    if not re.fullmatch(r'[a-z0-9-]+\.md', page.name): err('invalid filename')
    if f']({rel})' not in index: err('orphan page')
    if not lines or lines[0] != '---' or '---' not in lines[1:]: err('missing front matter'); continue
    end = lines.index('---', 1); fm = {}
    for line in lines[1:end]:
        m = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if m: fm[m.group(1)] = m.group(2).strip()
    for key in required:
        if not fm.get(key): err(f'missing {key}')
    if fm.get('sensitivity','').strip('"\'') == 'secret': err('secret page')
    for i, line in enumerate(lines[end+1:], end+2):
        if line.strip() and not line.lstrip().startswith('#') and not citation.search(line): err(f'uncited line {i}')
    for path, line, sha in citation.findall(text):
        source = (root / path).resolve()
        if not source.is_relative_to(root) or not source.is_file(): err(f'missing source {path}'); continue
        try:
            old = subprocess.check_output(['git','show',f'{sha}:{path}'], cwd=root, stderr=subprocess.DEVNULL)
            current = source.read_bytes()
            if old != current: err(f'stale source {path}@{sha}')
            if int(line) > len(old.splitlines()): err(f'invalid line {path}:{line}')
        except subprocess.CalledProcessError: err(f'bad revision {path}@{sha}')
    for target in link.findall(text):
        if re.match(r'^(https?://|mailto:)', target): continue
        path = unquote(target.split('#',1)[0]); dest = (page.parent / path).resolve() if path else page
        if not dest.is_relative_to(root) or not dest.is_file(): err(f'broken link {target}')
        elif '#' in target:
            anchor = unquote(target.split('#',1)[1]).lower()
            headings = re.findall(r'^#{1,6}\s+(.+?)\s*#*\s*$', dest.read_text(encoding='utf-8'), re.M)
            slugs = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
            if anchor not in slugs: err(f'broken anchor {target}')
for target in link.findall(index):
    if not (wiki / unquote(target.split('#',1)[0])).is_file(): errors.append(f'index: broken link {target}')
if not pages: errors.append('no pages')
print('\n'.join(errors) if errors else f'wiki-lint PASS: {len(pages)} pages')
sys.exit(bool(errors))
