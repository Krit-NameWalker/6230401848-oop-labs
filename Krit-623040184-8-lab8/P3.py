class Pet:
    def __init__(self, name1):
        self.name1 = name1

    def show_info(self):
        print(f"I'm {self.name1}")

    def move(self):
        print("moving ...")

class Cat(Pet):
    def __init__(self, name1, name2, color1):
        self.name2 = name2
        self.color1 = color1
        super().__init__(name1)

    def show_info(self):
        super().show_info()
        print(f"and is {self.color1}")

    def move(self):
        print(f"belonging to {self.name2}")

class Dog(Pet):
    def __init__(self, name1, name2, color2):
        self.name2 = name2
        self.color2 = color2
        super().__init__(name1)

    def show_info(self):
        super().show_info()
        print(f"and is {self.color2}")

    def move(self):
        print(f"belonging to {self.name2}")
        print("Dog likes to run more than walk")

    def eat_cat(self, Cat):
        print(f"Dog {self.name1} eats cat {Cat.name1}")

if __name__ == '__main__':
    pet1 = Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdaeng", "Manee", "white")
    cat1.show_info()
    cat1.move()
    dog1 = Dog("Thongdum", "Mana", "black")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)