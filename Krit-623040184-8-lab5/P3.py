import math

def hypotenuse(a, b):
    try:
        return math.sqrt(math.pow(a,2)+math.pow(b,2))
    except TypeError:
        return None

print("hypotenuse ({}, {}) is {}".format(3.0, 4.0, hypotenuse(3.0, 4.0)))
print("hypotenuse ({}, {}) is {}".format("3", "4", hypotenuse("3", "4")))
print("hypotenuse ({}, {}) is {}".format(3, "4.0", hypotenuse(3, "4.0")))