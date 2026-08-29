import os
import shutil

text_folder = "organized_dir/TextFiles"
image_folder = "organized_dir/ImageFiles"

os.makedirs(text_folder, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

for file in os.listdir("organized_dir"):
    if file.endswith(".txt"):
        shutil.move("organized_dir/" + file, text_folder)

    elif file.endswith(".png"):
        shutil.move("organized_dir/" + file, image_folder)

print("Files organized successfully.")