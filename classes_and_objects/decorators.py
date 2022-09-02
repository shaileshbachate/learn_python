class Employee:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    # After this, email will be treated as property, not a method.
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    
    @email.setter
    def email(self, email):
        self.fullname = email.split('@')[0].replace('.', ' ')

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()
    
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        # # OR we can directly delete 'first' and 'last'. then it will give error if we tried to access 'first', 'last', 'email', 'fullname' later # 
        # del self.first
        # del self.last


emp1 = Employee('shailesh', 'bachate', 22)
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.email)
print("------------------------------------------------------------------------")

emp1.first = 'shubham'
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.email)
print("------------------------------------------------------------------------")

emp1.fullname = 'chetan jadhav'
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.email)
print("------------------------------------------------------------------------")

del emp1.first
# print(emp1.full_name) # AttributeError: 'Employee' object has no attribute 'first'
print("------------------------------------------------------------------------")

emp1.email = 'shailesh.bachate@gmail.com'
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.email)
print("------------------------------------------------------------------------")

del emp1.fullname
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.email)
