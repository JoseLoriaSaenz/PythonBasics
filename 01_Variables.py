import os
os.system('cls')

# Variables name convention lowercase and snake_case
MyVariable = "MyVariable invalid naming convention"
print("\n")
print(MyVariable)

my_string_variable = "my_string_variable valid convention"
print("\n")
print(my_string_variable)

my_int_variable = 5
print("\n")
print(my_int_variable)

my_bool_varaible = True
print("\n")
print(my_bool_varaible)

print("\n")
print(my_bool_varaible, my_int_variable, my_string_variable)

print("\n")
print(my_bool_varaible, my_int_variable, my_string_variable, str(1.67))

print("\n")
my_complex_var = {'name': 'Jose Loria'}
print(my_complex_var)

name, surname, alias, age, address = "Jose", "Loria", "JoeMad", 52, ["Heredia", "Heredia", "Santa Bárbara"]
print("\n")
print(name, surname, address, age, alias)

# Standard functions in python
my_temp_var = str(5) * 15
my_temp_var_length = len(my_temp_var)
print("\n")
print(my_temp_var, my_temp_var_length)

# Input info from console
print("\n")
print("Input console")
my_input = input("Type something: ")
print(my_input)

# Change var type by assignation
print("Change var by value assignation")
print("Python is not strongly type languge")
print("\n")
age = "Cincuenta y dos"
print("Age:", age)

# Variable typing will be overrride by assignation
my_typed_int_var: int = "52"
print("\n")
print(my_typed_int_var, type(my_typed_int_var))
