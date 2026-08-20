class Employee:
    def calculate_salary(self):
        return 30000


class Developer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 10000


class Designer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 5000


developer = Developer()
designer = Designer()

print("Developer Salary:", developer.calculate_salary())
print("Designer Salary:", designer.calculate_salary())