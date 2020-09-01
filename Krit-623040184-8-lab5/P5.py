def cal(a, b, op, format):
    try:
        if op == "+":
            solution = a + b
        elif op == "-":
            solution = a - b
        elif op == "*":
            solution = a * b
        elif op == "/":
            solution = a / b
        elif op == "(":
            return "advice"
        else:
            print("Unknown operation.")
            return "unknown"
    except ZeroDivisionError:
        print("Cannot divide a number by zero")
        print("We cannot perform your requested")
        return "zero"
    if format == "float":
        return solution
    elif format == "int":
        return int(round(solution))
    else:
        print("Unknown format")
        return "unknown"

while True:
    while True:
        try:
            first_num = input("Please enter the first operand ('q' to quit): ")
            if first_num.casefold() == "q":
                quit()
            else:
                first_num = float(first_num)
                break
        except ValueError:
            print("Please enter a number")
    while True:
        try:
            second_num = input("Please enter the second operand: ")
            if second_num.casefold() == "q":
                quit()
            else:
                second_num = float(second_num)
                break
        except ValueError:
            print("Please enter a number")

    while True:
        list_operation = ["+", "-", "*", "/"]
        list_format = ["float", "int"]
        operator = input("Enter the an operator ('+', '-', '*', '/'): ") or "+"
        if operator.casefold() == "q":
            quit()
        elif operator == "(":
            print("Operation must be ADD, SUB, MUL or DIV.")
            break
        elif operator in list_operation:
            format_input = input("Enter output format (float, int):") or "float"
            if format_input in list_format:
                user_output = cal(first_num, second_num, operator, format_input)
            if user_output == "unknown":
                pass
            elif user_output == "zero":
                break
            elif format_input == "int":
                print(
                    "%.1f %s %.1f = %.0f"
                    % (first_num, operator, second_num, user_output)
                )
                break
            else:
                print(
                    "%.1f %s %.1f = %.1f"
                    % (first_num, operator, second_num, user_output)
                )
                break
        else:
            print("Unknown operation.")
            pass