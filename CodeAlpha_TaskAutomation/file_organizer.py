import os
import shutil

# Folder to organize
folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Folder does not exist!")
    exit()

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Python": [".py"]
}

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        moved = False

        for folder_name, extensions in file_types.items():

            if extension in extensions:

                destination = os.path.join(folder_path, folder_name)

                os.makedirs(destination, exist_ok=True)

                shutil.move(file_path, os.path.join(destination, file))

                moved = True
                break

        if not moved:
            other = os.path.join(folder_path, "Others")
            os.makedirs(other, exist_ok=True)
            shutil.move(file_path, os.path.join(other, file))

print("\n✅ Files organized successfully!")