# Syntax : hash(obj) # returns the hashed value if possible
# Internally, hash() method calls __hash__() method of an object which is set by default for any object.

int_val = 5
float_val = 5.00
float_val2 = 4.43
str_val = '5'
print(hash(int_val), hash(float_val), hash(float_val2))  # 5 5 991512493961887748
print(hash(str_val))  # variable value!

s = "Look at me!"
print(hash("Look at me!"), hash(s))  # same values for both
print("------------------------------------------------------------------------")

# # hash() returns hashed value only for immutable objects, hence can be used as an indicator to check for mutable/immutable objects.
tuple_val = (1, 2, 3)
print(hash(tuple_val))  # 529344067295497451

list_val = [1, 2, 3]
# print(hash(list_val))  # TypeError: unhashable type: 'list'
print("------------------------------------------------------------------------")

# There are many hash functions defined in the “hashlib” library in python.
import hashlib

# print(hashlib.md5("Shailesh"))  # TypeError: Unicode-objects must be encoded before hashing
name = "Shailesh"
result = hashlib.md5(name.encode())
# print(result)  # <md5 _hashlib.HASH object @ 0x0000028EDBEDAAF0>
print(result.digest())
# Explanation : The above code takes byte and can be accepted by the hash function. 
# The md5 hash function encodes it and then using digest(), byte equivalent encoded string is printed.

print(hashlib.md5(b'Shailesh').digest())
print(hashlib.md5(name.encode('utf-8')).digest())
print(hashlib.md5(b'Shailesh').hexdigest())
print(hashlib.md5(name.encode()).hexdigest())
print("------------------------------------------------------------------------")
