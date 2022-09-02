d1 = {}
d2 = dict()
d3 = dict([('one', 1), ('two', 2), ('three', None)])
d4 = {1: 'a', 2: 'b', 2: 'c'}  # keys should be unique, 2: 'b' will be ignored here.
print(f"d1, d2, d3, d4: {d1}, {d2}, {d3}, {d4}")
print(f"d3['one'], d3.get('one'): {d3['one']}, {d3.get('one')}")
print(f"d4[2], d4.get(2): {d4[2]}, {d4.get(2)}")
# print(d4[99])  # KeyError: 99
print(d4.get(99))  # no error, prints 'None' as output
print(d4.get(99, 'key not found'))  # we can change the default message(None)

print(f"Lengths: {len(d1)}, {len(d2)}, {len(d3)}, {len(d4)}")
print(f"Types: {type(d1)}, {type(d2)}, {type(d3)}, {type(d4)}")
print("------------------------------------------------------------------------")

# Copy a Dictionary #

# You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

d = d3.copy()
print(d)
d = dict(d4)
print(d)
print("------------------------------------------------------------------------")

# Remove items from dict #
d4 = {1:'one', 'two': 2, 'three': 'third', 'fourth': 4}
del d4[1] # del keyword removes the item with the specified key name
popped_value = d4.pop('three') # pop() method removes the item with the specified key name:
print(f'popped_value: {popped_value}')
# popped_value = d4.pop('qwerty') # KeyError: 'qwerty'
popped_value = d4.pop('qwerty', 'key not found')
print(popped_value)
last_item = d4.popitem() # popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
print(f'last_item: {last_item}')
print(f"d4: {d4}")
d4.clear()  # clear() method empties the dictionary
del d4  # del keyword is used to delete the dictionary itself
# print(d4)  # NameError: name 'd4' is not defined

# Key has to be immutable data type only, that means we can even have a tuple as a key but not a list.
d5 = {(1, 2): 'a'}
# d5 = {[1, 2]: 'a'}  # This will give error: TypeError: unhashable type: 'list'
print(d5, d5[(1, 2)])
print("------------------------------------------------------------------------")

d = {'one': 1, 'two': 2}
for key in d:
    print(f"{key}: {d[key]}")
for value in d.values():
    print(value, end=' ')
print()
for key, value in d.items():
    print(f"{key}: {value}")
print(d.keys(), type(d.keys()))
print(d.values(), type(d.values()))
print(d.items(), type(d.items()))
li_of_items = list(d.items())
print(li_of_items)
print("------------------------------------------------------------------------")

# Add new items to dictionary #
d = {'one': 1, 'two': 2}
mydict = {'one': 10}
mydict['new key'] = 3  # The new key will be added to dictinary.
mydict.setdefault('new key 2', 23)

# print({'one': 1} + {'three': 'third'})  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# mydict += d  # TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'
mydict.update(d)
# mydict.update((45, 'ff')) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
print(mydict)

mydict.setdefault('new key', 99999)  # If the key exist, this has no effect. i.e. the value of 'new key' will still be 3 and not 99999
print(mydict)
mydict.setdefault('new key 3')  # If the key does not exist, this value becomes the key's value. Default value None
print(mydict)
print("------------------------------------------------------------------------")

# dictionary unpacking #
myd = {1: "shailesh", 2: "shubham"}
a, b = myd
print(a, b, myd[a], myd[b])
print("------------------------------------------------------------------------")

# dict comprehensions #
mydict = {x: x**2 for x in range(5)}
print(mydict)

# Update element in nested data type #
x = {'a': [4,5,6], 'b': (11, 22, {'c': 9})}
# x['b'][2] = {'c': 99}  # TypeError: 'tuple' object does not support item assignment
x['b'][2]['c'] = 99  # works fine
print(x)
print("------------------------------------------------------------------------")

# Functions inside dictionary #
def multiply(x, y):
    return x*y

functions_inside_dictionary = {
    'multiply': multiply,
    'add': lambda x, y: x+y,
    'multiply by 2': lambda x: x*2
}

print(functions_inside_dictionary['multiply by 2'](2))
print(functions_inside_dictionary['multiply'](5, 2))
print("------------------------------------------------------------------------")
