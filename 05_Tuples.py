import os
os.system('cls')

# Tuples
print('\033[1m' + "Tuples" + '\033[0m')

my_tuple = tuple()
print("my_tuple = tuple()", "my_tuple:", my_tuple,
      "Type:", type(my_tuple), "len:", len(my_tuple))

my_new_tuple = 1, True, "Hello"
print("my_new_tuple = 1, True, \"Hello\"", "my_new_tuple:", my_new_tuple,
      "Type:", type(my_new_tuple), "len:", len(my_new_tuple))

# Tuples values
print("")
print('\033[1m' + "Assing values to tuples" + '\033[0m')

print("my_new_tuple[0] -->", my_new_tuple[0])
print("my_new_tuple[-1] -->", my_new_tuple[-1])
print("my_new_tuple[:] -->", my_new_tuple[:])
print("my_new_tuple[1:3] -->", my_new_tuple[1:3])
print("my_new_tuple[2] = False -->", '\033[91m', '\033[1m',
      "Tuples are inmutable. This Will Throw An Exception".upper(), '\033[0m')

# Nesting Tuples
tuple_letters = ("a", "b", "c", "d")
print("tuple_letters -->", tuple_letters)

tuple_numbers = (10, 20, 30, 40)
print("tuple_numbers -->", tuple_numbers)

nested_tuple = tuple_letters, tuple_numbers, (True, False, True)
print("nested_tuple", nested_tuple)

# Tuples methods
print("")
print('\033[1m' + "Tuples methods" + '\033[0m')

print("my_new_tuple.count(\"Hello\") --> ", my_new_tuple.count("Hello"))

# In Python True and 1 are equal
print("my_new_tuple.index(True) --> ", my_new_tuple.index(True))

my_tuple = my_tuple.__add__((True, "Bye", 52))
print("my_tuple -->", my_tuple)

my_tuple = my_tuple + my_new_tuple
print("my_tuple -->", my_tuple)

print("my_tuple.__len__() --> ", my_tuple.__len__())


# Destructuring Tuples
print("")
print('\033[1m' + "Destructuring Tuples" + '\033[0m')

a, b, c = my_new_tuple
print("a, b, c = my_new_tuple -->", "tuple:", my_new_tuple,
      "Destructured", "a =", a, "b =", b, "c =", c)

a, b = my_new_tuple[0:2]
print("a, b = my_new_tuple[0:2] -->", "tuple[0:2]:",
      my_new_tuple[0:2], "Destructured", "a =", a, "b =", b)

# Casting Tuple as List and viceversa
print("")
print('\033[1m' + "Casting Tuple as List" + '\033[0m')

my_tuple = list(my_tuple)
print("my_tuple = list(my_tuple) -->", my_tuple, "Type:", type(my_tuple))

my_tuple = tuple(my_tuple)
print("my_tuple = tuple(my_tuple) -->", my_tuple, "Type:", type(my_tuple))

# Comprehensions tuple
print("")
print('\033[1m' + "Comprehensions tuple" + '\033[0m')
print("[\"-\" + str(x*2) + \"-\" for x in my_tuple] --> ",
      ["-" + str(x*2) + "-" for x in my_tuple])
