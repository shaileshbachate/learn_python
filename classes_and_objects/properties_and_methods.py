# # Almost everything in Python is an object, with its properties and methods.
# # A Class is like an object constructor, or a "blueprint" for creating objects.

# # The self parameter is a reference to the current instance of the class, 
# # and is used to access variables that belongs to the class.
# # It does not have to be named self , you can call it whatever you like, 
# # but it has to be the first parameter of any function in the class:

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    

emp1 = Employee('Shailesh', 'Bachate')
print(emp1.first_name)  # properties can be accessed directly

# We can directly add new properties #
emp1.age = 22
print(emp1.age)

# Methods #
print(emp1.fullname())
# OR # emp1.fullname() is same as Employee.fullname(emp1)
print(Employee.fullname(emp1))
Employee.__init__(emp1, 'John', 'Doe')
print(emp1.fullname())
print("------------------------------------------------------------------------")

# Delete object property/attribute #
del emp1.first_name
# print(emp1.fullname())  # AttributeError: 'Employee' object has no attribute 'first_name'

# Delete objects #
del emp1
# print(emp1.age)  # NameError: name 'emp1' is not defined

# We can also delete the class, but why would you?!! #
del Employee
# emp2 = Employee("sd", "dsfh")  # NameError: name 'Employee' is not defined
print("------------------------------------------------------------------------")
