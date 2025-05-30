class Employee:
    def get_role(self):
        print("Role: Employee")

class Manager(Employee):
    def get_role(self):
        print("Role: Manager")

class Developer(Employee):
    def get_role(self):
        print("Role: Developer")

employee = Employee()
manager = Manager()
developer = Developer()
employee.get_role()
manager.get_role()
developer.get_role()