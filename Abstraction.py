# Abstraction example 1
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
# class Rectangle(Shape):
#     length = 5
#     breadth = 3
#     def calculate_area(self):
#         return self.length * self.breadth
#
# class Circle(Shape):
#     radius = 4
#     def calculate_area(self):
#         return 3.142 * (self.radius)**2
# rec = Rectangle() #object created for the class 'Rectangle'
# cir =Circle() #object created for the class 'Circle'
# print("Area of a rectangle:", rec.calculate_area())
# print("Area of a circle:", cir.calculate_area())

# Abstraction example 2
# from abc import ABC , abstractmethod
# class Shape(ABC):
#     def printx(self):
#         print("I am a normal method defined inside the abstract class 'Shape'")
#
#     @abstractmethod
#     def calculate_area(self):
#         pass
# class Rectangle(Shape):
#   length = 5
#   breadth = 3
#   def calculate_area(self):
#     return self.length * self.breadth
# rec = Rectangle()
# rec.printx()
# print("Area of a rectangle:", rec.calculate_area())

# IN-CLASS EXERCISE
from abc import ABC, abstractmethod
class  Bird(ABC):
    def defecate(self):
        print(" I can defecate")
    @abstractmethod
    def move(self):
        pass
class Hen(Bird):
    def move(self):
        return " what kind of move?"
class Ostrich(Bird):
    def move(self):
        return "Pls, what kind of move?"

hen = Hen()
hen.defecate()

