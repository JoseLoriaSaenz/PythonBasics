import os
os.system('cls')

# Conditionals
print('\033[1m' + "Conditionals" + '\033[0m')
print("")

# Single condition if
print('\033[1m' + "Single condition if" + '\033[0m')

if True:
    print("if True: -->", True)

if 1 == 1:
    print("if 1 == 1 -->", 1 == 1)

# Python falsy and trythy values
# Falsy
my_condition = ''
if my_condition:
    print("my_condition", my_condition, "# Falsy")

# Making truthy a false condition using not
if not (my_condition):
    print("not(my_condition) -->", not (my_condition),
          "mycondition:", "'" + my_condition + "'")

my_condition = 0
if my_condition:
    print("my_condition", my_condition, "# Falsy")

# Truthy
my_condition = 1 * 3
if my_condition:
    print("my_condition", my_condition, "# Truthty")

my_condition = "Hello"
if my_condition:
    print("my_condition", my_condition, "# Truthty")


# Multiple condition if
print("")
print('\033[1m' + "Multiple condition if" + '\033[0m')

if 10 > 5 and "a" == "a":
    print("10 > 5 and \"a\" == \"a\" --> True")

if 10 > 5 and "a" == "b":
    print("10 > 5 and \"a\" == \"b\" --> False")

# if / else
print("")
print('\033[1m' + "if / else" + '\033[0m')

my_condition = True
if my_condition:
    print("True my_condition -->", my_condition)
else:
    print("False my_condition -->", my_condition)

my_condition = False
if my_condition:
    print("True my_condition -->", my_condition)
else:
    print("False my_condition -->", my_condition)

my_condition = 10 > 5 and "a" != "a"
if my_condition:
    print("10 > 5 and \"a\" != \"a\" --> True", my_condition)
else:
    print("10 > 5 and \"a\" == \"a\" --> False", my_condition)

my_condition = 10 > 5 and "a" == "a"
if my_condition:
    print("10 > 5 and \"a\" == \"a\" --> True", my_condition)
else:
    print("10 > 5 and \"a\" == \"a\" --> False", my_condition)

# if / elif / else
print("")
print('\033[1m' + "if / elif / else" + '\033[0m')

letter = input("Type any letter: ")

if letter == "a":
    print("letter == \"a\" -->", letter == "a", "letter:", letter)
elif letter == "b":
    print("letter == \"b\" -->", letter == "b", "letter:",  letter)
else:
    print("niether a or b letter -->", letter)


# match
print("")
print('\033[1m' + "match" + '\033[0m')

number = int(input("Type a number between (1 and 3): "))

match number:
    case 1:
        print("You selected 1")
    case 2:
        print("You selected 2")
    case 3:
        print("You selected 3")
    case _:
        print(number, "is an invalid number")