while True:
    num = int(input("Enter an integer: "))
    if num == 99:
        break
    if num % 2:
        continue
    print(num)
