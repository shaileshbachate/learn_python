import numpy as np

li = [2,3,4,5]
print(type(li[1:2]))

li_slice = li[1:3]
print("Original:", li, li_slice)

li_slice[0] = 99
print("After modification:", li, li_slice)
print("------------------------------------------------------------------------")

arr = np.array([2,3,4,5])
print(type(arr[1:2]))

arr_slice = arr[1:3]
print("Original:", arr, arr_slice)

arr_slice[0] = 99
print("After modification:", arr, arr_slice)
print("------------------------------------------------------------------------")
