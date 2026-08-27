from pathlib import Path

file_path = Path("data/raw_data.txt")

absolute_path = file_path.resolve()

print("Absolute path:")
print(absolute_path)    