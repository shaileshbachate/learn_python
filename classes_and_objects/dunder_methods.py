class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def fullname(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return f"{self.first} {self.last} {self.salary}"
    
    # we should atleast have __repr__ method, because in case __str__ is called when __str__ is not defined, 
    # it falls back to __repr__, and __repr__ is executed
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.salary}')"

    def __len__(self):
        return len(self.fullname())

    def __add__(self, other):    
        return self.salary + other.salary
        

emp1 = Employee('shailesh', 'bachate', 150000)
emp2 = Employee('shubham', 'bachate', 100000)

print(emp1) # prints same output as print(str(emp1))
print("------------------------------------------------------------------------")

print(repr(emp1))
print(emp1.__repr__())
print(str(emp1))
print(emp1.__str__())
print("------------------------------------------------------------------------")

print(len(emp1), len(emp2))
print("------------------------------------------------------------------------")

print(emp1 + emp2)
print(emp1.__add__(emp2))
print("------------------------------------------------------------------------")

print(2+4)
print(int.__add__(2, 4))
