import os
import time

FOLDER = "assessment"
os.makedirs(FOLDER, exist_ok=True)

print("Watching 'assessment' folder for new student files...\n")
existing_files = set(os.listdir(FOLDER))

while True:
    time.sleep(15) 
    current_files = set(os.listdir(FOLDER))
    new_files = current_files - existing_files
    print(new_files)
    if new_files:
        for file in new_files:
            print(f"New assessment detected: {file}")
    else:
        print("No new files...")
    
    existing_files = current_files