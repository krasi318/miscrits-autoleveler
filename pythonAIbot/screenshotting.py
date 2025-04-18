import os
import time
from threading import Thread
from pynput import keyboard
from PIL import ImageGrab

# Create the screenshots directory if it doesn't exist
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Function to take screenshots
def take_screenshots(interval):
    while not stop_program[0]:
        # Capture the screen
        screenshot = ImageGrab.grab()
        # Save the screenshot with a timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot.save(f"screenshots/screenshot_{timestamp}.png")
        print(f"Screenshot saved: screenshots/screenshot_{timestamp}.png")
        time.sleep(interval)

# Function to listen for the 'q' key to quit
def listen_for_quit():
    def on_press(key):
        try:
            if key.char == 'q':
                stop_program[0] = True
                print("Exiting program...")
                return False
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Ask the user for the interval in seconds
interval = int(input("Enter the screenshot interval in seconds: "))
stop_program = [False]

# Run the screenshot and quit listener in separate threads
screenshot_thread = Thread(target=take_screenshots, args=(interval,))
quit_thread = Thread(target=listen_for_quit)

screenshot_thread.start()
quit_thread.start()

screenshot_thread.join()
quit_thread.join()
