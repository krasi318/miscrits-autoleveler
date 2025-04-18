import os
import roboflow
from roboflow import Roboflow

# Step 1: Create the datasets directory
home_dir = os.path.expanduser("~")  # Get the home directory for your system
datasets_dir = os.path.join(home_dir, "datasets")
os.makedirs(datasets_dir, exist_ok=True)  # Create the datasets directory if it doesn't exist
print(f"Datasets directory created at: {datasets_dir}")

# Step 2: Set the working directory (optional for downloading datasets)
os.chdir(datasets_dir)
print(f"Current working directory: {os.getcwd()}")

# Step 3: Install and use the Roboflow library
# Ensure you have installed the library via pip: pip install roboflow
roboflow.login()  # Use your stored login credentials or force re-login if needed

# Step 4: Initialize Roboflow and download the dataset
rf = Roboflow(api_key="ztH5uYKmna0bTidshLlT")
project = rf.workspace("kraschar").project("miscrits-level-bot")
version = project.version(1)
dataset = version.download("yolov11", location=datasets_dir)  # Specify the dataset download location
print("Dataset downloaded successfully!")
