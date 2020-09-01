def fac(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return num * fac(num-1)

if __name__ == "__main__":
    try:
        num = input("Enter an integer:")
        num = int(num)
        if num < 0:
            print("Please enter a positive integer. {} is not a positive integer".format(num))
        else:
            print("factorial {} is {}".format(num, fac(num)))
    except ValueError:
        num = str(num)
        print("Please enter a positive integer. invalid literal for int() with base 10: {} ".format(num))
