# Markel Links para Kodi

Addon de Kodi 21 (Omega) que recopila los enlaces AceStream de
[markellinks.app](https://www.markellinks.app/) y los reproduce con el addon
**Horus** (`script.module.horus`).

## Requisitos

- Kodi 21.x
- Addon [Horus](https://www.pluginsxbmc.com/2021/05/horus-reproductor-acestream.html) instalado
- Motor AceStream en marcha (en Horus, desactiva "Detener AceStream al salir")
- Se recomienda VPN: LaLiga y varias operadoras bloquean AceStream

## Instalacion

1. En Kodi: **Ajustes > Sistema > Complementos > Origenes desconocidos** (activar).
2. **Ajustes > Gestor de archivos > Anadir fuente** y escribe la URL de GitHub Pages:
   `https://mimse1.github.io/<repo>/` (nombre: `markellinks`).
3. **Complementos > icono de caja > Instalar desde archivo ZIP > markellinks >
   plugin.video.markellinks > plugin.video.markellinks-X.Y.Z.zip**.

Tambien puedes descargar el ZIP desde la carpeta `plugin.video.markellinks/` y
instalarlo desde el almacenamiento.

## Uso

- Raiz: cabecera con canales/enlaces/fuente, **Buscar**, **Rescanear** y categorias.
- Al pulsar una *Opcion* se abre Horus con `plugin://script.module.horus?action=play&id=<hash>`.
- Si hay problemas de reproduccion, activa en los ajustes el *Modo nolokodi*.
- Los mensajes del addon aparecen en `kodi.log` con la etiqueta `[plugin.video.markellinks]`.

## Publicar una version nueva

1. Cambia `version` en `plugin.video.markellinks/addon.xml`.
2. Ejecuta `python3 generate_repo.py` (regenera el ZIP, los `index.html`, `addons.xml` y `addons.xml.md5`).
3. Sube los cambios a GitHub.

## Aviso

Los enlaces proceden de fuentes externas y pueden dejar de funcionar.

## GitHub Pages

En **Settings > Pages**: *Deploy from a branch*, rama `main`, carpeta `/ (root)`.
El archivo `.nojekyll` evita que GitHub procese los archivos. La estructura publicada es:

```
https://mimse1.github.io/<repo>/                                   (listado)
https://mimse1.github.io/<repo>/plugin.video.markellinks/          (listado con el ZIP)
https://mimse1.github.io/<repo>/addons.xml
```
