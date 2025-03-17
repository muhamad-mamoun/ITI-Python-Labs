#! /bin/python3

# ================================================== #
# Summarize DataClass in Python

# 1- The costructor is created automatically.
# 2- The __repr__ method is created automatically.
# 3- The __eq__ method is created automatically.
# 4- The __str__ method is created automatically.

# from dataclasses import dataclass

# @dataclass
# class Person:
#     name: str = 'John'
#     age: int = 30
#     salary: float = 30000.0
#     date_of_birth: str = '01-01-1990'

# employee = Person('Mike', 25, 25000.0, '01-01-1995')
# print(employee)
# print(employee == Person('Mike', 25, 25000.0, '01-01-1995'))

# ================================================== #
# Method Resolution Order (MRO) in Multi Inheritance

# MRO is the how Python will search for the called function in the inheritence hierarcy.
# In linear hierarcy, it will search from down to up [from child to parent],
# But in case multiple inheritence, it will follow Depth-First algorithm,
# Which will search from down to up and from left to right.

# class GrandParent:
#     # pass
#     def display(self):
#         print('Hello from GrandParent')

# class FirstParent(GrandParent):
#     # pass
#     def display(self):
#         print('Hello from FirstParent')

# class SecondParent(GrandParent):
#     # pass
#     def display(self):
#         print('Hello from SecondParent')

# class Child(FirstParent, SecondParent):
#     pass
#     def display(self):
#         print('Hello from Child')

# childObject = Child()
# childObject.display() # Child --> FirstParent --> SecondParent --> GrandParent

# ================================================== #
# Dictionary Comprehension

# names = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']
# ages  = [24, 0, 14, -5, 16]
# employees_ages = { key : value for key, value in zip(names, ages) if value > 0}
# print(employees_ages)

# ================================================== #
# Composition

# class Engine:
#     def __init__(self, fuel_type, horse_power):
#         if fuel_type in [ 'Petrol', 'Diesel', 'Electric']:
#             self.__fuel_type = fuel_type
#         else: print('Invalid fuel type')
#         if horse_power > 0:
#             self.__horse_power = horse_power
#         else: print('Invalid fuel type')

#     @property
#     def fuel_type(self):
#         return self.__fuel_type
    
#     @fuel_type.setter
#     def fuel_type(self, fuel_type):
#         if fuel_type in [ 'Petrol', 'Diesel', 'Electric']:
#             self.__fuel_type = fuel_type
#         else: print('Invalid fuel type')

#     @property
#     def horse_power(self):
#         return self.__horse_power
    
#     @horse_power.setter
#     def horse_power(self, horse_power):
#         if horse_power > 0:
#             self.__horse_power = horse_power
#         else: print('Invalid horse power')
    
#     def display(self):
#         print(f'This is a {self.__horse_power} HP engine from {self.__fuel_type} type')

# class Car:
#     def __init__(self, engine, color):
#         self.__engine = engine
#         self.__color = color
    
#     def display(self):
#         print(f'This is a {self.__color} car with a {self.__engine.horse_power} HP engine from {self.__engine.fuel_type} type')

# myEngine = Engine('Petrol', 230)
# myCar = Car(myEngine, 'Black')
# myCar.display()

# ================================================== #
# Implement a Vector Class with Dunder Methods

# import math

# class Vector:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     def __str__(self):
#         return f'Vector({self.__x},{self.__y})'

#     def __repr__(self):
#         return f'Vector({self.__x},{self.__y})'
    
#     def __add__(self, other):
#         return Vector((self.__x + other.__x), (self.__y + other.__y))
    
#     def __sub__(self, other):
#         return Vector((self.__x - other.__x), (self.__y - other.__y))
    
#     def __mul__(self, value):
#         return Vector((self.__x * value), (self.__y * value))
    
#     def __eq__(self, other):
#         return (self.__x == other.__x) and (self.__y == other.__y)
    
#     def __len__(self):
#         return round(math.sqrt((self.__x ** 2) + (self.__y ** 2)))
    
#     def __getitem__(self, index):
#         if index == 0: return self.__x
#         elif index == 1: return self.__y

# vector1 = Vector(1, 6)
# vector2 = Vector(5, 4)
# print(str(vector1))
# print(repr(vector2))
# print(vector1 + vector2)
# print(vector1 - vector2)
# print(vector1 * 2)
# print(vector1 == vector2)
# print(vector1 == vector2 + Vector(-4, 2))
# print(len(vector1))
# print(vector1[0], vector1[1], vector1[2])
