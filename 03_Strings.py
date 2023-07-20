import os
import datetime
os.system('cls')

# Strings
my_string = "This is an string"
my_other_string = "This is other string"

print('\033[1m' + "Strings" + '\033[0m')
print(my_string + " " + my_other_string)

print("")
print('\033[1m' + "Escaped Strings" + '\033[0m')

# New Line
print("String1 \\n new line String2 -->",my_string +  + my_other_string)

# Tab
print("\\t tab Str -->", "\t" + my_other_string)


# String Format
print("")
print('\033[1m' + "String Format" + '\033[0m')

name, surname, dob, age = "Jose", "Loria", "29/10/1971", 52
my_formated_text = 'My name is %s %s, DOB: %s, my age is %d' % (name, surname, dob, age)
print("using %s, %d and % -->", my_formated_text)
print("using .format() -->", "My name is {0} {1}, DOB {2}".format(name, surname, dob))

person_var = {"Name":"Jose Loria", "Age": 52}
print("using format(varname=value) -->", "My Name is {fname}, I'm {age} y/o".format(fname=person_var['Name'], age=person_var['Age']))
print("using **object -->", "My name is {Name}. I'm {Age} y/o".format(**person_var))

print("")
print('\033[1m' + "Simplified String Format" + '\033[0m')
print("using F or f prefix", F"My name is {name} {surname}. I was born on {dob}", f"Person var Age property: {person_var['Age']}")

print("")
print('\033[93m' + '\033[1m' + "Date Formatting" + '\033[0m')
my_dob_date_var = datetime.date(1971,10,29)
print("format date day/month/year", my_dob_date_var.strftime("%d/%m/%Y"))

# Char distructoring
my_string_var = "Python"
a,b,c,d,e,f = my_string_var

print("")
print('\033[1m' + "Destructuring String" + '\033[0m')

print(f)
print(e)
print(d)
print(c)
print(b)
print(a)

# String Array
print("")
print('\033[1m' + "String Array" + '\033[0m')
print("Python[1:3] -->", my_string_var[1:3])
print("Python[3:] -->", my_string_var[3:])
print("Python[:3] -->", my_string_var[:3])
print("Python[3] -->", my_string_var[3])
print("Python[-2] -->", my_string_var[-2])
print("Python[::-1] -->", my_string_var[::-1])

my_repeated_str = "123" * 4
str_len = len(my_repeated_str)
step = 3
start_at = 0

print("String[start_at:string_len:step] -->", my_repeated_str[start_at:str_len:step])



# String Methods
print("")
print('\033[1m' + "String Methods" + '\033[0m')

print("Python.lower() -->", my_string_var.lower())
print("Python.upper() -->", my_string_var.upper())
print("Python.find('on') -->", my_string_var.find('on'))
print("Python.index('yt') -->", my_string_var.index('yt'))
print("123123123123.count(3) -->", "123123123123 has", my_repeated_str.count("3"), 'threes')

