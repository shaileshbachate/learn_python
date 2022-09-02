# Keyword arguments, default parameter value #

def mycalc(child1, child2, child3=10):
    return child1 + 2*child2 + 3*child3

print(mycalc(1, 2, 3))
print(mycalc(1, 2))
print(mycalc(1, child2=2))

# print(mycalc(child1=2, 4, 5)) # SyntaxError: positional argument follows keyword argument
# print(mycalc(1, 2, child2=3)) # TypeError: mycalc() got multiple values for argument 'child2'
print(mycalc(1, 2, child3=3))
print(mycalc(child2=2, child3=3, child1=1))

# def say(message='Hi', times): # SyntaxError: non-default argument follows default argument
#     print(message*times)
print("------------------------------------------------------------------------")

# Arbitrary arguments (*args) #

# If you don't know how many args will be passed into the function, add a * before the parameter name in the function defintion
# This way the function will receive a tuple of arguments, and can access the items accordingly.
def myadd(*values):
    sum = 0
    for x in values:
        sum += x
    return sum

print(myadd(1,2))
print(myadd(1,2,3,4,5))
print(myadd())

def mysub(val1, *values):
    for x in values:
        val1 -= x
    return val1

print(mysub(2,1))
print(mysub(21,1,2,3,4,5))
# print(mysub()) # TypeError: mysub() missing 1 required positional argument: 'val1'
print("------------------------------------------------------------------------")

# Arbitrary keyword arguments (*kwargs) #

# If you don't know how many keyword args will be passed into the function, add ** before the parameter name in the function defintion
# This way the function will receive a dictionary of arguments, and can access the items accordingly.
def printinfo(**info):
    for key in info.keys():
        print(f'{key}  : {info[key]}', end=' | ')
    print()

printinfo(name='shailesh', age=21)
printinfo(name='shailesh', age=21, email='sb@gmail.com')
print("------------------------------------------------------------------------")


def printdetails(name, *income_from_various_sources, **details):
    print(name, sum(income_from_various_sources))
    print('Details: ')
    for key in details.keys():
        print(f'    {key} : {details[key]}')
    print('-'*35)

printdetails('shailesh', 10000, 65000, 45000, age=22, email='sb@gmail.com')
printdetails('shailesh', 10000, 65000, 45000)
printdetails('shailesh', age=22, email='sb@gmail.com')
printdetails('shailesh')
# printdetails(age=22, email='sb@gmail.com') # TypeError: printdetails() missing 1 required positional argument: 'name'
print("------------------------------------------------------------------------")

# def func(name, **details, *income): # SyntaxError: invalid syntax # Parameter cannot follow "**" parameter
#     pass