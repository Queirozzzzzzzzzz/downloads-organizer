import time
from attributes import FILE_EXTENSIONS, DESTINATION_FOLDERS, DOWNLOADS_FOLDER

# Create destination folders if not exists
for folder_name, folder_path in DESTINATION_FOLDERS.items():
    folder_path = DOWNLOADS_FOLDER / folder_path
    folder_path.mkdir(parents=True, exist_ok=True)

def organize_files(folder_path):
    for file in folder_path.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in FILE_EXTENSIONS.items():
                if file.suffix in extensions:
                    file.rename(DOWNLOADS_FOLDER / DESTINATION_FOLDERS[category] / file.name)
                    moved = True
                    break
            if not moved:
                file.rename(DOWNLOADS_FOLDER / DESTINATION_FOLDERS['Others'] / file.name)

def scan_folders():
    organize_files(DOWNLOADS_FOLDER)

    for folder_name, folder_path in DESTINATION_FOLDERS.items():
        organize_files(folder_path)

# Check for new downloads
while True:
    try:
        scan_folders()
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(5)