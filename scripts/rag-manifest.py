#!/usr/bin/env python3
"""Generate a deterministic heading-level Markdown inventory; no embeddings."""
import fnmatch, hashlib, json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
patterns = [s.strip() for s in Path('.ragignore').read_text().splitlines() if s.strip() and not s.lstrip().startswith('#')]
def ignored(path, directory=False):
    p = path.as_posix().removeprefix('./')
    excluded = False
    for rule in patterns:
        negate = rule.startswith('!')
        rule = rule.lstrip('!')
        anchored = rule.startswith('/')
        rule = rule.lstrip('/')
        dir_rule = rule.endswith('/')
        rule = rule.rstrip('/')
        parts = p.split('/')
        hit = (any(fnmatch.fnmatchcase(part, rule) for part in parts) if '/' not in rule and not anchored else
               fnmatch.fnmatchcase(p, rule) or p.startswith(rule + '/'))
        if hit and (not dir_rule or directory or len(parts) > 1):
            excluded = not negate
    return excluded

def meta(lines):
    out = {}
    if lines and lines[0].strip() == '---':
        try:
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
            parsed = json.loads(''.join(lines[1:end]))
            if isinstance(parsed, dict):
                return {k: ','.join(map(str, v)) if isinstance(v, list) else str(v) for k, v in parsed.items()}
        except (ValueError, StopIteration):
            pass
        for line in lines[1:]:
            if line.strip() == '---': break
            m = re.match(r'^([a-z_]+):\s*(.*)$', line)
            if m: out[m[1]] = m[2].strip(' "\'')
    return out

rows = []
for base, dirs, files in os.walk('.', followlinks=False):
    dirs[:] = sorted(d for d in dirs if not Path(base, d).is_symlink() and not ignored(Path(base, d), True))
    for name in sorted(files):
        path = Path(base, name)
        if path.suffix.lower() != '.md' or path.is_symlink() or ignored(path): continue
        try: lines = path.read_text(encoding='utf-8').splitlines(keepends=True)
        except (UnicodeError, OSError): continue
        m = meta(lines)
        if m.get('sensitivity', 'internal').lower() == 'secret': continue
        chunks, title, start = [], '(preamble)', 0
        in_fence = False
        for i, line in enumerate(lines):
            if re.match(r'^\s*(```|~~~)', line): in_fence = not in_fence
            match = None if in_fence else re.match(r'^#{1,6}\s+(.+?)\s*#*\s*$', line)
            if match:
                if i > start and ''.join(lines[start:i]).strip(): chunks.append((title, start, i))
                title, start = match.group(1), i
        if start < len(lines) and ''.join(lines[start:]).strip(): chunks.append((title, start, len(lines)))
        for heading, a, b in chunks:
            content = ''.join(lines[a:b]).encode()
            rel = path.as_posix().removeprefix('./')
            rows.append({'id': hashlib.sha256(f'{rel}:{a+1}:{heading}'.encode()).hexdigest()[:16], 'path': rel, 'heading': heading, 'sha8': hashlib.sha256(content).hexdigest()[:8], 'tags': [v.strip() for v in m.get('tags','').strip('[]').split(',') if v.strip()], 'lang': m.get('lang','und'), 'sensitivity': m.get('sensitivity','internal')})
out = Path('docs/_meta/rag-manifest.jsonl'); out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(''.join(json.dumps(x, ensure_ascii=False, sort_keys=True)+'\n' for x in rows), encoding='utf-8')
print(f'manifest: {len(rows)} chunks')
