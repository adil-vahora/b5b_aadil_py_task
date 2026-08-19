students = [("Razzak", 78), ("Adil", 95), ("Afroz", 48)]

top_to_bottom = sorted(students, key=lambda x: x[1], reverse=True)
print(top_to_bottom)