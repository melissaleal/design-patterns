from abc import ABC, abstractmethod
from memory_profiler import profile

class ShapeType:
    def __init__(self, name, color, area):
        self.__name = name
        self.__color = color
        self.__area = area
    
    def describe(self):
        print(f"This is a {self.__name} with color {self.__color} and area {self.__area} cm².")
    
class ShapeFactory(ShapeType):
    _shape_types = {}
    
    @classmethod
    def getShapeType(cls, name, color, area):
        key = (name, color, area)
        if key not in cls._shape_types:
            cls._shape_types[key] = ShapeType(name, color, area)
        return cls._shape_types[key]
      
class Shape:
    def __init__(self, shapetype, width, height):
        self.__shapetype = shapetype
        self.__width = width
        self.__height = height
        
    def describe(self):
        self.__shapetype.describe()
        print(f"Dimensions: width = {self.__width} cm and height = {self.__height} cm\n")

pinkcircle = ShapeFactory.getShapeType("Circle", "Pink", 50)
redrectangle = ShapeFactory.getShapeType("Rectangle", "Red", 40)
bluesquare = ShapeFactory.getShapeType("Square", "Blue", 36)

@profile
def createShapesWithFlyweight():        
    for i in range(10**3):
        shapes = []
        shapes.append(Shape(pinkcircle, 7.98, 7.98))
        shapes.append(Shape(redrectangle, 8, 5))
        shapes.append(Shape(bluesquare, 6, 6))