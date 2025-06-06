from typing import ClassVar


class Employee:
    total_employees = 0


    depts: ClassVar[dict[str, int]] = {}

    def __init__(self, department: str) -> None:
        Employee.total_employees += 1
        Employee.depts[department] = Employee.depts.get(department, 0) + 1

# a)
employee1 = Employee("Manhattan")
employee2 = Employee("New-York")
employee3 = Employee("Los-Angeles")
employee4 = Employee("Manhattan")
employee5 = Employee("Los-Angeles")

# b)
print(f"Total number of employees: {Employee.total_employees}")

# c)
for (department, count) in Employee.depts.items():
    print(f"{department}: {count}")