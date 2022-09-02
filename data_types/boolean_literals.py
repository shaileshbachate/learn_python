x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print(True + False)  # 1
print("x is", x)    # x is True
print("y is", y)    # y is False
print("a:", a)      # a: 5
print("b:", b)      # b: 10

# In Python, True represents the value as 1 and False as 0.
# The value of x is True because 1 is equal to True. And, the value of y is False because 1 is not equal to False.
# Similarly, we can use the True and False in numeric expressions as the value.
print("------------------------------------------------------------------------")


z = ([] == True)
print("z is", z)    # z is False
z = ([] == False)
print("z is", z)    # z is False


def fun():
    return True


print(fun() + 1)
