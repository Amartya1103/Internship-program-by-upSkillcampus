import os
import shutil
from pathlib import Path
from logger import logger
from file_types import FILE_TYPES

def organize_folder(folder_path):
    """
    Organizes files in the given folder based on file extensions.
    """
    logger.info(f"Started organizing folder: {folder_path}")
    moved_files = 0
    summary = {
        "Documents": 0,
        "Images": 0,
        "Videos": 0,
        "Audio": 0,
        "Archives": 0,
        "Programs": 0,
        "Others": 0
    }

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            continue
        extension = Path(item).suffix.lower()
        category = "Others"

        for folder_name, extensions in FILE_TYPES.items():
            if extension in extensions:
                category = folder_name
                break
        destination_folder = os.path.join(folder_path, category)

        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, item)

        if os.path.exists(destination_file):
            name = Path(item).stem
            ext = Path(item).suffix
            counter = 1
            while True:
                new_name = f"{name}_{counter}{ext}"
                destination_file = os.path.join(destination_folder, new_name)
                if not os.path.exists(destination_file):
                    break
                counter += 1
        shutil.move(item_path, destination_file)
        logger.info(f"Moved '{item}' to '{category}' folder.")
        moved_files += 1
        summary[category] += 1
    logger.info(f"Finished organizing. Total files moved: {moved_files}")
    return moved_files, summary