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

1. Descarga el ZIP desde `zips/plugin.video.markellinks/` (o desde *Releases*).
2. En Kodi: **Ajustes > Sistema > Complementos > Origenes desconocidos** (activar).
3. **Complementos > icono de caja > Instalar desde archivo ZIP** y elige el ZIP.

## Uso

- Raiz: cabecera con canales/enlaces/fuente, **Buscar**, **Rescanear** y categorias.
- Al pulsar una *Opcion* se abre Horus con `plugin://script.module.horus?action=play&id=<hash>`.
- Si hay problemas de reproduccion, activa en los ajustes el *Modo nolokodi*.
- Los mensajes del addon aparecen en `kodi.log` con la etiqueta `[plugin.video.markellinks]`.

## Publicar una version nueva

1. Cambia `version` en `plugin.video.markellinks/addon.xml`.
2. Ejecuta `python3 generate_repo.py` (regenera el ZIP, `addons.xml` y `addons.xml.md5`).
3. Sube los cambios a GitHub.

## Aviso

Los enlaces proceden de fuentes externas y pueden dejar de funcionar.
