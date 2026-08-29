import shutil
import os

if os.path.exists("important.txt"):
    shutil.copy2("important.txt", "important_backup.txt")
    print("Backup created successfully.")
else:
    print("important.txt does not exist.")
