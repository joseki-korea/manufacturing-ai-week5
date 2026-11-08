#!/usr/bin/env python3
"""Check wiki metadata, citations, source freshness, reachability and links."""
import re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote
root = Path(__file__).resolve().parent.parent
wiki = root / 'docs/wiki'
try:
    origin = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
    repo = origin.rstrip('/').rsplit('/', 1)[-1].removesuffix('.git')
except (subprocess.CalledProcessError, FileNotFoundError):
    repo = root.name
errors, seen_ids = [], {}
required = 'id title summary domain tags owner status created updated source lang sensitivity related'.split()
citation = re.compile(r'\[source: ([^\]#]+)#L([1-9][0-9]*) @([0-9a-f]{8})\]')
link = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
pages = sorted((wiki/'pages').rglob('*.md'))
index_path = wiki/'index.md'
if not pages: errors.append('no pages')
for name in ('SCHEMA.md','index.md','log.md'):
    if not (wiki/name).is_file(): errors.append(f'missing {name}')
index = index_path.read_text(encoding='utf-8') if index_path.is_file() else ''
for page in pages:
    rel = page.relative_to(wiki).as_posix()
    if any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', part) for part in page.relative_to(wiki/'pages').with_suffix('').parts): errors.append(f'{rel}: invalid path')
    if index.count(f']({rel})') != 1: errors.append(f'{rel}: expected exactly one index entry')

for doc in sorted(wiki.rglob('*.md')):
    rel = doc.relative_to(wiki).as_posix()
    def err(s): errors.append(f'{rel}: {s}')
    text = doc.read_text(encoding='utf-8'); lines = text.splitlines()
    if not lines or lines[0] != '---' or '---' not in lines[1:]: err('missing front matter'); continue
    end = lines.index('---', 1); fm = {}
    for line in lines[1:end]:
        m = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if m: fm[m.group(1)] = m.group(2).strip().strip('"\'')
    for key in required:
        if not fm.get(key): err(f'missing {key}')
    if not fm.get('id', '').startswith(repo + '-wiki-'): err('id must start with repository slug')
    if fm.get('id') in seen_ids: err('duplicate id')
    if fm.get('id'): seen_ids[fm['id']] = rel
    if fm.get('sensitivity','').lower() == 'secret': err('secret page')
    for key in ('created','updated'):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', fm.get(key,'')): err(f'invalid {key}')
    if doc in pages:
        for i, line in enumerate(lines[end+1:], end+2):
            if line.strip() and not line.lstrip().startswith('#') and not citation.search(line): err(f'uncited line {i}')
        for path, lineno, sha in citation.findall(text):
            source = (root / path).resolve()
            if not source.is_relative_to(root) or not source.is_file(): err(f'missing source {path}'); continue
            try:
                old = subprocess.check_output(['git','show',f'{sha}:{path}'], cwd=root, stderr=subprocess.DEVNULL)
                if old != source.read_bytes(): err(f'stale source {path}@{sha}')
                if int(lineno) > len(old.splitlines()): err(f'invalid line {path}:{lineno}')
            except subprocess.CalledProcessError: err(f'bad revision {path}@{sha}')
    for target in link.findall(text):
        if re.match(r'^(https?://|mailto:)', target): continue
        path = unquote(target.split('#',1)[0]); dest = (doc.parent / path).resolve() if path else doc
        if not dest.is_relative_to(root) or not dest.is_file(): err(f'broken link {target}'); continue
        if '#' in target:
            anchor = unquote(target.split('#',1)[1]).lower()
            headings = re.findall(r'^#{1,6}\s+(.+?)\s*#*\s*$', dest.read_text(encoding='utf-8'), re.M)
            slugs = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
            if anchor not in slugs: err(f'broken anchor {target}')
if len(link.findall(index)) != len(pages): errors.append('index count does not match pages')
print('\n'.join(errors) if errors else f'wiki-lint PASS: {len(pages)} pages')
sys.exit(bool(errors))
