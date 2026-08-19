students = [
    {"name": "Adil", "marks": 88},
    {"name": "Afroz", "marks": 95},
    {"name": "Rahim", "marks": 91}
]

highest = students[0]

for student in students:
    if student["marks"] > highest["marks"]:
        highest = student

print("Highest marks:", highest["name"])
print("Marks:", highest["marks"])