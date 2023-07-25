import os
import sys
os.system('cls')

# Exceptions
print('\033[1m' + "Exceptions" + '\033[0m')
print("")

# Error hnadling
print('\033[1m' + "Type Exception" + '\033[0m')
try:
    print(5 + "5")
except Exception as e:
    print(f"Something wen't wrong! Error: {e.args}")

print("")
print('\033[1m' + "File reading exception" + '\033[0m')
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

print("")
print('\033[1m' + "Args reading exception" + '\033[0m')
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
    finally:
        print("Reading arg finished")
     
  
print("")
print('\033[1m' + "Zero Division exception" + '\033[0m')
 
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

print("")
print('\033[1m' + "Chaining and raising exceptions" + '\033[0m')
try:
    try:
        open("database.sqlite")
    except OSError:
        raise RuntimeError("unable to handle error")
except Exception as e:
    print(e)



