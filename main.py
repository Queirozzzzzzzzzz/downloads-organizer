import time
from attributes import FILE_EXTENSIONS, DESTINATION_FOLDERS, DOWNLOADS_FOLDER

# Create destination folders if not exists
for folder_name, folder_path in DESTINATION_FOLDERS.items():
    folder_path.mkdir(parents=True, exist_ok=True)

def organize_files(folder_path):
    for item in folder_path.iterdir():
        if item.is_dir():
            if item.name not in (folder.name for folder in DESTINATION_FOLDERS.values()):
                item.rename(DESTINATION_FOLDERS['Folders'] / item.name)
                break

        if item.is_file():
            moved = False
            for category, extensions in FILE_EXTENSIONS.items():
                if item.suffix in extensions:
                    item.rename(DESTINATION_FOLDERS[category] / item.name)
                    moved = True
                    break
            if not moved:
                item.rename(DESTINATION_FOLDERS['Others'] / item.name)

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