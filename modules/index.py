# # Consider a module to be the same as a code library.
# # A file containing a set of functions, variables of all types (arrays, dictionaries, objects etc) you want to include in your application.

import mymod
from mymod2 import divide, student, Manager
from mymod3 import *
import mymod4 as m4

print(mymod.add(15, 6))
print(mymod.person["name"])
dev1 = mymod.Developer('Chetan', 'Jadhav')
print(dev1.fullname())
print("------------------------------------------------------------------------")

# # Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# # Example: divide(15,6), not mymod2.divide(15,6)
print(divide(15, 6))
print(student['roll'])
mngr1 = Manager('shubham', 'bachate')
print(mngr1.fullname())
print("------------------------------------------------------------------------")

print(myfloor(3.4))
print(myceil(3.4))
emp1 = Employee('shailesh', 'bachate')
print(emp1.fullname())
print("------------------------------------------------------------------------")

print(m4.li)
print("------------------------------------------------------------------------")

# # The dir() function is a built-in function to list all the function names (or variable names) in a module.
# # Note: The dir() function can be used on all modules, also the ones you create yourself.
print(dir(mymod))
# print(dir(mymod2))    # NameError: name 'mymod2' is not defined
# print(dir(mymod4))    # NameError: name 'mymod4' is not defined
print(dir(m4))
print("------------------------------------------------------------------------")
