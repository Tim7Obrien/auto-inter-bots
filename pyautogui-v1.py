import pyautogui
import time
import os
import pydirectinput
import random

value_list_x = [678, 715, 752, 789, 826, 861  ] 
value_list_y = [496, 570, 649, 722]
os.system('nircmd win activate title "League of Legends (TM) Client"')
pydirectinput.moveTo(958,489)
pydirectinput.keyDown('f2')
z = True
while z == True: 
  check = pyautogui.screenshot()
  while (pyautogui.pixelMatchesColor(861, 821, (134, 250, 229), tolerance=10)==False) and (pyautogui.pixelMatchesColor(729,834, (61, 229, 250), tolerance=10)==True):
        pydirectinput.moveTo(958,489)
        pydirectinput.keyDown('f3')
        pydirectinput.keyDown('w')
        time.sleep(2)
        pydirectinput.keyUp('w')
        time.sleep(3)
  while pyautogui.pixelMatchesColor(861, 821, (134, 250, 229), tolerance=10)==True:
            while pyautogui.pixelMatchesColor(914,784, (255, 247, 125), tolerance=10)==True:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('e')
                    pydirectinput.keyUp('ctrl')
                    pydirectinput.keyUp('e')
            while pyautogui.pixelMatchesColor(870,784, (255, 247, 125), tolerance=10)==True:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('w')
                    pydirectinput.keyUp('ctrl')
                    pydirectinput.keyUp('w')
            while pyautogui.pixelMatchesColor(825,784, (255, 247, 125), tolerance=10)==True:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('q')
                    pydirectinput.keyUp('ctrl')
                    pydirectinput.keyUp('q')
            while pyautogui.pixelMatchesColor(958,784, (255, 247, 125), tolerance=10)==True:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.keyDown('r')
                    pydirectinput.keyUp('ctrl')
                    pydirectinput.keyUp('r')
            pydirectinput.keyDown('e')
            time.sleep(1)
            pydirectinput.keyUp('e')
            time.sleep(1)
            while (pyautogui.pixelMatchesColor(729,834, (61, 229, 250), tolerance=10)==False) and (pyautogui.pixelMatchesColor(713,831,(225, 246, 251), tolerance=10)==False):
                  time.sleep(0.25)
                  pydirectinput.keyDown('p')
                  time.sleep(0.25)
                  pydirectinput.keyUp('p')
                  time.sleep(0.25)
                  pydirectinput.moveTo(820,292)
                  time.sleep(0.25)
                  pydirectinput.click()
                  time.sleep(0.25)
                  pydirectinput.moveTo(random.choice(value_list_x), random.choice(value_list_y))
                  time.sleep(0.25)
                  pydirectinput.click(clicks=2, interval=0.15)
                  pydirectinput.keyDown('p')
                  time.sleep(0.25)
                  pydirectinput.keyUp('p')
