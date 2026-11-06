#!/usr/bin/env python3
"""Genera los ZIP de cada addon, addons.xml y addons.xml.md5.

Uso:  python3 generate_repo.py
Ejecutalo tras cambiar la version en plugin.video.*/addon.xml y sube los
cambios (carpeta del addon, zips/, addons.xml y addons.xml.md5).
"""
import hashlib
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
EXCLUDE_DIRS = {'__pycache__', '.git'}
EXCLUDE_EXT = ('.pyc', '.pyo')


def addon_dirs():
    for name in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, name)
        if os.path.isfile(os.path.join(path, 'addon.xml')):
            yield name, path


def read_addon_xml(path):
    with open(os.path.join(path, 'addon.xml'), encoding='utf-8') as fh:
        text = fh.read()
    text = re.sub(r'^\s*<\?xml[^>]*\?>\s*', '', text)
    version = re.search(r'<addon[^>]*\sversion="([^"]+)"', text).group(1)
    return text.strip(), version


def make_zip(addon_id, path, version):
    out_dir = os.path.join(ROOT, 'zips', addon_id)
    os.makedirs(out_dir, exist_ok=True)
    for old in os.listdir(out_dir):
        if old.endswith('.zip'):
            os.remove(os.path.join(out_dir, old))
    target = os.path.join(out_dir, '%s-%s.zip' % (addon_id, version))
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zf:
        for folder, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for fname in sorted(files):
                if fname.endswith(EXCLUDE_EXT):
                    continue
                full = os.path.join(folder, fname)
                zf.write(full, os.path.relpath(full, ROOT))
    return target


def main():
    parts = []
    for addon_id, path in addon_dirs():
        xml, version = read_addon_xml(path)
        parts.append(xml)
        print('%s %s -> %s' % (addon_id, version,
                               os.path.relpath(make_zip(addon_id, path, version), ROOT)))
    content = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n%s\n</addons>\n' \
        % '\n'.join(parts)
    with open(os.path.join(ROOT, 'addons.xml'), 'w', encoding='utf-8') as fh:
        fh.write(content)
    with open(os.path.join(ROOT, 'addons.xml.md5'), 'w') as fh:
        fh.write(hashlib.md5(content.encode('utf-8')).hexdigest())
    print('addons.xml y addons.xml.md5 generados')


if __name__ == '__main__':
    main()
