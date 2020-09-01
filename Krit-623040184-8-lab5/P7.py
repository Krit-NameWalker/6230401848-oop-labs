ADD, SUB, MUL, DIV = range(4)

def flexible_calculator(operation=ADD, output_format=float, *args):
    try:
        result = args[0]
    except IndexError:
        print("At least one number must be entered")
    else:
        for arg in args[1:]:
            if operation == ADD:
                result += arg
            elif operation == SUB:
                result -= arg
            elif operation == MUL:
                result *= arg
            elif operation == DIV:
                result /= arg
            else:
                raise ValueError("Operation must be ADD, SUB, MUL or DIV.")
            if output_format == float:
                result = float(result)
            elif output_format == int:
                result = round(result)
            else:
                raise ValueError("Format must be float or int")
        return result

def calculator(a, b, operation=ADD, output_format=float):
    if operation == ADD:
        result = a + b
    elif operation == SUB:
        result = a - b
    elif operation == MUL:
        result = a * b
    elif operation == DIV:
        result = a / b
    else:
        raise ValueError("Operation must be ADD, SUB, MUL or DIV.")
    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = round(result)
    else:
        raise ValueError("Format must be float or int")
    return result

answer = calculator(2, 3)
print("calculator (2, 3) = {}".format(answer))
answer = calculator(2, 3, MUL)
print("calculator (2, 3, MUL) = {}".format(answer))
answer = calculator(2, 3, SUB, int)
print("calculator (2, 3, SUB, int) = {}".format(answer))
answer = flexible_calculator(ADD, int, 1, 2, 3)
print("flexible_calculator(ADD, int, 1, 2, 3) = {}".format(answer))
answer = flexible_calculator(ADD, int, 1, 2, 3, 4)
print("flexible_calculator(ADD, int, 1, 2, 3, 4) = {}".format(answer))
answer = flexible_calculator(SUB, float, 1, 2, 3, 4, 5)
print("flexible_calculator(SUB, float, 1, 2, 3, 4, 5) = {}".format(answer))
answer = flexible_calculator(ADD, int, 1)
print("flexible_calculator(ADD, int, 1) = {}".format(answer))
answer = flexible_calculator(MUL, int, 2, 3, 4)
print("flexible_calculator(MUL, int, 2, ,3 ,4) = {}".format(answer))
answer = flexible_calculator(DIV, float, 10, 5, 2)
print("flexible_calculator(DIV, float, 10, 5, 2) = {}".format(answer))
answer = flexible_calculator(DIV, float)
print("flexible_calculator(DIV, float) = {}".format(answer))