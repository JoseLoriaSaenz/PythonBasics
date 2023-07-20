from msilib.schema import Property
import os
os.system('cls')

# Classes
print('\033[1m' + "Classes" + '\033[0m')
print("")

# Define simple class 
class Warehouse:
   name = 'Storage-01'
   region = 'West'

w1 = Warehouse()
print(f'Warehouse: name={w1.name} region={w1.region}')

# Class with constructor
class Warehouse:
    name = 'Storage-01'
    region = ''
   
    def __init__(self, region) -> None:
        self.region = region
        
w1 = Warehouse('East')
print(f'Warehouse: name={w1.name} region={w1.region}')

# Class with constructor with default value
class Warehouse:
    name = 'Storage-01'
    region = ''
   
    def __init__(self, region='East') -> None:
        self.region = region
        
w1 = Warehouse()
print(f'Warehouse: name={w1.name} region={w1.region}')

# Complex class 
class Warehouse:
    name = 'Storage-01'
    region = ''
    country = ''
   
    def __init__(self, region: str = 'East', country: str = '') -> None:
        self.region = region
        self.country = country
    
    def getWarehouseInfo(self) -> str:
        return f'Warehouse: {self.name}, Country: {self.country}, Region: {self.region}'
    
    def renameWarehouse(self, newName: str):
        self.name = newName
    
w1 = Warehouse(country='Spain', region='Andalucia')
print(w1.getWarehouseInfo())
w1.renameWarehouse('Raw-Material-Storage-05')
print(w1.getWarehouseInfo())

# Inheritance
print("")
print('\033[1m' + "Inheritance" + '\033[0m')

class Person:
    name: str
    surname: str
    age: str
    
class Employee(Person):    
    id: int
    department: str
   
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value

e = Employee()
e.name = "Joe"
e.surname = "Mad"
e.id = 125354
e.age = 35
e.department = "Accounting"
e.salary = 100
e._salary = 1000


print("")
print('Is an instance of Person and Employee')
print(isinstance(e, Person))
print(isinstance(e, Employee))
print("")
print('Is Employee a subclass of Person')
print(issubclass(Employee, Person))

# Multiple Inheritance
print("")
print('\033[1m' + "Multiple Inheritance" + '\033[0m')

class ClassA:
    id: int

class ClassB:
    name: str 
       
class ClassC(ClassA, ClassB):
    address: str
    
    def object(self):
        return {'Id':'{self.id}', 'Name':'{self.name}', 'Address': '{self.address}'}

c = ClassC()
c.id = 1
c.name = "John"
c.address = "Main Street"

o = c.object()
print(o)



        
    
