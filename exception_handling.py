# try:
# except:
    # except:
    # except ParticularErrorName:
    # except Exception:
    # except ParticularErrorName as ex:
    # except Exception as e:
# else:
# finally:


try:
    print(x)
    # pass
except NameError:
    print("# NameError # name 'x' is not defined!!!")
except TypeError:
    print("Type error")
except ValueError:
    print("Value error")
except SyntaxError:
    print("# SyntaxError # invalid syntax")
except:
    print("Some error")
else:
    print("If there is no error, this line will be printed")
finally:
    print("This line will be printed regardless if the try block raises an error or not!!!\n")
print("------------------------------------------------------------------------")


try:
    print(5 + " : five")
except NameError as ex:
    print(f"# NameError #: {ex}!!!\n")
except TypeError as ex:
    print(f"# TypeError #: {ex}!!!\n")
except Exception as ex:
    print(f"Error: {ex}!!!\n")
print("------------------------------------------------------------------------")


def fun(x):
    if x > 10:
        raise Exception(f"x({x}) should be less than 10")
    print(x)

def fun2(arr, i):
    if i >= len(arr):
        raise IndexError("index out of range !!!\n")
    print(arr[i])

try:
    fun(4)
    fun(12) # If this line raises an exception, the next lines in the try block will not be executed
    fun(5)
except Exception as ex:
    print(f"Some error: {ex}!!!\n")

try:
    fun2([1,2,3,4], 10)
except IndexError as ex:
    print(f"# Index Error # {ex}")
print("------------------------------------------------------------------------")


print("THE END".center(72, '_'))
