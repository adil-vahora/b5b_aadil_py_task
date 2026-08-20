class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= self.__salary:
            self.__salary = salary
        else:
            print("Salary cannot be decreased")


employee = Employee("Adil", 30000)

print(employee.get_salary())

employee.set_salary(40000)
print(employee.get_salary())

employee.set_salary(25000)
print(employee.get_salary())