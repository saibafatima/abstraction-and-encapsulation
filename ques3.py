# Q3. What is abc module in python? Why is it used?


definition = "The abc module in Python stands for Abstract Base Classes. It is a module provided in the Python standard library that allows you to define abstract base classes. Abstract base classes serve as blueprints for other classes and provide a way to define common interfaces and behaviors."

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

# Instantiating objects
rectangle = Rectangle(4, 6)
circle = Circle(5)

# Calling methods
print("Area of rectangle:", rectangle.calculate_area())
print("Perimeter of rectangle:", rectangle.calculate_perimeter())

print("Area of circle:", circle.calculate_area())
print("Perimeter of circle:", circle.calculate_perimeter())
