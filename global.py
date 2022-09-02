a = 1
def fun1():
    print(a)  # 1
fun1()
print(a)  # 1
print("------------------------------------------------------------------------")

b = 2
def fun2():
    print(b)  # local variable 'x' referenced before assignment
    b = 20
# fun2()  # UnboundLocalError: local variable 'x' referenced before assignment
print("------------------------------------------------------------------------")


c = 3
def fun3():
    c = 4
    print(c)  # 4
fun3()
print(c)  # 3
print("------------------------------------------------------------------------")


d = 5
def fun3():
    global d
    d = 50
    print(d)  # 50
fun3()
print(d)  # 50
print("------------------------------------------------------------------------")
