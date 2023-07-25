import os
os.system('cls')

# Modules
print('\033[1m' + "Modules" + '\033[0m')
print("")

import fibo_module as f
# from fibo_module import *
# from fibo_module import fib
# from fibo_module import fib, fib2
from math import pi as PI_VALUE

print(f.fib(5))
print(f.fib2(5))
print(PI_VALUE)

