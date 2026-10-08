"""Check the standalone skill package using only Python's standard library."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
required = ['SKILL.md', 'README.md', 'COPYRIGHT.md', 'provenance.md',
            'glossary.md', 'patterns.md', 'cheatsheet.md']
for name in required:
    if not (root / name).is_file():
        errors.append(f'Missing: {name}')
chapters = sorted((root / 'chapters').glob('ch*.md'))
if len(chapters) != 12:
    errors.append(f'Expected 12 chapters, got {len(chapters)}')
skill = (root / 'SKILL.md').read_text(encoding='utf-8')
if not skill.startswith('---\nname: coulling-volume-price-analysis\ndescription: "'):
    errors.append('Invalid skill name or missing quoted description')
for path in root.rglob('*'):
    if '.git' in path.relative_to(root).parts or not path.is_file():
        continue
    if path.suffix.lower() in {'.epub', '.pdf', '.mobi', '.azw', '.azw3', '.docx'} or path.name in {'full_text.txt', 'metadata.json'}:
        errors.append(f'Source material in package: {path.relative_to(root)}')
    if path.suffix != '.md':
        continue
    content = path.read_text(encoding='utf-8')
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', content):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        destination = (path.parent / target.split('#', 1)[0]).resolve()
        if not destination.is_relative_to(root) or not destination.exists():
            errors.append(f'Invalid local link in {path.relative_to(root)}: {target}')
for path in chapters:
    content = path.read_text(encoding='utf-8')
    for heading in ['## 核心思想', '## 框架与操作', '## 关键概念', '## 心智模型', '## 反模式', '## 重构例子', '## 要点与连接']:
        if heading not in content:
            errors.append(f'Missing {heading}: {path.name}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(chapters)} chapters; required files, local links and source exclusions checked.')
