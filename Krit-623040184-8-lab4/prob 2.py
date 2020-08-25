def cal(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            print("Please enter an operator")
            return "unknow"
    except ZeroDivisionError:
        print("float division by zero")
        return "zero"

while True:
    try:
        first_num = input("Enter the first operand: ")
        if first_num.casefold() == "quit":
            quit()
        else:
            first_num = float(first_num)
            break
    except ValueError:
        print("Please enter a number")

while True:
    try:
        second_num = input("Enter the second operand: ")
        if second_num.casefold() == "quit":
            quit()
        else:
            second_num = float(second_num)
            break
    except ValueError:
        print("Please enter a number")

while True:
    operator = input("Enter the an operator (+,-,*,/): ")
    if operator.casefold() == "quit":
        quit()
    else:
        user_output = cal(first_num, second_num, operator)
        if user_output == "unknow":
            pass
        elif user_output == "zero":
            pass
        else:
            print("Result", first_num, operator, second_num, "is", user_output)
            break
