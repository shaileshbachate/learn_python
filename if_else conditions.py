x = 'shailesh'
y = 'shailesh'

if 0 or "" or None or False or not True or 1 >= 5 or 1 != 1 or x is not y or [] or () or {} or set():
    print("This will not be printed")
elif -1 and 7 and True and not False and 1 < 5 and 1 == 1 and x is y and [1, 3] and "hello" and {"one": 1, "two": 2} and {9}:
    print("hey there")
else:
    print("WTF")
print("------------------------------------------------------------------------")

# ternary operator #
print(True) if 5 > 10 else print(False)

# single line if elif else #
print(10) if len(x) == 10 else print(6) if len(x) == 6 else print(len(x))
print("------------------------------------------------------------------------")


li = []
if li is None:
    print('None')
elif li == None:
    print('None')
else:
    print('li is not None, but it is an empty list')
