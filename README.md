# Bot de Discord para Monitoreo de Streams de Twitch

Este proyecto es un bot de Discord que monitorea una lista de canales de Twitch y realiza acciones automáticas cuando detecta que alguno está transmitiendo en vivo. Además, responde a mensajes en Discord que contengan enlaces de Twitch y puede interactuar automáticamente en el chat del stream.

## Características

- Monitorea canales de Twitch especificados y detecta cuándo están en vivo.
- Abre automáticamente el stream en el navegador y envía un mensaje predefinido en el chat del canal.
- Responde a mensajes de Discord que contengan enlaces de Twitch, abriendo el enlace y enviando el mensaje en el chat.
- Ignora enlaces que no sean de Twitch por seguridad.
- Reproduce un sonido al abrir un stream.

## Requisitos

- Python 3.8 o superior
- [Discord.py](https://github.com/Rapptz/discord.py)
- [Requests](https://pypi.org/project/requests/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [winsound](https://docs.python.org/3/library/winsound.html) (solo Windows)
- Un archivo de sonido llamado `sound.wav` en el mismo directorio que el script.
- Un bot de Discord y sus credenciales.
- Credenciales de aplicación de Twitch (Client ID y Client Secret).

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:

   ```sh
   pip install discord.py requests pyautogui
   ```

3. Coloca tu archivo `sound.wav` en el directorio del proyecto.
4. Configura tus credenciales de Discord y Twitch en el archivo `bot_discord2.py`.

## Uso

Ejecuta el bot con:

```sh
python bot_discord2.py
```

El bot se conectará a Discord y comenzará a monitorear los canales de Twitch especificados. Cuando detecte que un canal está en vivo, abrirá el stream y enviará el mensaje configurado en el chat.

## Utilidad: pruebaCoordenadas.py

Incluye un script llamado `pruebaCoordenadas.py` que te ayuda a obtener fácilmente las coordenadas exactas del campo de chat de Twitch en tu pantalla. Solo ejecuta el script, mueve el mouse al campo de chat y espera unos segundos; el script mostrará las coordenadas que puedes usar en la configuración del bot.

```sh
python pruebaCoordenadas.py
```

Esto facilita la personalización del bot para diferentes resoluciones y navegadores.

## Notas

- Las coordenadas del chat de Twitch (`CHAT_CLICK_COORDS`) pueden necesitar ser ajustadas según tu resolución de pantalla y navegador.
- Este bot está diseñado para sistemas Windows debido al uso de `winsound`.
- No compartas tus tokens ni credenciales en público.

---

¡Contribuciones y sugerencias son bienvenidas!
