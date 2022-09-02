import os

# print(dir(os))
print(os.getcwd())

try:
    os.chdir('./import_os')
    print(os.getcwd())
except:
    pass

os.mkdir('./test')
print(os.listdir())
os.rmdir('./test')
print(os.listdir())

os.makedirs('test/folder')
print(os.listdir('./test'))
os.removedirs('test/folder')

try:
    os.rename('../test.txt', 'sample.txt')
    print('moved and renamed successfully')
except FileNotFoundError:
    print('File not found')

print(os.stat('sample.txt'))
print("------------------------------------------------------------------------")

# environment variables
print(os.environ.get('userprofile'))
print("------------------------------------------------------------------------")

# print(dir(os.path))

folder = '\\docs\\folder'
filename = 'test.txt'
path = os.path.join(folder, filename)
print(path)

print(os.path.dirname(path))
print(os.path.basename(path))

dir_name, base_name = os.path.split(path)
print(dir_name, base_name)

name, extension = os.path.splitext(path)
print(name, extension)
print("------------------------------------------------------------------------")

print(os.path.exists(path))
print(os.path.isdir('sample.txt'))
print(os.path.isfile('sample.txt'))
print("------------------------------------------------------------------------")

if os.path.exists("demo.txt"):
  os.remove("demo.txt")
  print('file removed successfully')
else:
  print("The file does not exist")
