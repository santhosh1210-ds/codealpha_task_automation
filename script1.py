# Task Automation with Python Scripts
# CodeAlpha Python Programming Internship - Task 3
# Automation: Move all .jpg files from one folder to another

import os
import shutil

# Source and destination folders
source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created folder: {destination_folder}")

# Track how many files moved
moved_count = 0

# Loop through files in source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
        moved_count += 1

print(f"\nTask complete! {moved_count} .jpg file(s) moved to '{destination_folder}'.")