li = []
li2 = li  # Now li, li2 are pointing to the same list, so change in li2 will be reflected in li[0] also

li2.append([1,2,3])
print(li, li2)

li2 = li[0]
# Now li, li2 are not pointing to same list.
# but li2 and li[0] are pointing to same list, so change in li2 will be reflected in li[0] also.
li2[0] = 23
print(li, li2)

li2 = 999  # Here, li2 becomes completely separate from li. Any changes in li2 will not be seen in li.
print(li, li2)
print("------------------------------------------------------------------------")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ans = ListNode()
temp = ans

print(ans.val)
print(temp.val)
temp.next = ListNode(2)
print(ans.next.val)
print(temp.next.val)
temp.val = 3

temp = temp.next
temp.next = ListNode(5)
temp = temp.next
temp.next = ListNode(9)

while ans:
    print(ans.val, end=' ')
    ans = ans.next
print()
