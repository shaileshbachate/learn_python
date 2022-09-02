# Protected Access Modifier:
# The members of a class that are declared protected are only accessible to a class derived from it. 
# Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class. 

# Private Access Modifier:
# The members of a class that are declared private are accessible within the class only, 
# private access modifier is the most secure access modifier. 
# Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class. 


class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 2    # private
        self._c = 3     # protected
 
    def displayB(self):
        return self.__b


class Derived(Demo):
    def __init__(self):
        Demo.__init__(self)
    
    def displayB_derived(self):
        return self.__b


obj = Demo()

print(obj.displayB())
# print(obj.__b)  # AttributeError: 'Demo' object has no attribute '__b'
# ANSWER: The program has an error because b is private and hence can’t be printed
# Explanation: Variables beginning with two underscores are said to be private members of the class and they can’t be accessed directly.

obj2 = Derived()
print(obj2._c)
print(obj2.displayB())
# print(obj2.displayB_derived())  # AttributeError: 'Derived' object has no attribute '_Derived__b'
