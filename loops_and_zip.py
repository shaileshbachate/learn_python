# while #
x = 0
while x < 4:
    print(x, end=' ')
    x += 1
print(x + x)  # 8

# for #
for x in range(4):
    print(x, end=' ')
print(x + x)  # 6
print("------------------------------------------------------------------------")

# zip() #
li = [1, 3, 4, 5]
li2 = [7, 8, 9]
for x, y in zip(li, li2):
    print(f"{x}, {y}; ", end=" ")
print()

li3 = [10,20,30]
li4 = list(zip(li, li2, li3))
print(li4)
print("------------------------------------------------------------------------")

for x in 2, 3, 4, 5:
    print(x, end=' ')
print()

li = [1, 3, 4, 5]
li2 = [7, 8, 9]
for x in li, li2:
    print(x, end=' ')
print()
print("------------------------------------------------------------------------")

# else in for loop #
for x in range(6):
    print(x, end=' ')
else:
    print("\nFinally finished!")
print("------------------------------------------------------------------------")

# break, continue, pass
for x in range(10):
    if x > 7:
        break
    elif x == 5:
        continue
    elif x < 3:
        pass
    else:
        print(x, end=' ')
else:
    print("This will not be printed")
# # Note: The else block will NOT be executed if the loop is stopped by a break statement.
print()
print("------------------------------------------------------------------------")
