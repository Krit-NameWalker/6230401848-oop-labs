import sys
from functools import reduce


num_input = int(sys.argv[1])
num = range(1, num_input + 1)
list_num = list(num)
print(f"With the argument as {num_input}, yhe input list is {list_num}")

def fac(num_input):
    num_fac = range(1, num_input + 1)
    fac = reduce(lambda x, y: x * y, num_fac)
    return fac

factorial = map(lambda x: fac(x), num)
print(f"The factorial number are {list(factorial)}")