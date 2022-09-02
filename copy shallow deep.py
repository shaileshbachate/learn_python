li1 = [1,2,3]
li2 = [4,5,6]
li3 = [7,8,9]

li = [li1, li2, li3]
print(li)
ref_to_li = li
shallow_copy_of_li = li.copy() # li.copy() and list(li), both return shallow copy of a list

li.append('b')  # 'b' will be present in the 'ref_to_li' but not in 'shallow_copy_of_li'
li[0][1] = 20   # both 'ref_to_li' and 'shallow_copy_of_li'are modified
li2[2] = 60     # both 'ref_to_li' and 'shallow_copy_of_li'are modified
li[2] = [70, 80, 90]  # only 'ref_to_li' is modified but 'shallow_copy_of_li' isn't

print(ref_to_li)
print(shallow_copy_of_li)

