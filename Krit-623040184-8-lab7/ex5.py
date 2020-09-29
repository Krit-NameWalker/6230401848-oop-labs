import math


class Circle:
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        sum1 = math.pi * self.radius ** 2
        return sum1

    def perimeter(self):
        sum2 = 2 * math.pi * self.radius
        return sum2

if __name__ == '__main__':
    print(f"The circle with radius {3} has the area as \n {Circle(3).area():.2f} and the perimeter as {Circle(3).perimeter():.2f}")
    print(f"The circle with radius {4} has the area as \n {Circle(4).area():.2f} and the perimeter as {Circle(4).perimeter():.2f}")