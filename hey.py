import pyautogui
import time
from PIL import Image


grass_type_img = "grasselemental.png"
water_type_img = "waterelemental.png"
fire_type_img = "fireelemental.png"

big_flower_img = "bigflower.png"
bush_img = "bush.png"


fire_spell_img = "campfirespell.png"
bash_spell_img = "bashspell.png"

run_button_img = "runawaybutton.png"

is_ready_to_train = "isreadytotrain.png"
train_button = "trainbutton.png"
trainnow_button = "trainnowbutton.png"
continue_button = "continue_button.png"
close_button = "close_button.png"
close_big_button = "close_big_button.png"


def locate_and_click(image_path, name):
    try:
        time.sleep(4)
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
        if location:
            print(f"Found {name} at: {location}")
            pyautogui.moveTo(location)
            pyautogui.click()
            pyautogui.moveTo(location)
            pyautogui.click()
            return True
        else:
            print(f"{name} not found.")
            return False
    except pyautogui.ImageNotFoundException as e:
        print(f"Error: {name} image not found. Details: {e}")
        return False


# Function to detect enemy type
def detect_enemy_type():
    try:
        if pyautogui.locateCenterOnScreen(grass_type_img, confidence=0.7):
            return "grass"
        elif pyautogui.locateCenterOnScreen(water_type_img, confidence=0.7):
            return "water"
        elif pyautogui.locateCenterOnScreen(fire_type_img, confidence=0.7):
            return "fire"
        else:
            return "unknown"
    except pyautogui.ImageNotFoundException as e:
        print(f"Error during enemy type detection: {e}")
        return "unknown"


# Function to handle the fight
def handle_fight(enemy_type):
    while True:
        if enemy_type == "grass":
            print(f"Enemy type detected: {enemy_type}. Attacking with fire spell.")
            locate_and_click(fire_spell_img, "fire spell")
        elif enemy_type == "fire":
            print(f"Enemy type detected: {enemy_type}. Attacking with bash spell.")
            locate_and_click(bash_spell_img, "bash spell")
        elif enemy_type == "water":
            print("Enemy type detected: Water. Running away.")
            locate_and_click(run_button_img, "run button")
            return  # End fight loop if running away
        else:
            print("Unknown enemy type. Skipping attack.")
            return

        # Wait before checking for "close_big_button.png"
        time.sleep(2)

        # Check if the close button appears
        if locate_and_click(close_big_button, "close button"):
            print("Enemy defeated. Restarting loop.")
            return  # Exit the fight loop and start over


# Main loop
while True:
    try:
        # Look for the purple flower
        found_flower = locate_and_click(big_flower_img, "purple flower")

        # Wait before the next action
        time.sleep(12)

        # Handle the fight if it starts
        print("Checking if fight has started...")
        enemy_type = detect_enemy_type()

        if enemy_type != "unknown":
            handle_fight(enemy_type)
        else:
            print("No fight detected. Continuing to search for the flower.")

        # Add delay to prevent rapid looping
        time.sleep(2)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break