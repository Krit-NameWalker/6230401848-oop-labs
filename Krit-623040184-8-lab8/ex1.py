class Rectangle:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def get_width(self):
        return self.__num1

    def get_height(self):
        return self.__num2

    def set_width(self, new_width):
        self.__num1 = new_width

    def set_height(self, new_height):
        self.__num2 = new_height

    def __str__(self):
        return f"This rectangle has width as {str(self.__num1)} height as " + str(self.__num2)

if __name__ == '__main__':
    rect1 = Rectangle(3, 4)
    print(rect1)
    print(f"Width is {rect1.get_width()}")
    rect1.set_height(5)
    print(f"Height is {rect1.get_height()}")