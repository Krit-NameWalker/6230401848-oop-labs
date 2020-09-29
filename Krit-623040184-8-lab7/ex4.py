class Numbers:
    def __init__(self, x, y):
        self.number1 = x
        self.number2 = y

    def add(self):
        sum = self.number1 + self.number2
        return f"{sum} \n {Numbers.display(self)}"

    def display(self):
        return f"{self.number1} and {self.number2}"

    @classmethod
    def display_factor(cls, number):
        cls.number = number
        if number % 2 == 0:
            return f"Factors of {number} is {number/2} and {number/2}"
        elif number % 2 == 1:
            return f"Factors of {number} is {(number / 2) - 0.5} and {(number / 2) + 0.5}"

    @staticmethod
    def is_valid_divisor(num):
        if num > 0:
            return f"{num} is a valid divisor"
        elif num <= 0:
            return f"{num} is not valid divisor"


if __name__ == '__main__':
    print(f"3 + 5 is {Numbers(3, 5).add()}")
    print(Numbers.display_factor(6))
    print(Numbers.display_factor(8))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))