from abc import *
import random


class Shape(ABC):
    @abstractmethod
    def __init__(self, colors):
        self.colors = colors

    @abstractmethod
    def draw(self, name):
        print(f"Drawing a {name} with", end ="")


class Circle(Shape):
    num_circles = 0

    def __init__(self, colors, radius):
        super().__init__(colors)
        type(self).num_circles += 1
        self.radius = radius

    def draw(self):
        super().draw("circle")
        print(f"radius {self.radius}")

    def set_radius(self, new_radius):
        self.radius = new_radius

    @classmethod
    def get_num_circles(cls):
        return cls.num_circles


class Rectangles(Shape):
    num_rectangles = 0

    def __init__(self, colors, width, height):
        super().__init__(colors)
        type(self).num_rectangles += 1
        self.width = width
        self.height = height

    def draw(self):
        super().draw("rectangle")
        print(f"width {self.width} height {self.height}")

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def print_area(self):
        area = self.width * self.height
        print(f"Rectangle width {self.width} height {self.height} has area as {area}")

    @classmethod
    def get_num_rectangles(cls):
        return cls.num_rectangles


if __name__ == '__main__':
    circles = []
    retangles = []
    NUM_OBJECTS = 3
    MIN = 10
    MAX = 20
    colors = ["green", "yellow", "blue", "red", "pink"]
    for i in range(NUM_OBJECTS):
        color = random.choice(colors)
        radius = random.randint(MIN, MAX)
        circles.append(Circle(color, radius))
        circles[i].draw()
    print(f"Num circles is {Circle.get_num_circles()}")

    for i in range(NUM_OBJECTS):
        color = random.choice(colors)
        width = random.randint(MIN, MAX)
        height = random.randint(MIN, MAX)
        retangles.append(Rectangles(color, width, height))
        retangles[i].draw()
        retangles[i].print_area()
    print(f"Num rectangles is {Rectangles.get_num_rectangles()}")