from queue import PriorityQueue


pq_of_strings = PriorityQueue()
for s in ["one", "two", "three"]:
    pq_of_strings.put(s)
while not pq_of_strings.empty():
    print(pq_of_strings.get())
print("pq_of_strings.empty():", pq_of_strings.empty())
print("--------------------------------------------------")

pq_of_numbers = PriorityQueue()
for x in [2, 1, 3]:
    pq_of_numbers.put(x)
print("current size of pq_of_numbers:", pq_of_numbers.qsize())

while not pq_of_numbers.empty():
    print(pq_of_numbers.get())
    print("current size of pq_of_numbers:", pq_of_numbers.qsize())

print("pq_of_numbers.empty():", pq_of_numbers.empty())
print("--------------------------------------------------")

pq_of_items = PriorityQueue()

pq_of_items.put((2, 'asdfg'))
pq_of_items.put((3, 'zxcvb', 1))
pq_of_items.put((1, 'qwert'))
pq_of_items.put((1, 'abcde', 5))
pq_of_items.put((1, 'abcde', 3))
pq_of_items.get_nowait

while not pq_of_items.empty():
    print(pq_of_items.get())
print("pq_of_items.empty():", pq_of_items.empty())
print("--------------------------------------------------")


pq_of_finite_size = PriorityQueue(maxsize=3)

pq_of_finite_size.put(35)
pq_of_finite_size.put(21)
pq_of_finite_size.put(16)
# pq_of_finite_size.put(99) # This will block, and the program will pause here
# pq_of_finite_size.put_nowait(999) # This will raise a queue.Full exception
# pq_of_finite_size.put(9, block=False) # This will raise a queue.Full exception

while not pq_of_finite_size.empty():
    print(pq_of_finite_size.get())
