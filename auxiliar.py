import pyautogui
import time

time.sleep(3)

# Irá verificar a posição do mouse e printar no terminal
print(pyautogui.position())

# Irá realizar o scroll da página
pyautogui.scroll(100) # positivo: irá subir a página / negativo: irá descer a página
