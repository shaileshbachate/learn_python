class Employee:
    num_of_employees = 0
    raise_amt = 1.05

    def __init__(self, name="", salary=0):
        self.name = name
        self.salary = salary
        Employee.num_of_employees += 1

    def raise_salary(self):
        self.salary *= self.raise_amt
    
    def change_raise_amt(self, amt):
        self.raise_amt = amt
    
    @classmethod
    def change_raise_amt_of_class(cls, amt):
        cls.raise_amt = amt
        # OR
        # Employee.raise_amt = amt

    @staticmethod
    def create_object_from_string(s):
        name, salary = s.split('-')
        return Employee(name, salary)

    def __str__(self):
        return f"{self.name} {self.salary} {self.raise_amt}"
    
    def __repr__(self):
        return f"Employee({self.name}, {self.salary})"




e1 = Employee("Shailesh", 100000)
print(e1)
print(str(e1))
print(repr(e1))
print(e1.__dict__)

e2 = Employee()
e2.change_raise_amt_of_class(1.2)
print(e2)
print(e2.__dict__)

e3 = Employee.create_object_from_string("john-20000")
print(e3)
e3.change_raise_amt(1.1)
print(e3)
print(e3.__dict__)

Employee.raise_amt = 2
e5 = Employee("temp", 1000)
e5.raise_salary()
print(e5)
e5.raise_amt = 1.5
e5.raise_salary()
print(e5)
print(e5.__dict__)


