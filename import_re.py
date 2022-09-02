# Link: # https://docs.python.org/3/library/re.html

# /w  /W    # /d  /D    # /b  /B    # \s  \S    # \A  # \Z
# .   # [] {} ()    # * + ?    # *? +? ??    # ^ $    # |  -  [^]  \    # (\2)
# re.compile(pattern, flags)
# re.I re.IGNORECASE    # re.VERBOSE
# re.search(pattern, text, flags)    # re.match    # re.finditer    # re.findall
########################################################################################

# # The search() Function #
# # The search() function searches the string for a match, and returns a Match object if there is a match.
# # If there is more than one match, only the first occurrence of the match will be returned.
# # If no matches are found, the value None is returned
########################################################################################

# # Match Object
# # A Match Object is an object containing information about the search and the result.
# # Note: If there is no match, the value None will be returned, instead of the Match Object.

# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
########################################################################################

import re

# match object and search function #
txt = "The rain in Spain"
match = re.search("(a)i", txt)
print("match.start():", match.start())  # 5
print("match.end(): ", match.end())     # 7
print("match.span():", match.span())    # (5, 7)
print("match.span()[0]:", match.span()[0])  # 5
print("match.group(0):", match.group(0))    # ai
print("match.group(1):", match.group(1))    # a
print("match[0]:", match[0])                # ai
print("match[1]:", match[1])                # a
print("match.string:", match.string)        # The rain in Spain
print("------------------------------------------------------------------------")


test = """
'roll': 'BT18CSE103',
'name': 'Shailesh',
'dob': 15-04-1999
"""

# compiled pattern, flags #
pattern = re.compile(r'bt\d\dcse\d{3}', re.I)
# roll = re.search(pattern, test, re.I)  # ValueError: cannot process flags argument with a compiled pattern
roll = re.search(pattern, test)
# # OR 
roll = re.search(r'bt\d\dcse\d{3}', test, re.I)
print(roll[0])
print("------------------------------------------------------------------------")

# re.match(pattern, string, flags=0) #
# If zero or more characters at the BEGINNING of string match the regular expression pattern,
# Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
# If you want to locate a match anywhere in string, use search() instead
match = re.match(r"(t)(est)", "test")
print(match)    # <re.Match object; span=(0, 4), match='test'>
print(match[0])
print(match[1])
print(match[2])
match = re.match(r"(t)(est)", "unit test")
print(match)  # None
print("------------------------------------------------------------------------")

# re.finditer(pattern, string, flags=0) and match object #
matches = re.finditer(r"(\w)(\w\w)", "abcdefghij")
print(matches)  # <callable_iterator object at 0x000002D721D003D0>
for match in matches:
    # print(match)  # <re.Match object; span=(0, 2), match='ab'>
    print(match[0], end=' | ')
    print(match.span(), end=' - ')
    print(match.start(), end=' - ')
    print(match.end(), end=' | ')
    print(match[1], end=' - ')
    print(match.group(2), end=' | ')
    print(match.group(0, 1, 2), end=' | ')  # a tuple of grp 0, grp 1, and grp 2
    print(match.string)
print("------------------------------------------------------------------------")

# re.findall(pattern, string, flags=0) #
# Return all non-overlapping matches of pattern in string, as a list of strings. If no matches are found, an empty list is returned.

# If one or more groups are present in the pattern, return a list of groups; 
# this will be a list of tuples if the pattern has more than one group. Empty matches are included in the result.

print(re.findall(r"\w\w", "abcdefghij"))  # ['ab', 'cd', 'ef', 'gh', 'ij']
print(re.findall(r"(\w)\w", "abcdefghij"))  # ['a', 'c', 'e', 'g', 'i']
print(re.findall(r"(\w\w)\w\w(\w)", "abcdefghij"))  # [('ab', 'e'), ('fg', 'j')]
print("------------------------------------------------------------------------")

# finditer, findall, types #
key1, key2 = re.finditer(r'\b[a-zA-Z]{4}\b', test, re.I)
print(key1[0], key2[0])

matches = re.finditer(r'\b[a-zA-Z]{4}\b', test, re.I)
for match in matches:
    print(match, type(match))
    print(match[0])

matches = re.findall(r'\b[a-zA-Z]{4}\b', test, re.I)
for match in matches:
    print(match, type(match))
print("------------------------------------------------------------------------")

# greedy/non-greedy qualifiers #
test = "1234567890"
match = re.search(r'\d{3,6}', test)  # attempting to match as many repetitions as possible
print(match[0])
match = re.search(r'\d{3,6}?', test) # attempting to match as few repetitions as possible
print(match[0])
match = re.search(r'\d*', test)
print(match[0])
match = re.search(r'\d*?', test)
print(match[0])
match = re.search(r'\d+', test)
print(match[0])
match = re.search(r'\d+?', test)
print(match[0])
match = re.search(r'\d?', test)
print(match[0])
match = re.search(r'\d??', test)
print(match[0])
print("------------------------------------------------------------------------")

# \s #
matches = re.finditer("\s+", "a\nb cd    efg")
for match in matches:
    print(match[0], match.span())
print("------------------------------------------------------------------------")

# re.sub(pattern, repl, string, count=0, flags=0) #
txt = "The rain in Spain"
x = re.sub("\s", "-", txt)  # replace all occurences
print(x)
x = re.sub("\s", "_", txt, 2) # Replace the first two occurrences of a white-space character with _
print(x)
print("------------------------------------------------------------------------")

# Backreferencing and substitution #
test = '''
ahahhaahhahh
https://www.google.com
https://youtube.com
http://qwerty.gov
'''
pattern = r'(https?://)(www.)?(\w+)(.com|.gov)'
newtest = re.sub(pattern, r'\3\4', test)
print(newtest)
print("------------------------------------------------------------------------")
