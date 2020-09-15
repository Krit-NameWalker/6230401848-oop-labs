user = input("Enter a filename : ")

try:
    with open(user, encoding='utf8') as f:
        for line in f:
            print(line, end=" ")
except TypeError:
    exit()
