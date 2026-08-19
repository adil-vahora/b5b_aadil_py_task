employees = {
    "Riya": 50000,
    "Aman": 75000,
    "Neha": 60000,
    "Raj": 90000,
    "Kiran": 85000
}

sorted_employees = sorted(
    employees.items(),
    key=lambda x: x[1],
    reverse=True
)

for name, salary in sorted_employees[:3]:
    print(name, salary)