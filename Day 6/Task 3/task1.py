from pathlib import Path

backup_folder = Path("backup")

if backup_folder.exists():
    print("Backup folder already exists.")
else:
    backup_folder.mkdir()
    print("Backup folder created.")