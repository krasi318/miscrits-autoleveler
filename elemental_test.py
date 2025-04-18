import pyautogui
from pyautogui import ImageNotFoundException

try:
    flower = pyautogui.locateCenterOnScreen("fireelemental.png", confidence=0.8)
    if flower:
        pyautogui.moveTo(flower)
    else:
        print("It's not grass elemental")
except ImageNotFoundException:
    print("Image not found: grasselemental.png")
