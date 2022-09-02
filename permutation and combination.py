from itertools import combinations_with_replacement, permutations, combinations

print('# Combinations #')
li = [1, 2, 3, 4]

combs = combinations(li, 2)
print(combs) # <itertools.combinations object at 0x000002157A5CE900>
# print(len(combs))  # # TypeError: object of type 'itertools.combinations' has no len()

# print(len(list(combs))) # # This is correct, but if we use it here, we won't be able to go through combs. 
# # So the following code will not print anything
for x in list(combs):
    print(x, end=' ')
print()

print(len(list(combs))) # This will print 0 here, as we already iterated through the combs iterator.
print("------------------------------------------------------------------------")

li = [1, 2, 3, 4]

# # So, It is better idea to just covert the combinations to list at the beginning only.
combs = list(combinations(li, 2))

for x in list(combs):
    print(x, end=' ')
print()

print(len(list(combs))) # This will give correct value.
print("------------------------------------------------------------------------")

print('# Permutations #')
li = [2, 1, 3, 4]
perms = list(permutations(li, 2))
print(perms)
print(len(perms))
print("------------------------------------------------------------------------")

print('# Combinations with duplicate elements #')
li = [2, 3, 2, 1]
combs = list(combinations(li, 2))
print(combs, '|', len(combs))
combs = list(combinations_with_replacement(li, 2))
print(combs, '|', len(combs))
combs = set(combinations(li, 2))
print(combs, '|', len(combs))
combs = list(combinations(set(li), 2))
print(combs, '|', len(combs))
print("------------------------------------------------------------------------")

print('# Permutations with duplicate elements #')
li = [2, 3, 2, 1]
perms = list(permutations(li, 2))
print(perms, '|', len(perms))
perms = set(permutations(li, 2))
print(perms, '|', len(perms))
print("------------------------------------------------------------------------")

li = [2, 1, 3, 4]
print(len(list(permutations(li, 4))))
