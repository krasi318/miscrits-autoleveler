import pyautogui
from pyautogui import ImageNotFoundException
import time

try:
    rock = pyautogui.locateCenterOnScreen("rock.png", confidence=0.8)
    if rock:
        print("found a rock, left clicking it ")
        pyautogui.moveTo(rock)
        pyautogui.leftClick()

        print("waiting 6 sec for the fight to start ")
        time.sleep(6)

        fire_elemental = pyautogui.locateCenterOnScreen("fire_elemental.png", confidence=0.8)
        if fire_elemental:
            mighty_bash = pyautogui.locateCenterOnScreen("mbash.png", confidence=0.8)
            pyautogui.moveTo(mighty_bash)
            pyautogui.leftClick()




    else: print("hui batinka")
except ImageNotFoundException:
    print("Image not found: grasselemental.png")
