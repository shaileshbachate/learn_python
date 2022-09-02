li = ['p', 'z', 'l', 'x']
en = enumerate(li)

for i, x in en:
    print(i, x, end=' | ')
print()

di = dict(en) # This will be an empty dictionary, as we already traversed through 'en'
print(di)
print("------------------------------------------------------------------------")

li = ['p', 'z', 'l', 'x']
en = sorted(enumerate(li), key=lambda x: x[1])
di = dict(en)
print(di)
print("------------------------------------------------------------------------")

mat = [[1, 2, 3, 4 ], [ 5, 6, 7, 8]]
for i, x in enumerate(mat):
    print(i, x, end=' | ')
print()
print("------------------------------------------------------------------------")
