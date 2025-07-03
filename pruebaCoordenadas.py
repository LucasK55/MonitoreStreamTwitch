import pyautogui
import time

print("🖱️ Mové el mouse al campo de chat de Twitch...")
time.sleep(5) # Te da 5 segundos para mover el mouse
x, y = pyautogui.position()
print(f"📍 Coordenadas detectadas: x={x}, y={y}")
