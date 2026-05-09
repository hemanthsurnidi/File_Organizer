import os
import shutil
from pathlib import Path

# Folder to organize
DOWNLOADS_FOLDER = "sample_downloads"

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Code": [".py", ".js", ".java"],
    "Archives": [".zip", ".rar"]
}

folder = Path(DOWNLOADS_FOLDER)

if not folder.exists():
    print("Folder does not exist.")
    exit()

for file in folder.iterdir():
    if file.is_file():
        moved = False

        for category, extensions in FILE_TYPES.items():
            if file.suffix.lower() in extensions:
                target_folder = folder / category
                target_folder.mkdir(exist_ok=True)

                new_path = target_folder / file.name
                shutil.move(str(file), str(new_path))

                print(f"Moved {file.name} -> {category}")
                moved = True
                break

        if not moved:
            others = folder / "Others"
            others.mkdir(exist_ok=True)

            new_path = others / file.name
            shutil.move(str(file), str(new_path))

            print(f"Moved {file.name} -> Others")

print("Organization completed!")
