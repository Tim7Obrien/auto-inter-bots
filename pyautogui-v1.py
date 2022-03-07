import pyautogui
import time


pyautogui.keyDown('F3')
check = pyautogui.screenshot()
check_life = check.getpixel((735, 987))
check_attach = check.getpixel((892, 384))
if check_life ==(127, 137, 174):
  alive=True
else: 
    alive=False
if check_attach ==(231, 207, 132):
      attach=True
else: 
    attach=False
pyautogui.keyUp('F3')
print(alive)
print(attach)