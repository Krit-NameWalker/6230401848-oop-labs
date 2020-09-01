import math

def print_cal(a,b):
    print("{}^2 + {}^2 is {}".format(a,b, math.sqrt(math.pow(a,2) + math.pow(b,2))))

print_cal(3.0,4.0)
print_cal(3,4)
print_cal(3.0,4)