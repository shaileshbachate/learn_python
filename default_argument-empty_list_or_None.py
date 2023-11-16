# if we directly write arg = [], then each time the function is called without parameter, same list will be used.
def wrong_use_of_default_arg(arg=[]):
    arg.append(4)
    return arg


a = wrong_use_of_default_arg()
print(a)  # [4]
b = wrong_use_of_default_arg()
print(b)  # [4, 4]
c = wrong_use_of_default_arg()
print(c)  # [4, 4, 4]
print("------------------------------------------------------------------------")


def right_use_of_default_arg(arg=None):
    arg = arg or []
    arg.append(4)
    return arg


a = right_use_of_default_arg()
print(a)  # [4]
b = right_use_of_default_arg()
print(b)  # [4]
c = right_use_of_default_arg()
print(c)  # [4]
print("------------------------------------------------------------------------")


def counter(n=[0]):
    n[0] += 1
    return n[0]


print(f"The function was called {counter()} times")
print(f"The function was called {counter()} times")
print(f"The function was called {counter()} times")
