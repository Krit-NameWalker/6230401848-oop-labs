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
            print("Unknow operator :(")
            return "unknow"
    except ZeroDivisionError:
        print("Cannot divide a number by 0")
        return "zero"

    while True:
        first_num = input("Enter the first number: ")
        if first_num.casefold() == "quit":
            quit()
        else:
            first_num = float(first_num)
            break
    while True:
        second_num = input("Enter the first number: ")
        if second_num.casefold() == "quit":
            quit()
        else:
            second_num = float(second_num)
            break
    while True:
        operator = input("Enter the operator: ")
        if operator.casefold() == "quit":
            quit()
        else:
            user_output = cal(first_num, second_num, operator)
            if user_output == "unknow":
                pass
            elif user_output == "zero":
                pass
            else:
                print(
                    "%.1f %s %.1f = %.1f"
                    % (first_num, operator, second_num, user_output)
                )
                break
