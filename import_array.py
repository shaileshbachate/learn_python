import array

li = [3, 8, 2, 1, 6]
print(li, type(li))
print(type(li[0]))
print(len(li))
print("------------------------------------------------------------------------")

# typecode must be b, B, u, h, H, i, I, l, L, q, Q, f or d
arr = array.array('i', li)
print(arr, type(arr))
print(type(arr[0]))
print(len(arr))
print(arr.itemsize)
print("------------------------------------------------------------------------")

arr.reverse()
print(arr)
li = arr.tolist()
print(li, type(li))
print("------------------------------------------------------------------------")

arr2 = array.array('i')
print(arr2)
arr2.append(4)
arr2.append(10)
arr2.insert(0, 7)
print(arr2)
arr2.pop(1) # removes item at index 1
print(arr2)
arr2.remove(10) # removes the item 10 from array
print(arr2)
arr2.pop() # removes last item
print(arr2)
print("------------------------------------------------------------------------")

arr2 = arr + arr2
print(arr2)
arr2.extend([10, 20, 30])
print(arr2)
# arr2 += [45, 55] # TypeError: can only extend array with array (not "list")
arr2 += array.array('i', [45, 55])
print(arr2)
print("------------------------------------------------------------------------")

print(arr2.index(10))
# print(arr2.index(10, 1, 6)) # TypeError: array.index() takes exactly one argument (3 given)
print(arr2.count(10))
# print(arr2.count(10, 1, 6)) # TypeError: array.count() takes exactly one argument (3 given)
print("------------------------------------------------------------------------")

# arr.sort() # AttributeError: 'array.array' object has no attribute 'sort'
arr = sorted(arr) # this will convert the array to sorted list.
print(arr, type(arr))
print("------------------------------------------------------------------------")

arr = array.array('f', [4, -5])
print(arr, arr.itemsize)
# arr = array.array('i', [4, 5.3]) # TypeError: integer argument expected, got float
# arr = array.array('i4', [4, 5]) # TypeError: array() argument 1 must be a unicode character, not str

# arr = array.array('I', [4, -5]) # OverflowError: can't convert negative value to unsigned int
arr = array.array('I', [4, 5])
print(arr, arr.itemsize)

# arr = array.array('b', [23422]) # OverflowError: signed short integer is greater than maximum
arr = array.array('b', [4, 5])
print(arr, arr.itemsize)
print("------------------------------------------------------------------------")

# print(dir(array))
# print(dir(array.array))

