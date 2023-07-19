from os import system as sys
sys('cls')

# Lists
print('\033[1m' + "Lists" + '\033[0m')

my_list = list()
print("my_list = list(), type, len -->", my_list, type(my_list),  "len:", len(my_list))

my_list_2 = []
print("my_list = [], type, len -->", my_list_2, type(my_list),  "len:", len(my_list_2))

my_int_list = [1,2,3]
print("my_int_list = [1,2,3], len -->", my_int_list, "len:", my_int_list)

my_multitype_list = [1,True,"Hello"]
print("my_int_list = [1,True,\"Hello\"], len -->", my_multitype_list,  "len:", len(my_multitype_list))

# Assing values to list after creation
print("\n")
print('\033[1m' + "Assing values to list after creation" + '\033[0m')

my_list = [1971, 1972, 1973]
print("my_list = [1971, 1972, 1973] -->", my_list, "len:", len(my_list))

# Accessing and Adding elements
print("\n")
print('\033[1m' + "Accessing and Adding elements" + '\033[0m')
print("my_list[1] -->", my_list[1])

my_list[2] = 1975
print("my_list[2] = 1975 -->", my_list)

my_list.append(1980)
print("my_list.append(1980) -->", my_list)

my_list.append(1971 - 11)
print("my_list.append(1971 - 11) -->", my_list)

my_list.insert(2, 1973)
print("my_list.insert(2, 1973) -->", my_list)

print("my_list[1] -->", my_list[1])
print("my_list[:] -->", my_list[:])
print("my_list[0:3] -->", my_list[0:3])
print("my_list[1:4] -->", my_list[1:4])
print("my_list[-1] -->", my_list[-1])
print("my_list[] -->", '\033[91m', '\033[1m', "This Will Throw An Exception".upper(), '\033[0m')

# Lists methods
print("\n")
print('\033[1m' + "Lists methods" + '\033[0m')

print("my_list.count(1972) -->", my_list.count(1972))

my_org_list = my_list.copy()
print("my_org_list = my_list.copy() -->", my_org_list)

my_list.reverse()
print("my_list.reverse() -->", "orginal" , my_org_list, "reversed", my_list)

my_list.remove(1975)
print("my_list.remove(1975) -->", my_list)

del my_int_list[1]
print("del my_int_list[1] -->", my_int_list)

my_int_list.clear()
print("my_intList.clear()", my_int_list)

print("my_list + my_org_list -->", my_list + my_org_list)

print("(my_list + my_org_list).count(1980) -->", (my_list + my_org_list).count(1980))

# Destructuring Lists
print("\n")
print('\033[1m' + "Destructuring Lists" + '\033[0m')

a, b, c = my_multitype_list
print("a, b, c = my_multitype_list -->", "list:", my_multitype_list, "Destructured", a, b, c)

print("### Create a List assignning multiple variables ###".upper())
my_constructed_list = b, c, a
print("my_constructed_list = b, c, a -->", my_constructed_list)

# List as Stack
print("\n")
print('\033[1m' + "Lists as Stack" + '\033[0m')

my_list_as_stack = [1, 2, 3]
print("my_list_as_stack = [1, 2, 3] -->", my_list_as_stack)

my_list_as_stack.append(4)
print("PUSH: my_list_as_stack.append(4) -->", my_list_as_stack)

poped_last_value = my_list_as_stack.pop()
print("POP popped_value = my_list_as_stack.pop() -->", "Poped Value:", poped_last_value, "Stack:", my_list_as_stack)

poped_value_by_index = my_list_as_stack.pop(1)
print("POP poped_value_by_index = my_list_as_stack.pop(1) -->", "Poped Value by Index:", poped_value_by_index, "Stack:", my_list_as_stack)

# List as Queue
print("\n")
print('\033[1m' + "Lists as Queue" + '\033[0m')

my_list_as_queue = [1, 2, 3]
print("my_list_as_queue = [1, 2, 3] -->", my_list_as_queue)

# Need to import deque for collections
from collections import deque
my_list_as_queue = deque(my_list_as_queue)

print("NEED: from collections import deque")
print("my_list_as_queue = deque(my_list_as_queue) -->", my_list_as_queue)

print("\n")
print("### Queue element at end ###")
my_list_as_queue.append(4)
print("my_list_as_queue.append(4) -->", my_list_as_queue)

print("### Queue element at front ###")
my_list_as_queue.appendleft(0)
print("my_list_as_queue.appendleft(0) -->", my_list_as_queue)

print("### Dequeue element at end ###")
my_list_as_queue.pop()
print("my_list_as_queue.pop() -->", my_list_as_queue)

print("### Dequeue element at front ###")
my_list_as_queue.popleft()
print("my_list_as_queue.appendleft() -->", my_list_as_queue)

# List Comprehensions
print("\n")
print('\033[1m' + "Lists Comprehensions" + '\033[0m')

my_special_list = [x**2 for x in range(5)]
print("my_special_list = [x**2 for x in range(5)] -->", my_special_list)

my_special_list_2 = ["a"*x for x in range(10)]
print("my_special_list = [x**2 for x in range(10)] -->", my_special_list_2)

linear_vector= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
print("linear_vector= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,] -->", linear_vector)

even_square_vector = [x**2 for x in linear_vector if x % 2 != 0 ]
print("even_square_vector = [x**2 for x in linear_vector if x % 2 != 0 ] -->", even_square_vector)