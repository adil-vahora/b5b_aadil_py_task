from pathlib import Path

file = Path("notes.txt")

if file.exists():
    print("File size:", file.stat().st_size, "bytes")
    print("File extension:", file.suffix)
else:
    print("notes.txt does not exist.")