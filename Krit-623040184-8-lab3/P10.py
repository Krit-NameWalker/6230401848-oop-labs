num = 0
sum = 0

while True:
    inte = int(input("Enter an integer: "))
    if inte > 0:
        sum += inte
        num += 1
    if inte < 0 and num == 0:
        print("You haven't entered a positive number")
        break
    if inte < 0 and num != 0:
        average = sum / num
        print("average is %d" % average)
        break
