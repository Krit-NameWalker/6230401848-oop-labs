import sys
from functools import reduce

num = int(sys.argv[1])

result = reduce(lambda x, y: x * y, range(1, num + 1))
print(f"Factorial of ({num}) is", result)