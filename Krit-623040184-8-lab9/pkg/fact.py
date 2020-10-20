def fact(n):
    if n == 1:
        return n
    if n == 0:
        return 0
    else:
        return n * fact(n-1)

if __name__ == '__main__':
    import sys