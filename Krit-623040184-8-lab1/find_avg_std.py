import math
import random
print("1111111111 PB 1111111111")
print("Random 1 t0 10")
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
print("Random integer : ", "[", n1, ",", n2, "]")

Avg = (n1 + n2) / 2
Std = math.sqrt(((n1 - Avg)*(n1 - Avg)+(n2 - Avg)*(n2 - Avg))/ 2)
print("The average of ", n1, "and", n2, "is", Avg)
print("The stadard deviation of", n1, "and", n2, "is", Std)

