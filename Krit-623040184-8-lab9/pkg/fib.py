def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fib(n - 2) + fib(n -1)

if __name__ == '__main__':
    import sys