import sys
import pdb


def divide(dividend, divisor):
    return dividend / divisor


#pdb.set_trace()
while True:
    dividend = int(input("Please enter the dividend:"))
    if dividend < 0:
        break
    divisor = int(input("Please enter the divisor:"))
    if divisor < 0:
        break
    try:
        answer = divide(dividend, divisor)
    except ZeroDivisionError:
        print("division by zero")
    else:
        print('The answer is: {}'.format(answer))
