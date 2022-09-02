# Tuple items are ordered, unchangeable, and allow duplicate values.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
t1 = ()
print(type(t1))
i = (5)  # this will be considered as int
print(type(i))  # <class 'int'>
# # To create a tuple with only one item, you have to add a comma after the item, 
# # otherwise Python will not recognize it as a tuple.
t2 = (5,)
print(type(t2))
t3 = tuple([3, 2, 23, 23])
print(i, t1, t2, t3)
print(*t3)
print("------------------------------------------------------------------------")

# Tuple unpacking #
print('# Tuple unpacking #')
t = (2, 4.3, True, "hey")
a, b, c, d = t
print(a, b, c, d)

# Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.
a, *b = t
# b will be a list of remaining values of tuple
print(type(a), type(b), a, b)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green, tropic, red)
print("------------------------------------------------------------------------")

# we also use tuple unpacking in for loops
print('# tuple unpacking in for loops #')
li = [(1,2), (3,4)]
for x, y in li:
    print(x, y)
print("------------------------------------------------------------------------")

# Swapping two numbers #
print('# swapping two numbers #')
x = 34
y = 56
x, y = y, x
print(x, y)
print("------------------------------------------------------------------------")

# Concatenate two or more tuples #
print('# Concatenate two or more tuples #')
t = t1 + t2 + t
print(t)

# multiply tuples #
print('# multiply tuples #')
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# Delete tuple #
# # We can delete the tuple entirely but not individual items
# del t[0]  # TypeError: 'tuple' object doesn't support item deletion
del t
# print(t)  # NameError: name 't' is not defined
print("------------------------------------------------------------------------")

# # You can't add elements to a tuple because of their immutable property. 
# # There's no append() or extend() method for tuples, 
# # You can't remove elements from a tuple, also because of their immutability.


# returning multiple values from function #
def myfun():
    return 1,2,3

print(type(myfun()))  # <class 'tuple'>
print(myfun())
a, b, c = myfun()
print(a, b, c)
print("------------------------------------------------------------------------")

# This is not same as list comprehension, here a 'generator object' is created instead of a tuple.
go = (x**2 for x in [2,3,4,5])
print(go)  # <generator object <genexpr> at 0x0000024ED006EA50>
for y in go:
    print(y, end=' ')  # 4 9 16 25
print()
print("------------------------------------------------------------------------")

# Tuple methods #
print('# Tuple methods #')
t = (0, 4, 1, 14, 4, 9)
print(f'sum(t)          => {sum(t)}')
print(f'max(t)          => {max(t)}')
print(f'min(t)          => {min(t)}')
print(f'all(t)          => {all(t)}')
print(f'any(t)          => {any(t)}')
print(f't.count(4)      => {t.count(4)}')
# print(f't.count(4)       => {t.count(4, 2, 4)}') # TypeError: tuple.count() takes exactly one argument (3 given)
print(f't.index(4)      => {t.index(4)}')
print(f't.index(4,2,5)  => {t.index(4, 2, 5)}')
print("------------------------------------------------------------------------")
