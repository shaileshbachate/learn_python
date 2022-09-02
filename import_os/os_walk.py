import os


print(os.walk('.'), type(os.walk('.')))

for x in os.walk('.'):
    print(x, type(x))
print("________________________________________________________________________")

for dirpath, dirnames, filenames in os.walk('.'):
    print(dirpath, type(dirpath))
    [print(dirname, type(dirname), end='; ') for dirname in dirnames]
    print(type(dirnames))
    [print(filename, type(filename), end='; ') for filename in filenames]
    print(type(filenames))
    print("------------------------------------------------------------------------")
print("________________________________________________________________________")


replicating_oswalk_structure = [(1,['a','b'],['i','j','k']), (2,['c','d','e'],['l','m','n'])]
for x in replicating_oswalk_structure:
    print(x)

for x, y, z in replicating_oswalk_structure:
    print(x)
    [print(yi, end=' ') for yi in y]
    print()
    [print(zi, end=' ') for zi in z]
    print()
    print("------------------------------------------------------------------------")
