from abc import ABC, abstractmethod
from memory_profiler import profile
import matplotlib.pyplot as plt

class Shape(ABC):
    @abstractmethod
    def describe(self):
        pass
    
class Circle(Shape):
    def __init__(self, color, area, radius):
        self.__color = color
        self.__area = area
        self.__radius = radius
        
    def describe(self):
        print(f"This is a circle with color {self.__color}, area {self.__area} cm² and radius {self.__radius} cm.")
    
class Rectangle(Shape):
    def __init__(self, color, area, width, height):
        self.__color = color
        self.__area = area
        self.__width = width
        self.__height = height
        
    def describe(self):
        print(f"This is a rectangle with color {self.__color}, area {self.__area} cm², width {self.__width} cm and height {self.__height} cm.")
    
class Square(Shape):
    def __init__(self, color, area, edge):
        self.__color = color
        self.__area = area
        self.__edge = edge
        
    def describe(self):
        print(f"This is a square with color {self.__color}, area {self.__area} cm² e edge {self.__edge} cm.")
    
@profile
def createShapesWithoutFlyweight():
    circles = []
    rectangles = []
    squares = []
    for i in range(10**3):
        circle = Circle('red', 10, 5)
        rectangle = Rectangle("blue", 20, 5, 4)
        square = Square("green", 25, 5)
        circles.append(circle)
        rectangles.append(rectangle)
        squares.append(square)