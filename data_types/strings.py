# # Strings in python are surrounded by either single quotation marks, or double quotation marks.
# # 'hello' is the same as "hello".

my_empty_string = ''
print(my_empty_string)
my_empty_string = str()
print(my_empty_string)

my_string = 'Hello\t\tWorld'
print(my_string)
# Python raw string is created by prefixing a string literal with ‘r’ or ‘R’.
# Python raw string treats backslash (\) as a literal character.
my_raw_string = r"hello\t\tworld"
print(my_raw_string)


multiline_string = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
ut labore et dolore magna aliqua.'''
# Note: in the result, the line breaks are inserted at the same position as in the code.
print(multiline_string)
print("------------------------------------------------------------------------")

# string comparison
print('String comparison (\'a\' > \'Z\'):', 'a' > 'Z')
print('aa' > 'ab')
print("------------------------------------------------------------------------")

# Strings are Arrays #
# # Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# # However, Python does not have a character data type, a single character is simply a string with a length of 1.
# # Square brackets can be used to access elements of the string.
s = "0123456789"
print(f"s           => {s}")
print(f"s[2]        => {s[2]}")
print(f"s[2:5]      => {s[2:5]}")
print(f"s[6:1]      => {s[6:1]}")
print(f"s[-5:-2]    => {s[-5:-2]}")
print(f"s[1:8:2]    => {s[1:8:2]}")
# in [i:j:k], if step-size(k) is negative, default value of i will be 'len(s) - 1'
print(f"s[:1:-1]    => {s[:1:-1]}")
print(f"s[1::2]     => {s[1::2]}")
print(f"s[::2]      => {s[::2]}")
print(f"s[::-2]     => {s[::-2]}")
print(f"s[::-1]     => {s[::-1]}")  # reverse of string
print(f"s[999:]     => {s[999:]}")

for x in s:
    print(x, end='-')
print()

if 'xyz' in s:
    print("Found")
print('xyz' not in s)
print("------------------------------------------------------------------------")


first = "Shailesh"
last = "Bachate"
print("My name is " + (first) + " " + (last) + ".")
print(f"My name is {first} {last}.")
print("My name is {} {}.".format(first, last))
print("My name is {1} {0}.".format(first, last.upper()))
print("------------------------------------------------------------------------")


name = "   shailesh Navnath bachatE  "
print(f"name                        => {name}")
# The strip() method removes any whitespace from the beginning or the end.
name = name.strip()
print(f"name.lstrip('sh')           => {name.lstrip('sh')}")
print(f"name.rstrip('tE')           => {name.rstrip('tE')}")
print(f"len(name)                   => {len(name)}")
print(f"name.upper()                => {name.upper()}")
print(f"name.lower()                => {name.lower()}")
print(f"name.isupper()              => {name.isupper()}")
print(f"name.islower()              => {name.islower()}")
print(f"name.capitalize()           => {name.capitalize()}")
print(f"name.title()                => {name.title()}")
print(f"name.istitle()              => {name.istitle()}")
print(
    f"title,capitalize difference => {'2ab p Z'.title()}    |    {'2ab p Z'.capitalize()}")
print(f"name.swapcase()             => {name.swapcase()}")
# # The find() and index() methods find the first occurrence of the specified value.
# # The find() method is almost the same as the index() method, the only difference is that the index() method
# # raises an exception if the value is not found, while the find() method returns -1 if the value is not found.
# # Syntax: string.find(value, start, end)
# # Syntax: string.index(value, start, end)
print(f"name.find('xyz')            => {name.find('xyz')}")
print(f"name.index('sh', 2, 15)     => {name.index('sh', 2, 15)}")
print(f"name.count('sh')            => {name.count('sh')}")
print(f"name.count('sh', 2, 8)      => {name.count('sh', 2, 8)}")
# returns True if the string starts with the specified value
print(f"name.startswith('tE')       => {name.startswith('tE')}")
# returns True if the string ends with the specified value
print(f"name.endswith('tE')         => {name.endswith('tE')}")
# Check if position 2 to 8 ends with the phrase 'sh'
print(f"name.endswith('sh', 2, 8)   => {name.endswith('sh', 2, 8)}")
# replaces all occurences
print(f"name.replace(' ', '_')      => {name.replace(' ', '_')}")
print(f"name                        => {name}")
print("------------------------------------------------------------------------")

# # The center() method will center align the string, using a specified character (space is default) as the fill character.
# # Syntax: string.center(length, character)
print(name.center(40))
# The second argument i.e. the fill character must be exactly one character long
print(name.center(50, '_'))
# Return a 50 characters long, left justified version of the word 'name'
print(name.ljust(50, 'x'))
# right justified means, there will be whitespacees to the left of the name.
print(name.rjust(50))
print("------------------------------------------------------------------------")

# # The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# # The first element contains the part before the specified string. The second element contains the specified string.
# # The third element contains the part after the string.
# # Note: This method search for the first occurrence of the specified string.
mytuple = name.partition('Navnath')
print("Tuple after partition of string:", mytuple)
print("------------------------------------------------------------------------")

# isdecimal() < isdigit() < isnumeric() #
# The isdecimal() method returns True if all characters in a string are decimal characters. If not, it returns False.
# The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
# The isnumeric() method returns True if all characters in a string are numeric characters. If not, it returns False.
print("# isdecimal()    =>", "654".isdecimal(),
      "654.23".isdecimal(), "\u0033".isdecimal())  # True False True
print("# isdigit()      =>", "654".isdigit(), "654.23".isdigit(),
      "\u0033".isdigit())  # True False True # \u0033 is unicode for 3
print("# isnumeric()    =>", "654".isnumeric(),
      "654.23".isnumeric(), "\u0033".isnumeric())  # True False True


# s = '²3455'
# subscript is a digit
s = '\u00B23455'
print("subscript        =>", s.isdecimal(),
      s.isdigit(), s.isnumeric())  # False True True
# s = '½'
# fraction is not a digit
s = '\u00BD'
print("fraction         =>", s.isdecimal(),
      s.isdigit(), s.isnumeric())  # False False True
print("------------------------------------------------------------------------")

# checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9)
print("'qA2'.isalnum()  =>", "qA2".isalnum())
# checks if all the characters of a string are alphabetical (a-z, and A-Z)
print("'qA2'.isalpha()  =>", "qA2".isalpha())
print("------------------------------------------------------------------------")

# # separator.join(iterable) => str # iterable can be list, tuple, string, dictionary, or set #
li = ['ab', 'cddee', 'f\nffff']
print(' '.join(li))
print(''.join(set(li)))
print('_'.join({'one': 1, 'two': 'second'}))
print('.'.join('friends'))

li = [4, 5, 6]

# itos = ''.join(li)  # TypeError: sequence item 0: expected str instance, int found
itos = ''.join(map(str, li))
print(itos)
print("------------------------------------------------------------------------")

# # str.split(separator, maxsplit) => li of strings #
s = " ha ha  ha\nhaha , ha"
# if a separator is not provided, then any whitespace is a separator
print(s.split())
print(s.split(','))

# print(s.split(''))  # ValueError: empty separator
# So if we want to separate every single letter then we should use list() constructor for that`
print(list(s))
print("------------------------------------------------------------------------")

s = " Hello World! hey-there   some_random+stuff - ?!  after-tab"
print(s.split())
print('length:', len(s.split(' ', maxsplit=4)), '|', s.split(' ', maxsplit=4))
print('length:', len(s.split(' ', maxsplit=9)), '|', s.split(' ', maxsplit=9))
print('length:', len(s.split(' ')), '|', s.split(' '))
print(s.split(' ', 2))  # we don't have to write 'maxsplit=2'
print("------------------------------------------------------------------------")
