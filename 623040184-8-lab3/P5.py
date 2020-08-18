num = int(input("Enter number to find the factorial: "))
i = num
fac = 1
while num > 0:
    fac = num * fac
    num -= 1
print("Factorial of %d is %d" % (i, fac))
