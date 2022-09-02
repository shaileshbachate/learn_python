import sys

# command line arguments are stored in the form of list in sys.argv
args_list = sys.argv
print("File name:", args_list[0])   # name of file
print("args:", args_list[1:])       # args
print("------------------------------------------------------------------------")

li = list(map(int, args_list[1:]))
print(li)
