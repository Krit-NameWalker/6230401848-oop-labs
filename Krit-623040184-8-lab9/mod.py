
s = "Strive not to be a success, but rather to be of value. -Albert Einstein"
a = [100, 200, 300]


def foo(arg):
    print(f'ar  g = {arg}')


class Foo:
    pass


if __name__ == '__main__':
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)