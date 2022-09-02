class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class my_linked_list:
    def __init__(self):
        self.head = None
    
    def print(self):
        temp = self.head
        print("Linked List: ", end='')
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def append(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node(data)

    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.data != data:
                temp = temp.next
            temp.next = temp.next.next
    
    def __len__(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverse(self):
        temp = self.head
        prev = None
        while temp:
            fwd = temp.next
            temp.next = prev
            prev = temp
            temp = fwd
        self.head = prev

    # # Using stack        
    # def reverse(self):
    #     temp = self.head
    #     stack = []
    #     while temp:
    #         stack.append(temp.data)
    #         temp = temp.next
    #     self.head = None
    #     for x in reversed(stack):
    #         self.append(x)

    def deletelist(self):
        # In python garbage collection happens therefore, just self.head = None would also delete the link list # as far as I know
        self.head = None


ll = my_linked_list()
print(ll)

# Append item at the end of the linked list #
ll.append(1)
ll.append(2)
ll.append(1)
ll.append(4)
ll.append(3)
ll.append(5)
ll.print()
print("------------------------------------------------------------------------")

# length #
print("Length of linked list:", ll.__len__())
print("Length of linked list:", len(ll))
print("------------------------------------------------------------------------")


# Remove #
ll.remove(1)
ll.print()
ll.remove(2)
ll.print()
print("------------------------------------------------------------------------")

#
ll.reverse()
ll.print()
print("------------------------------------------------------------------------")

ll.deletelist()
ll.print()
