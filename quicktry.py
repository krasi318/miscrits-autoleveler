import pyautogui
import time
from PIL import Image

# Define the images for different elements and buttons
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

# Function to locate and click on an image
def locate_and_click(image_path, name, confidence=0.7):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            print(f"Found {name}")
            pyautogui.moveTo(location)
            pyautogui.click()
            pyautogui.moveTo(location)
            pyautogui.click()
            print(f"Clicked on {name}.")
            return True
        else:
            print(f"{name} not found.")
            return False
    except pyautogui.ImageNotFoundException:
        print(f"Error: {name} image not found.")
        return False

# Function to detect enemy type
def detect_enemy_type():
    try:
        if pyautogui.locateCenterOnScreen(grass_type_img, confidence=0.8):
            return "grass"
        elif pyautogui.locateCenterOnScreen(water_type_img, confidence=0.8):
            return "water"
        elif pyautogui.locateCenterOnScreen(fire_type_img, confidence=0.8):
            return "fire"
        else:
            raise ValueError("Unknown enemy type")
    except Exception as e:
        print(f"Error detecting enemy type: {e}")
        return "unknown"

# Function to attack with the fire spell
def attack_with_fire_spell():
    try:
        fire_spell = pyautogui.locateCenterOnScreen(fire_spell_img, confidence=0.8)
        if fire_spell:
            pyautogui.moveTo(fire_spell)
            pyautogui.click()
            print("Fire spell used!")
        else:
            print("Fire spell not found.")
    except pyautogui.ImageNotFoundException:
        print("Error: Fire spell not found.")

# Function to attack with the bash spell
def attack_with_bash_spell():
    try:
        bash_spell = pyautogui.locateCenterOnScreen(bash_spell_img, confidence=0.8)
        if bash_spell:
            pyautogui.moveTo(bash_spell)
            pyautogui.click()
            print("Bash spell used!")
        else:
            print("Bash spell not found.")
    except pyautogui.ImageNotFoundException:
        print("Error: Bash spell not found.")

# Function to check for and click the close button
def check_and_close():
    try:
        close_button = pyautogui.locateCenterOnScreen(close_big_button, confidence=0.8)
        if close_button:
            time.sleep(1)
            pyautogui.moveTo(close_button)
            pyautogui.click()
            time.sleep(3)
            print("Clicked on Close button.")
            return True
        else:
            print("Close button not found.")
            return False
    except pyautogui.ImageNotFoundException:
        print("Error: Close button not found.")
        return False

# Function to click the run away button if the enemy type is unknown
def click_run_button():
    try:
        run_button = pyautogui.locateCenterOnScreen(run_button_img, confidence=0.8)
        if run_button:
            pyautogui.moveTo(run_button)
            pyautogui.click()
            print("Clicked on Run Away button.")
        else:
            print("Run Away button not found.")
    except pyautogui.ImageNotFoundException:
        print("Error: Run Away button not found.")

# Main loop to search for the flower and handle fights
while True:
    # Search for the purple flower
    print("Searching for the purple flower...")
    flower_found = locate_and_click(big_flower_img, "purple flower")

    if not flower_found:
        print("Flower not found. Waiting for 20 seconds.")
        time.sleep(20)
        continue  # Skip to the next loop iteration to search again

    # Start the fight and attack
    print("Fight started!")
    time.sleep(7)

    # Detect enemy type (grass, fire, water) with exception handling
    enemy_type = detect_enemy_type()
    while True:
        if enemy_type == "grass":
            print("Enemy type: Grass. Attacking with Fire Spell.")
            time.sleep(2)
            attack_with_fire_spell()
        elif enemy_type == "fire":
            print("Enemy type: Fire. Attacking with Bash Spell.")
            time.sleep(2)
            attack_with_bash_spell()
        elif enemy_type == "water":
            print("Enemy type: Water. Running away.")
            time.sleep(2)
            click_run_button()
        else:
            print("Enemy type unknown. Running away.")
            click_run_button()

        # Continuously check for the close button after attack
        print("Checking for the Close button...")
        time.sleep(2)

        if check_and_close():
            print("Close button clicked. Returning to search for the flower.")
            break  # Exit the attack loop and return to searching for the flower
        else:
            print("Close button not found. Continuing the attack cycle.")