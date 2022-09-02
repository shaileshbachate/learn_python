# # A lambda function is a small anonymous function.
# # A lambda function can take any number of arguments, but can only have one expression. # Python expressions cannot contain statements
# # SYNTAX # lambda arguments : expression

fun = lambda x: print(x)
fun(500)

add = lambda x, y: x + y
print(add(3,4))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
    return lambda x: x*n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(5))
print(mytripler(5))
print("------------------------------------------------------------------------")

for x in map(lambda x: x*2, [1,2,3,4]):
    print(x, end=' ')
print()
print("------------------------------------------------------------------------")

li = list(map(lambda x, y: x - y, [10, 20, 30, 40], [1,2,3,4]))
print(li)
print("------------------------------------------------------------------------")

li = list(map(add, [10, 20, 30, 40, 50], [1,2,3,4]))
print(li)
print("------------------------------------------------------------------------")

li = [0,1,2,3,4,5,6,7,8,9]
li_even = list(filter(lambda x: not x%2, li))
li_odd = list(filter(lambda x: x%2, li))
print(li_even, li_odd)
print("------------------------------------------------------------------------")
