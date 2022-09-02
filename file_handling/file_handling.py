# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "r+" - Read and Write - placing the pointer at the beginning of the file. returns an error if file doesn't exist.

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

f = open('./file_handling/sample.txt')  # default mode is 'rt'

print('current position: ', f.tell())
print(f.read(3))        # reads 3 letters
print('current position: ', f.tell())
print(f.read(3))
print('current position: ', f.tell())

print(f.readline())     # reads a line # in this case, remaining data of the line
print('current position: ', f.tell())
print(f.readlines())    # remaining data in form of a list of lines
print('current position: ', f.tell())

f.seek(5)               # moves current position to nth index
content = f.read()
print(content)         # reads all the remaining data
f.close()

fi = open('./file_handling/output.txt', 'w')
fi.write(content)
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
fi.close()
print("------------------------------------------------------------------------")


with open('./file_handling/output.txt', 'r+') as f:
    print(f.tell())
    f.write('hey \n')      # starts overwriting data, without deleting the whole data at once
    f.writelines(['second line \n', 'third\n']) 

with open('./file_handling/sample.txt', 'a') as f:
    print(f.name)
    print(f.mode)
    print(f.closed)
print("------------------------------------------------------------------------")

# to delete a file we can use os.remove('filename') method in 'os' module
