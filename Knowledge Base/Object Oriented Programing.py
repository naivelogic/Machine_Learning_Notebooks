# Objecrt Orirented Programing (OOP)
## Statistics and Machine Learning in Python

"""
Principles:
* Encapsulate data (attributes) and code (methods) into objects.
* Class = template or blueprint that acn be used to create objects.
* An object is a specific instance of a class
* Inheritance: OOP allows classes to inherit commonly used state and hehaviour from other classes. Reduce code deuplication
* Polymorphism: (usually obtained through polymorphism) calling code is agnostic as to whether an object belongs to a parent class or one of its decendants (abstraction, modularity). The same method called on 2 objects of 2 different classes will behave differently
"""

import math

class Shape2D:
    def area(self): 
        raise NotImplementedError()

# __init__ is a special method called the constructor

# Inheritance + Encapsulation
class Square(Shape2D):
    def __init__(self, width):
        self.width = width
    
    def area(self):
        return self.width ** 2

class Disk(Shape2D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

shapes = [Square(2), Disk(3)]

# Polymorphism
print([s.area() for s in shapes])
# [4, 28.274333882308138]

s = Shape2D()
try: 
    s.area()
except NotImplementedError as e:
    print("NotImplemented Error")
