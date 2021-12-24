from Employers.RefactorEmployees import Employee
class AirportEmployees(Employee):
    raise_amt = 1.10
    def __init__(self, first_name, last_name, salary, position, workingarea, employees=None):
        super().__init__(first_name, last_name, salary)
        self.position = position
        self.workingarea = workingarea
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, empname):
        if empname not in self.employees:
            self.employees.append(empname)

    def remove_emp(self, empname):
        if empname in self.employees:
            self.employees.remove(empname)

    def print_emps(self):
        for empname in self.employees:
            print('-->',
                  f"This employer's name: {empname}")



