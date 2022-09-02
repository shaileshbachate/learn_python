empty_dict = {}
print(type(empty_dict))
empty_set = set()
print(type(empty_set))

# # Set items are unordered, unchangeable, and do not allow duplicate values.
myset = {"a", "b", "c", "a", False}

# # Sets are unordered, so you cannot be sure in which order the items will appear.
print("set: " + str(myset))

print(f"Type: {type(myset)}")  # Type: <class 'set'>
print(f"length of set: {len(myset)}")

# The set() constructor
myset1 = set("shailesh")
myset2 = set([1, "a", True, 7.8])
myset3 = set(("b", 2, 2, "c", "b"))
myset4 = set({1, "a", True, 7.8})
myset5 = set({"One": 100, "Two": 200})
myset6 = {x for x in range(5)}
print(myset1, myset2, myset3, myset4, myset5)
print(type(myset6), myset6)

# Access Set items
# # You cannot access items in a set by referring to an index or a key.
# # But you can loop through the set items using a for loop,
# # or ask if a specified value is present in a set, by using the in keyword.
print("found") if "a" in myset else print("not found")
for x in myset:
    print(x, end=" ")
print()
print("------------------------------------------------------------------------")


# s = {{1, 2}, {3, 4}} # TypeError: unhashable type: 'set'
# s = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
s = {(1, 2), (3, 4)}
print(s)
print("------------------------------------------------------------------------")


# Change Items #
# # Once a set is created, you cannot change its items, but you can add new items.

# Add Items #
myset.add("d")
print(f"After using add(): {myset}")

# print(myset+myset2)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# Add Any Iterable #
# # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
myset.update({"e", "f", "g"})
myset.update([1, 4, 5])
myset.update({"Three": 100, "Four": 200})
print(myset)


# Remove Item
# # If the item to remove does not exist, remove() will raise an error.
myset.remove("Four")
print(f"After using remove(): {myset}")
# # If the item to remove does not exist, discard() will NOT raise an error.
myset.discard("Four")
print(f"After using discard(): {myset}")

# # You can also use the pop() method to remove an item, but this method will remove the last item.
# # Remember that sets are unordered, so you will not know what item that gets removed.
# # The return value of the pop() method is the removed item.
popped_item = myset.pop()
print(f"popped item: {popped_item}")

# # The clear() method empties the set:
myset.clear()
print(myset)

# # The del keyword will delete the set completely:
del myset2
# print(myset2)  # NameError: name 'myset2' is not defined
print("------------------------------------------------------------------------")


s1 = {1, 2, 3, 40, 54, 34}
s2 = {11, 22, 33, 40, 96}

# UNION #
s3 = s1 | s2
# OR
s4 = s1.union(s2)
print(s3, s4)

# INTERSECTION #
s5 = s1 & s2
s6 = s1.intersection(s2)
print(s5, s6)

# DIFFERENCE
s7 = s1 - s2
s8 = s1.difference(s2)
s72 = s2 - s1
s82 = s2.difference(s1)
print(s7, s8, ";", s72, s82)

# SYMMETRIC DIFFERENCE
s9 = s1 ^ s2
s10 = s1.symmetric_difference(s2)
s92 = s2 ^ s1
s102 = s2.symmetric_difference(s1)
print(s9, s10, ";", s92, s10)
print("------------------------------------------------------------------------")

s1 = {0, 1, 4, 54, 34}
print(sum(s1))
print(max(s1))
print(min(s1))
print(all(s1))
print(any(s1))
print("------------------------------------------------------------------------")

s1 = {2, 3, 4}
s2 = {4, 6, 3, 5, 1, 2}
print(s1.issubset(s2), s1|s2 == s2)
print(s2.issuperset(s1), s1|s2 == s2)
print(s1.isdisjoint(s2), not s1&s2)

s2 = {6,7,8}
print(s1.isdisjoint(s2), not s1&s2)
print(s1, s2)
print("------------------------------------------------------------------------")

# Comparing sets #
s1 = {1, 2, 3, 4}
s2 = {2, 4, 3, 1}
if s1 == s2: print("Equal")
if s1 <= s2: print("s1 is subset of s2")

s2 = {2, 4, 3, 1, 5}
if s1 < s2: print("s1 is proper subset of s2")
if s1 > s2: print("s2 is proper subset of s1")
print("------------------------------------------------------------------------")
