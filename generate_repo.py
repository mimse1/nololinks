#!/usr/bin/env python3
"""Genera los ZIP de cada addon, addons.xml, addons.xml.md5 y los index.html.

Uso:  python3 generate_repo.py
Ejecutalo tras cambiar la version en plugin.video.*/addon.xml y sube los
cambios (carpeta del addon con su ZIP e index.html, addons.xml, addons.xml.md5, index.html raiz y .nojekyll).
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
    """El ZIP queda dentro de la carpeta del addon (<id>/<id>-<version>.zip),
    que es el formato que Kodi espera tanto en una fuente de archivos como en
    el datadir de un repositorio."""
    for old in os.listdir(path):
        if old.endswith('.zip'):
            os.remove(os.path.join(path, old))
    target = os.path.join(path, '%s-%s.zip' % (addon_id, version))
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zf:
        for folder, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for fname in sorted(files):
                if fname.endswith(EXCLUDE_EXT) or fname.endswith('.zip') \
                        or fname == 'index.html':
                    continue
                full = os.path.join(folder, fname)
                zf.write(full, os.path.relpath(full, ROOT))
    return target


def write_index(folder, title, links):
    """Listado HTML sencillo (estilo Apache) que Kodi sabe recorrer."""
    rows = '\n'.join('<a href="%s">%s</a><br>' % (href, text) for href, text in links)
    html = ('<!DOCTYPE html>\n<html><head><meta charset="utf-8">'
            '<title>Index of %s</title></head>\n<body>\n<h1>Index of %s</h1>\n'
            '<pre>\n%s\n</pre>\n</body></html>\n') % (title, title, rows)
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as fh:
        fh.write(html)


def main():
    parts = []
    root_links = []
    for addon_id, path in addon_dirs():
        xml, version = read_addon_xml(path)
        parts.append(xml)
        zip_path = make_zip(addon_id, path, version)
        print('%s %s -> %s' % (addon_id, version, os.path.relpath(zip_path, ROOT)))
        zip_name = os.path.basename(zip_path)
        write_index(path, '/%s/' % addon_id, [(zip_name, zip_name)])
        root_links.append(('%s/' % addon_id, '%s/' % addon_id))
    root_links += [('addons.xml', 'addons.xml'), ('addons.xml.md5', 'addons.xml.md5')]
    content = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n%s\n</addons>\n' \
        % '\n'.join(parts)
    with open(os.path.join(ROOT, 'addons.xml'), 'w', encoding='utf-8') as fh:
        fh.write(content)
    with open(os.path.join(ROOT, 'addons.xml.md5'), 'w') as fh:
        fh.write(hashlib.md5(content.encode('utf-8')).hexdigest())
    write_index(ROOT, '/', root_links)
    open(os.path.join(ROOT, '.nojekyll'), 'a').close()
    print('addons.xml, addons.xml.md5 e index.html generados')


if __name__ == '__main__':
    main()
