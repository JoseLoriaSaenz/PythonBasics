import os
os.system('cls')

# Loops
print('\033[1m' + "Loops" + '\033[0m')
print("")

# For Loop
print('\033[1m' + "For Loop" + '\033[0m')

fruits = ["apple", "orange", "pear", "banana"]
print("fruits = [\"apple\", \"orange\", \"pear\", \"banana\"]")
print("for fruit in fruits --> print(fruit)")
for fruit in fruits:
    print(fruit, end=', ')

print("")
integers = (1, 2, 3, 4, 5)
print("integers = (1,2,3,4,5)")
print("for integer in integers --> print(integer**2)")
for integer in integers:
    print(integer**2, end=', ')


print("")
print("for Loop with range")
print("for a in range(1,4) --> print(a)")
for a in range(1, 4):
    print(a, end=", ")

print("")
users = {'John': 'active', 'Mary': 'inactive', 'Tom': 'active'}
print("users = {'John': 'active', 'Mary': 'inactive', 'Tom': 'active'}")
for user, status in users.items():
    print(f"{user} is {status.upper()}", end=' -- ')

# For / Else / Break
print("")
print('\033[1m' + "for / else / break" + '\033[0m')
print(''' 
      for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
              print(n, 'equals', x, '*', n//x)
              break
      else:
            print(n, 'is a prime number')
      ''')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


# For / Continue
print("")
print("For / Continue")
print("Discard inactive users")
print("users = {'John': 'active', 'Mary': 'inactive', 'Tom': 'active'}")
for user, status in users.items():
    if status == "inactive":
        continue
    print(f"{user} is {status.upper()}", end=' -- ')


# While Loop
print("")
print('\033[1m' + "While Loop" + '\033[0m')

value = 1
print("value = 1")
print("while value <= 3")
while value <= 3:
    print("value -->", value, end=', ')
    value += 1

# While / Else
print("")
print('\033[1m' + "while / else" + '\033[0m')

value = 10
print("value = 10")
print("while value <= 15")
while value <= 15:
    print(value, end=", ")
    value += 1
else:
    print("\nfinal value -->", value, end='\n')
