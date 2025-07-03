import discord
import re
import webbrowser
import winsound
import pyautogui
import time
import requests
import asyncio

# ==========================
# CONFIGURACIÓN DEL BOT
# ==========================

DISCORD_TOKEN = 'DICORD_TOKEN_CHANGE'
TWITCH_CLIENT_ID = 'CLIENT_ID_CHANGE'
TWITCH_CLIENT_SECRET = 'CLIENT_SECRET_CHANGE'
TWITCH_CHANNELS = ['canal1', 'canal2', 'vegetta777', ]  # Reemplazar con los nombres reales
CHAT_MESSAGE = "Primero" #Mensaje a enviar
CHAT_CLICK_COORDS = ("X", "Y")  # Coordenadas del campo de chat de Twitch
CHECK_INTERVAL = 60  # Intervalo de verificación en segundos (1 minuto)

# ==========================
# AUTENTICACIÓN CON TWITCH
# ==========================

def get_twitch_token():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': TWITCH_CLIENT_ID,
        'client_secret': TWITCH_CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    data = response.json()
    return data.get('access_token')

# ==========================
# VERIFICAR SI UN CANAL ESTÁ EN VIVO
# ==========================

def is_channel_live(channel_name, token):
    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {token}'
    }
    url = f'https://api.twitch.tv/helix/streams?user_login={channel_name}'
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data'][0] if data['data'] else None

# ==========================
# ACCIONES AL DETECTAR STREAM EN VIVO
# ==========================

def open_stream_and_send_message(url):
    print(f'🌐 Abriendo stream: {url}')
    webbrowser.open(url)
    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
    time.sleep(2)
    time.sleep(0.5)  # Espera para asegurarse de que el navegador esté listo
    pyautogui.click(*CHAT_CLICK_COORDS)
    time.sleep(0.5)  # Espera para asegurarse de que el campo de chat esté activo
    pyautogui.typewrite(CHAT_MESSAGE, interval=0.05)
    pyautogui.press("enter")

# ==========================
# BOT DE DISCORD
# ==========================

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)
notified_streams = set()

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')
    asyncio.create_task(monitor_streams())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '@everyone' in message.content:
        urls = re.findall(r'(https?://\S+)', message.content)
        for url in urls:
            if 'twitch.tv' in url:
                print(f'🌐 Abriendo URL segura: {url}')
                open_stream_and_send_message(url)
            else:
                print(f'⚠️ Enlace ignorado por seguridad: {url}')

# ==========================
# MONITOREO DE STREAMS
# ==========================

async def monitor_streams():
    global notified_streams
    token = get_twitch_token()
    await client.wait_until_ready()

    while not client.is_closed():
        for channel in TWITCH_CHANNELS:
            stream_data = is_channel_live(channel, token)
            if stream_data and channel not in notified_streams:
                stream_url = f"https://www.twitch.tv/{channel}"
                print(f'🔴 {channel} está EN VIVO: {stream_data["title"]}')
                open_stream_and_send_message(stream_url)
                notified_streams.add(channel)
            elif not stream_data and channel in notified_streams:
                notified_streams.remove(channel)
        await asyncio.sleep(CHECK_INTERVAL)

# ==========================
# INICIAR BOT
# ==========================

client.run(DISCORD_TOKEN)
