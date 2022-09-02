int_from_str = int(" 2 ")
# int_from_str2 = int("3.45")  # ValueError: invalid literal for int() with base 10: '3.45'
int_from_str2 = int(float("3.45"))
print(int_from_str)
print(int_from_str2)

num_in_str = "345.435"
num_in_float = float(num_in_str)
print("My age is: " + str(int(num_in_float/10)))
print(num_in_float + 5.2)
print("------------------------------------------------------------------------")

x = "01100001"
print(int(x, 2))        # 97
print(chr(int(x, 2)))   # a
print(chr(65))          # A
# print(chr('a'))       # TypeError: an integer is required (got type str)
print("------------------------------------------------------------------------")

# ASCII values of characters
print(f"ord('a')    =>  {ord('a')}")     # 97
print(f"ord('Z')    =>  {ord('Z')}")     # 90
print(f"ord('7')    =>  {ord('7')}")     # 53
# print(ord(5))     # TypeError: ord() expected string of length 1, but int found
# print(ord('abc')) # TypeError: ord() expected a character, but string of length 3 found
print("------------------------------------------------------------------------")

# print(oct('12'))  # TypeError: 'str' object cannot be interpreted as an integer
print(bin(12), type(bin(12)))   # 0b1100  # <class 'str'>
print(oct(12), type(oct(12)))   # 0o14    # <class 'str'>
print(hex(12), type(hex(12)))   # 0xx     # <class 'str'>

print(int(0b1100))  # 12
print(int(0o14))    # 12
print(int(0xc))     # 12

# print(int('0b1100')) ValueError: invalid literal for int() with base 10: '0b1100'
print(int('0b1100', 2))     # 12
print("------------------------------------------------------------------------")

print(bool(""), bool("hey"))
print(bool(0), bool(5), bool(-1))
print(bool({}), bool((2,3)))
print("------------------------------------------------------------------------")
