from collections import defaultdict


a = defaultdict(set)
a[0].add(5)
a[0].add(9)
print(a)
print(a[0])
print("------------------------------------------------------------------------")

d = defaultdict(list)
print(d)

d['a'] = [1, 2, 3]
print(d['a'])
print(d['a'][0])
print(d[100], type(d['qwe']))
print(d[(23, 14)].append(12))
# print(d['e'][0])  # IndexError: list index out of range
print(d)
print("------------------------------------------------------------------------")

cart = defaultdict(int)

print(cart['apple'])
cart['orange'] += 1
cart['orange'] += 1
print(cart['orange'])
print(cart)
print("------------------------------------------------------------------------")
