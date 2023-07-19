import os
os.system('cls')

# Dictionaries
print('\033[1m' + "Dictionaries" + '\033[0m')

my_dict = dict()
print("my_dict = dict() -->", my_dict, "Type:", type(my_dict), "len:", len(my_dict))

my_other_dict = {}
print("my_other_dict = {{}} -->", my_other_dict, "Type:", type(my_other_dict), "len:", len(my_other_dict))

my_dict = {"name":"Joe", "surname":"Mad", "age":35}
print("my_dict = dict() -->", my_dict, "Type:", type(my_dict), "len:", len(my_dict))

my_dict["address"] = "Heredia"
print("my_dict[\"address\"] = \"Heredia\" -->", my_dict, "Type:", type(my_dict), "len:", len(my_dict))

my_dict["languages"] = {"Lang_1": "C#", "Lang_2": "Javascript", "Lang_3": "Visual Basic"}

print("dict(john=4139, guido=4127, jack=4098) -->", dict(john=4139, guido=4127, jack=4098))

print("dict([('john', 4139), ('guido', 4127), ('jack', 4098)]) -->", dict([('john', 4139), ('guido', 4127), ('jack', 4098)]))

my_new_dict = dict.fromkeys((range(1, 5)))
print("my_new_dict = dict.fromkeys((range(1, 5))) -->", my_new_dict)

my_new_dict_2 = dict.fromkeys((range(1, 5)), "")
print("my_new_dict_2 = dict.fromkeys((range(1, 5), \"\")) -->", my_new_dict_2)

# Retrieve Dictionary values
print("\n")
print('\033[1m' + "Retrieve Dictionary values" + '\033[0m')
print("my_dict[\"age\"] -->", my_dict["age"])
print("my_dict[\"languages\"] -->", my_dict["languages"])
print("my_dict[\"languages\"][\"Lang_2\"] -->", my_dict["languages"]["Lang_2"])

# Changing dictionary entry value
print("\n")
print('\033[1m' + "Changing dictionary entry value" + '\033[0m')

my_dict["languages"]["Lang_2"] = "Kotlin"
print("my_dict[\"languages\"][\"Lang_2\"] = \"Kotlin\" -->", my_dict["languages"]["Lang_2"])

# Adding dictionary entry value
print("\n")
print('\033[1m' + "Adding dictionary entry value" + '\033[0m')

my_dict["languages"]["Lang_4"] = "C++"
print("my_dict[\"languages\"][\"Lang_4\"] = \"C++\" -->", my_dict["languages"])

# Remove Dictionary entry
print("\n")
print('\033[1m' + "Remove Dictionary entry" + '\033[0m')

del my_dict["age"]
print("del my_dict[\"age\"] -->", my_dict)

# Comprehensions dictionary
print("\n")
print('\033[1m' + "Comprehensions dictionary" + '\033[0m')
print("{{x: x**3 for x in (2, 4, 6)}} -->", {x: x**3 for x in (2, 4, 6)})

# Locating item in dictionary
print("\n")
print('\033[1m' + "Locating item in dictionary" + '\033[0m')
print("\"name\" in my_dict -->", "name" in my_dict)

# Looks on the keys not the values
print("\"Kotlin\" in my_dict[\"languages\"] -->", "Kotlin" in my_dict["languages"])
print("\"Mad\" in my_dict.values() -->", "Mad" in my_dict.values())


# Dictionary methods
print("\n")
print('\033[1m' + "Dictionary methods" + '\033[0m')

print("my_dict.values() -->", my_dict.values())
print("my_dict.items() -->", my_dict.items())
print("my_dict.keys() -->", my_dict.keys())
print("my_dict.get(\"languages\")", my_dict.get("languages"))

# Loop Dictionary
print("\n")
print('\033[1m' + "Loop Dictionary" + '\033[0m')

for k, v in my_dict.items():
    print(k +":", v)
