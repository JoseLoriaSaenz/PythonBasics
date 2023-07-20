import os
import gc
os.system('cls')

# Functions
print('\033[1m' + "Functions" + '\033[0m')
print("")

# Define a function no return
print("def my_function():")
def my_function():
    print("\nmy function was executed")
    
# Call a function not return
my_function()

# Define a function with return
print("def my_return_function():")
def my_return_function():
    return "\nmy return function was executed"
    
# Call a function with return
print(my_return_function())

# Function with parameters
def my_param_function (text: str):
    print(text)
    
my_param_function("Hello World!")

# Default params function
print("")
print('\033[1m' + "Default params function" + '\033[0m')

def default_value_params_func(text: str = "Default Value"):
    print(text)


print("default_value_params_func() --> Default Value")
default_value_params_func()

print("default_value_params_func(\"No default value\") --> No default value")
default_value_params_func("No default value")

# Default params value considerations
print("")
print('\033[1m' + "Default params value considerations" + '\033[0m')

print('\033[1m' + "Default params value is evaluated only once" + '\033[0m')
print('''
      This following code: 
      
      i = 5
      def f(arg=i):
        print(arg)
      i = 6
      f() --> will print 5
      ''' )

i = 5
print("i Initial value -->", i)
def f(arg=i):
    print("i Function Default Value -->",arg)
i = 6
print("i Reassign value to 6 -->", i)
f()

# If default is mutable such as list, dictionaty or class instance will keep previous values
print("")
print('\033[1m' + "If default is mutable such as list, dictionaty or class instance will keep previous values" + '\033[0m')

print('''
      This following code: 
      
      def f(a, L=[]):
        L.append(a)
        return L

      print(f(1)) --> [1]
      print(f(2)) --> [1,2]
      print(f(3)) --> [1,2,3]         
      ''' )

def f(a, L=[]):
    L.append(a)
    return L

print("f(1) -->", f(1))
print("f(2) -->", f(2))
print("f(3) -->", f(3))

# Avoid the previous behavior with if L is None or len(L) == 0
print("")
print('\033[1m' + "If default is mutable such as list, dictionaty or class instance will keep previous values" + '\033[0m')

print('''
      This following code: 
      
      def f(a, L=None):
        if L is None:
          L=[]
        L.append(a)
        return L

      print(f(1)) --> [1]
      print(f(2)) --> [2]
      print(f(3)) --> [3]         
      ''' )

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print("f(1) -->", f(1))
print("f(2) -->", f(2))
print("f(3) -->", f(3))

# Standard arguments
print("")
print('\033[1m' + "Standard arguments" + '\033[0m')
   
print('''
      This following code: 

      def standard_arg(arg):
        print(arg)
      
      standard_arg(1) --> 1 
      standard_arg(2) --> 2
      ''')

def standard_arg(arg):
    print(arg)
    
print('standard_arg(1) -->', end = ' ')
standard_arg(1)
print('standard_arg(2) -->', end = ' ')
standard_arg(2)

# Positional Only arguments
print("")
print('\033[1m' + "Positional Only arguments" + '\033[0m')
   
print('''
      This following code: 

      def pos_only_arg(arg, /):
        print(arg)
      
      standard_arg(1) --> 1
      standard_arg(arg=2) --> this will throw an exception
      ''')

def pos_only_arg(arg, /):
    print(arg)

print('standard_arg(1) -->', end = ' ')
pos_only_arg(1)
print('standard_arg(arg=2) --> exception ', end = '\n')

# Keyword Only arguments
print("")
print('\033[1m' + "Keyword Only arguments" + '\033[0m')
   
print('''
      This following code: 

      def kwd_only_arg(*, arg):
        print(arg)
      
      standard_arg(1) --> this will throw an exception
      standard_arg(arg=2) --> 2
      ''')

def kwd_only_arg(*, arg):
    print(arg)

print('standard_arg(1) --> exception')
print('standard_arg(arg=2) -->', end = ' ')
kwd_only_arg(arg=2)

# Combined arguments
print("")
print('\033[1m' + "Combined arguments" + '\033[0m')
   
print('''
      This following code: 

      def combined_args(pos_only, /, standard, *, kwd_only):
        print(pos_only, standard, kwd_only)
      
      combined_args(1, 2, kwd_only=3) --> 1 2 3
      combined_args(1, standard=2, kwd_only=3) --> 1 2 3
      combined_example(1, 2, 3) --> exception missing keyword parameter kwd_only
      combined_example(pos_only=1, standard=2, kwd_only=3) --> exception argument passed as keyword argument pos_only
      ''')

def combined_args(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

print('combined_args(1, 2, kwd_only=3) -->', end = ' ')
combined_args(1, 2, kwd_only=3)
print('combined_args(1, standard=2, kwd_only=3) -->', end = ' ')
combined_args(1, standard=2, kwd_only=3)
print('combined_example(1, 2, 3) --> exception missing keyword parameter kwd_only')
print('combined_example(pos_only=1, standard=2, kwd_only=3) --> exception argument passed as keyword argument pos_only')

# Argument type precedence
print("")
print('\033[1m' + "Argument type precedence" + '\033[0m')

print('\033[1m' + "positional, *args [Tuple], **keywords [Dictionary]" + '\033[0m')
print("def order_hamburguer(type: str, with_chesse: bool, *ingredients, **hold_ingredients)")
def order_hamburguer(type: str, with_chesse: bool, *ingredients, **hold_ingredients):
    print('\n')
    print('Burger Order #9999-99')
    print(f"You ordered: {type} burger ", end = '')
    if with_chesse:
        print('with chesse', end = '\n')
    else:
        print("with", end = '\n')
        
    print(f'{"-"*5}INGREDIENTS LIST{"-"*5}')
    i = 0
    for ingridient in ingredients:
        i += 1
        print(f"Ingridient {i}: {ingridient}")
        
    print(f'{"-"*5}HOLD INGREDIENTS{"-"*5}')
    for hold in hold_ingredients:
        print("Hold ", end = '')
        print(f"{hold}:", hold_ingredients[hold], end = "\n")
    print(f'{"-"*7}END OF ORDER{"-"*7}')


print('order_hamburguer("Double Decker", True, "Tomato", "Lettuce", "Onion", "Kale", Ketchup="no", Mustard="yes", Pickles="yes" )')
order_hamburguer("Double Decker", True, "Tomato", "Lettuce", "Onion", "Kale", Ketchup="no", Mustard="yes", Pickles="yes", Mayonnaise="no")

# Recursive function
print("")
print('\033[1m' + "Recursive function" + '\033[0m')

def factorial(number: int) -> int:
    if number < 0:
        return "number must be positive"
    elif number >= 2167:
        return "Out of Memory error"
    elif number >= os.sys.getrecursionlimit():
        os.sys.setrecursionlimit(number*2)
        os.sys.set_int_max_str_digits(number**2)
        
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

number = int(input("Type a integer: "))

result = factorial(number)
print(f"factorial({number}) -->", result)


