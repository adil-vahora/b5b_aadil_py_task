list1 = []

list1.append("Go to college")
list1.append("Finish DMDW assignment")
list1.append("Read 5 pages")
list1.append("Go to internship")

print("List of tasks:")
for i in list1:
    print(f"{i}")

list1.remove("Go to college")
list1.remove("Read 5 pages")

print("\nAfter doing 2 tasks:")
for i in list1:
    print(f"{i}")