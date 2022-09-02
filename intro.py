
# Arithmetic
a = 4
b = 5
print(b/a)   # 1.25
print(b//a)  # 1
print(b*a)   # 20
print(-2 % 2)  # 0
print(b**a)  # 625
print(25**2.5)  # 3125.0
# print(b += a) # SyntaxError: invalid syntax
b += a
print(b)     # 9
print("------------------------------------------------------------------------")

name = "Shailesh"

# print(name + 9)      # TypeError: can only concatenate str (not "int") to str
# print(4 + "shai")    # TypeError: unsupported operand tṆype(s) for +: 'int' and 'str'
# print(f"4{"shail"}")  # SyntaxError: f-string: expecting '}'
print(f"4 {'shail'}")
print(f"{2+2} {name}")
print("4 {} {}".format(name, "Bachate"))
print("Hello", end=', ')
print("World", end="!!!\n")
print("------------------------------------------------------------------------")

really_long_number = 788888888888888888888888888888888877777777777777
really_long_decimal_number = 7888888888888888888888888888888888789689689.5461
boolean_value = True
mylist = ["one", 2, True, 3.4]

# Set items are unordered(and unindexed), unchangeable, and do not allow duplicate values.
myset = {"one", 2, 4.5, False}
# Dictionary items are ordered, changeable, and does not allow duplicates.
mydict = {"one": 1, 2: True}

print(f"(Text Type) string value: {name}")
print(f"(Numeric Type) int value: {really_long_number}")
print(f"(Numeric Type) float value: {really_long_decimal_number}")
print(f"(Boolean Type) Boolean value: {boolean_value}")
print(f"(Sequence Type) List: {mylist}")
print(f"(Set Type) Set: {myset}")
print(f"(Mapping Type) Dict: {mydict}")

print(f"value: {mydict['one']}")
print(f"value: {mydict[2]}")

print(type(name))
print(type(really_long_number))
print(type(really_long_decimal_number))
print(type(boolean_value))
print(type(myset))
print(type(mydict))
print(type(mylist))
print("------------------------------------------------------------------------")

# Using eval is not recommended. (due to security risks)
eval("print(min([3,21,11,4,7,12]))")

eval(f"print({input()*4})")  # for input 5, result will be => 5555
eval(f"print({input()}*4)")  # for input 5, result will be => 20
eval(f"print(4*{input()})")  # for input 5, result will be => 20

eval(input("Enter something to evaluate and run: "))
