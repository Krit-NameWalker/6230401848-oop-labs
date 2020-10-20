from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        pass

    @abstractmethod
    def move(self):
        pass


class Snake(Animal):
    def __init__(self):
        super().__init__("snake")

    def move(self):
        print(f"I can crawl")


class Dog(Animal):
    def __init__(self):
        super().__init__("dog")

    def move(self):
        print(f"I can bark")


class Human(Animal):
    def __init__(self):
        super().__init__("human")

    def move(self):
        print(f"I can walk and run")


if __name__ == '__main__':
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()