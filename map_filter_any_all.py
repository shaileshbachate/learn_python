# 'map', 'filter', 'all' and 'any' methods in python are somewhat similar to 'map', 'filter', 'every' and 'some' methods in JavaScript...

# Syntax # map(function_object, iterable1, iterable2, ...)
# Syntax # filter(function_object, iterable)
# Unlike map function, filter function can take only one iterable as input

def add(x, y):
    return x+y


li = [10, 20, 30, 40]
li2 = [1, 2, 3, 4]
# print(map(add, li, li2))  # <map object at 0x000001DB85122F70>
print(tuple(map(add, li, li2)))
for x in map(add, li, li2):
    print(x, end=' ')
print()
print("------------------------------------------------------------------------")

map(lambda x: print("#"*(x//10)), li)   # This will not print anything
# we can achieve the desired result using list comprehension instead of map
[print("#"*(x//10)) for x in li]
print("--------------------------------------------------------------")
list(map(lambda x: print("#"*(x//5)), li))  # This will print the result
print("--------------------------------------------------------------")
# This will print the result
[_ for _ in map(lambda x: print("#"*(x//10)), li)]
print("------------------------------------------------------------------------")


li = [{'name': 'Shailesh', 'age': 22}, {
    'name': 'Chetan', 'age': 20}, {'name': 'Shubham', 'age': 17}]
# print(filter(lambda x: x['age'] > 18, li))  # <filter object at 0x000001DB85122F70>
for x in filter(lambda x: x['age'] > 18, li):
    print(x, end=' ')
print()
print("------------------------------------------------------------------------")


list_of_students_whose_age_is_above_18 = list(
    map(lambda x: x['name'], filter(lambda x: x['age'] > 18, li)))
print(list_of_students_whose_age_is_above_18)
print("------------------------------------------------------------------------")

# Python any() and all() Functions
# Syntax: # any(iterable) # all(iterable)
# iterable object can be a list, tuple, dictionary etc
li = [2, 0]
se = {0, '', False}
tu = (True, 1, "SH")
di = {1: '', 'SHai': False}
# Note: When used on a dictionary, the any() function checks if any of the keys are true, not the values.
# Note: When used on a dictionary, the all() function checks if all the keys are true, not the values.
print(any(li), all(li))
print(any(se), all(se))
print(any(tu), all(tu))
print(any(di), all(di))
print("------------------------------------------------------------------------")
