import platform

print(dir(platform))
print("------------------------------------------------------------------------")

print("system:", platform.system())
print("processor:", platform.processor())
print("architecture:", platform.architecture())
print("machine:", platform.machine())
print("node:", platform.node())
print("platform:", platform.platform())
print('Python build no. and date:', platform.python_build())
print('Python compiler:', platform.python_compiler())
print("------------------------------------------------------------------------")
