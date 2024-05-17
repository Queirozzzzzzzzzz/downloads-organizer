import time
from attributes import FILE_EXTENSIONS, DESTINATION_FOLDERS, DOWNLOADS_FOLDER

# Create destination folders if not exists
for folder_name, folder_path in DESTINATION_FOLDERS.items():
    folder_path.mkdir(parents=True, exist_ok=True)

from pathlib import Path
import time

def organize_files(folder_path):
    for item in folder_path.iterdir():
        destination = None
        if item.is_dir():
            if item.name not in (folder.name for folder in DESTINATION_FOLDERS.values()):
                destination = DESTINATION_FOLDERS['Folders']
        elif item.is_file():

            for category, extensions in FILE_EXTENSIONS.items():
                if item.suffix in extensions:
                    destination = DESTINATION_FOLDERS[category]
                    break
            if destination is None and item.suffix != '.tmp':
                destination = DESTINATION_FOLDERS['Others']

        if destination:
            try:
                item.rename(destination / item.name)
            except FileExistsError:
                print(f"Couldn't move {item.name} because its name already exists at the destination.")

def scan_folders():
    organize_files(DOWNLOADS_FOLDER)

    for folder_name, folder_path in DESTINATION_FOLDERS.items():
        organize_files(folder_path)

scan_folders()