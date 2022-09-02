import json

dict = {
    'id': 1,
    'subjects': {'DSPD': 'k', 'IOOM': 'm'},
    'name': 'Shailesh',
    'roll': 103,
    'lang': ('Mar', 'Eng')
}

# The dump() method is used when the Python objects have to be stored in a file.	

# dump(dict, fp, indent=0, sort_keys=0, separators=(',', ': '))
with open('./import_json/myjsonfile.json', 'w') as f:
    json.dump(dict, f)

with open('./import_json/myjsonfile2.json', 'w') as f:
    json.dump(dict, f, indent=4)

with open('./import_json/myjsonfile3.json', 'w') as f:
    json.dump(dict, f, indent=4, sort_keys=True)
print("------------------------------------------------------------------------")


# The dumps() is used when the objects are required to be in string format and is used for parsing, printing, etc, .

# dumps(dict, indent=0, sort_keys=0, separatos=(',', ': '))
myjsonstring = json.dumps(dict)
print(myjsonstring)

myjsonstring2 = json.dumps(dict, indent=4)
print(myjsonstring2)

myjsonstring3 = json.dumps(dict, indent=4, sort_keys=True)
print(myjsonstring3)

myjsonstring4 = json.dumps(dict, indent=4, sort_keys=True, separators=(';', ' = '))
print(myjsonstring4)
print("------------------------------------------------------------------------")

mydict = json.loads(myjsonstring)
print(mydict)
mydict = json.loads(myjsonstring2)
print(mydict)
print("------------------------------------------------------------------------")

# Python	        JSON
# dict	            Object
# list	            Array
# tuple	            Array
# str	            String
# int	            Number
# float	            Number
# True	            true
# False	            false
# None	            null

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
