import math

class Shape:
    def __init__(self, name: str, color: str):
        self.name: str = name
        self.color: str = color
        
    def describe(self) -> None:
        print(f"{self.__class__.__name__}({self.color})")
        
        
class Circle(Shape):
    def __init__(self, name: str, color: str, radius: float):
        super().__init__(name, color)
        self.radius: float = radius
        
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    
class Rectangle(Shape):
    def __init__(self, name: str, color: str, length: float, width: float):
        super().__init__(name, color)
        self.length: float = length
        self.width: float = width
        
    def area(self) -> float:
        return self.length * self.width
    
    
class Triangle(Shape):
    def __init__(self, name: str, color: str, base: float, height: float):
        super().__init__(name, color)
        self.base: float = base
        self.height: float = height
        
    def area(self):
        return self.base * self.height / 2
    
    
shapes = [  Circle("circle", "red", 3),
            Rectangle("rectangle", "green", 4, 5),
            Triangle("triangle", "blue", 6, 4)]

for shape in shapes:
    shape.describe()
    print(shape.area())