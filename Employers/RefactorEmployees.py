
class Salary:
    def __init__(self,salary, bonus):
        self.salary = salary
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.salary * 12) + self.bonus



class Employee:
    raise_amt = 1.25;
    def __init__(self, first_name,last_name, salary,bonus):
        self.first_name = first_name
        self.last_name = last_name
        self.obj = Salary(salary, bonus)

    #Polyporism
    def add_emp(self):
        pass

    # Polyporism
    def remove_emp(self):
        pass

    # Polyporism
    def print_emps(self):
        pass


    def fulldetails(self):
        return f"Employe Name: {self.first_name} + Employe Surname: {self.last_name} + Employe salary: {self.salary}"

    def total_salary(self):
        return self.obj.annual_salary()


