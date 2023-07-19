import os
os.system('cls')

# Sets
print('\033[1m' + "Sets" + '\033[0m')

my_set = set()
print("my_set = set()", "my_set:", my_set, "Type:", type(my_set), "len:", len(my_set))

my_empty_set = {} # This initially will be created as Dict
print("my_empty_set = \{\} -->", "my_empty_set:", my_empty_set, "Type:", '\033[1m', type(my_empty_set), '\033[0m', "len:", len(my_empty_set))

my_empty_set = {1980, 1979, 1979, 1981, 1982}
print("my_empty_set = {1980, 1979, 1979, 1981, 1982} -->", "my_empty_set:", my_empty_set, "Type:", '\033[1m', type(my_empty_set), '\033[0m', "len:", len(my_empty_set))

# Sets are unique values
my_fruits_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("my_fruits_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} -->", "my_fruits_set:", my_fruits_set, "Type:", type(my_fruits_set), "len:", len(my_fruits_set))

print("my_fruits_set[0] --> ", '\033[91m', '\033[1m', '''Sets are unordered so can't access value by inde. 
                        This Will Throw An Exception'''.upper(), '\033[0m')

# Add element to set
print("\n")
print('\033[1m' + "Add element to set" + '\033[0m')
my_fruits_set.add("mango")
print("my_fruits_set.add(\"mango\") -->", my_fruits_set)

# Concatenate sets
print("\n")
print('\033[1m' + "Concatenate sets" + '\033[0m')
print("my_fruits_set.union({\"apple\", \"grape\", \"lemon\"}) -->", my_fruits_set.union({"apple", "grape", "lemon"}))
print("my_empty_set.union(my_fruits_set) -->", my_empty_set.union(my_fruits_set))

# Set difference
print("\n")
print('\033[1m' + "Set diference" + '\033[0m')

car_brands = {"Mitsubishi", "Honda", "BMW", "Mercedes", "Toyota", "Mitsubishi", "BMW" }
bike_brands = {"BMW", "Honda", "Harley Davidson", "Honda"}

print("car_brands -->", car_brands)
print("bike_brands -->", bike_brands)
print("\n")
print("car_brands.difference(bike_brands) -->", car_brands.difference(bike_brands))

# Locating item in set
print("\n")
print('\033[1m' + "Locating item in set" + '\033[0m')
print("\"pear\" in my_fruits_set -->", "pear" in my_fruits_set)
print("\"Mango\" in my_fruits_set -->", "Mango" in my_fruits_set)

# Removing item from set
print("\n")
print('\033[1m' + "Removing item from set" + '\033[0m')
my_fruits_set.remove("mango")
print("my_fruits_set.remove(\"mango\") -->", my_fruits_set)

# Pop item from set
print("\n")
print('\033[1m' + "Pop item from set" + '\033[0m')
print("my_fruits_set.pop() -->", my_fruits_set.pop())

# Removing all items from set
print("\n")
print('\033[1m' + "Removing all items from set" + '\033[0m')
my_fruits_set.clear()
print("my_fruits_set.clear() -->", my_fruits_set)

# Removing all items from set
print("\n")
print('\033[1m' + "Removing all items from set" + '\033[0m')
print("del my_fruits_set -->", '\033[91m', '\033[1m', "Will destroy my_fruits_set variable".upper(), '\033[0m')


# Comprehensions set
print("\n")
print('\033[1m' + "Comprehensions set" + '\033[0m')
print("{x for x in \'abracadabra\' if x not in \'abc\'} -->", {x for x in 'abracadabra' if x not in 'abc'})