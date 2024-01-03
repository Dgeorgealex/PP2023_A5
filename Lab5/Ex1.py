import math


class Shape:
    def compute_perimeter(self): pass
    def compute_area(self): pass

    def print_info(self):
        class_name = self.__class__.__name__
        print(f"{class_name}, perimeter={self.compute_perimeter()}, area={self.compute_area()}")


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def compute_perimeter(self):
        return 2 * math.pi * self.r

    def compute_area(self):
        return math.pi * self.r ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def compute_perimeter(self):
        return 2 * (self.length + self.width)

    def compute_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def compute_perimeter(self):
        return self.sideA + self.sideB + self.sideC

    def compute_area(self):
        p = self.compute_perimeter() / 2
        return (p * (p - self.sideA) * (p - self.sideB) * (p - self.sideC))**0.5


if __name__ == "__main__":
    circle = Circle(4)
    circle.print_info()

    rectangle = Rectangle(3, 4)
    rectangle.print_info()

    triangle = Triangle(3, 4, 5)
    triangle.print_info()
