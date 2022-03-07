import pyautogui
import time
import os
import pydirectinput
i=True

os.system('nircmd win activate title "League of Legends (TM) Client"')
while i==True:
  pydirectinput.keyDown('f3')
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
  if alive==True and attach==False:
      pyautogui.moveTo(948, 498)
      pydirectinput.keyDown('w')
      time.sleep(5) 
      pydirectinput.keyUp('w')
  else:
    pydirectinput.keyUp('f3')
