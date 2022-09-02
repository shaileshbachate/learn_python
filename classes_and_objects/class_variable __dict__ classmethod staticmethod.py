class Employee:
    num_of_emps = 0
    raise_amt = 1.05
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_emps += 1

    def raise_salary(self):
        self.salary = int(self.salary * self.raise_amt)

    def change_raise_amt(self, r_a):
        self.raise_amt = r_a

    @classmethod
    def change_raise_amt_class_method(cls, r_a):
        cls.raise_amt = r_a
        # # OR #
        # Employee.raise_amt = r_a

    # here, the following method will work same as the above one(change_raise_amt_class_method).
    @staticmethod
    def change_raise_amt_static_method(r_a):
        Employee.raise_amt = r_a

    @classmethod
    def create_object_from_string(cls, string):
        name, pay = string.split('-')
        return cls(name, pay)


print(Employee.num_of_emps)
emp1 = Employee('shailesh', 100000)
print(emp1.num_of_emps)

emp2 = Employee('shubham', 100000)
print(emp1.num_of_emps)

emp3 = Employee('chetan', 100000)
print(emp1.num_of_emps)
print(Employee.num_of_emps)
print("------------------------------------------------------------------------")

emp1.raise_salary()
print(emp1.salary)

emp2.raise_amt = 1.1
emp2.raise_salary()
print(emp2.salary)

emp3.raise_salary()
print(emp3.salary)

print(emp1.raise_amt, emp2.raise_amt, emp3.raise_amt)
print(Employee.raise_amt)
print("------------------------------------------------------------------------")

Employee.change_raise_amt_class_method(1.2)
# # OR #
# emp1.change_raise_amt_class_method(1.2)

emp1.raise_salary()
print(emp1.salary)
emp2.raise_salary()
print(emp2.salary)
emp3.raise_salary()
print(emp3.salary)

print(emp1.raise_amt, emp2.raise_amt, emp3.raise_amt)
print(Employee.raise_amt)
print("------------------------------------------------------------------------")

# Employee.change_raise_amt_static_method(1.5)
# # OR #
emp1.change_raise_amt_static_method(1.5)

emp1.raise_salary()
print(emp1.salary)
emp2.raise_salary()
print(emp2.salary)
emp3.raise_salary()
print(emp3.salary)

print(emp1.raise_amt, emp2.raise_amt, emp3.raise_amt)
print(Employee.raise_amt)
print("------------------------------------------------------------------------")

emp1.change_raise_amt(2)

emp1.raise_salary()
print(emp1.salary)
emp2.raise_salary()
print(emp2.salary)
emp3.raise_salary()
print(emp3.salary)

print(emp1.raise_amt, emp2.raise_amt, emp3.raise_amt)
print(Employee.raise_amt)
print("------------------------------------------------------------------------")

# __dict__ #
print(emp1.__dict__) # shows all the attributes of the object and their values
print(emp2.__dict__)
print(emp3.__dict__)
print(Employee.__dict__) # shows all the attributes of the class and their values
print("------------------------------------------------------------------------")

emp4 = Employee.create_object_from_string('mangesh-400000')
print(emp4.__dict__)
