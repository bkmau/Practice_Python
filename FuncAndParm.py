"""
PEP 3107 - Function Annotations
https://www.python.org/dev/peps/pep-3107/
"""

def func1(a, b):
    print("a = {}, b = {}".format(a, b))


def func2(a, b=None):
    print("a = {}, b = {}".format(a, b))


def func3(*args):
    for index, element in enumerate(args):
        print("index = {} value = {}".format(index, element))


def func4(**kwargs):
    for key, value in kwargs.items():
        print("key = {} value = {}".format(key, value))


def main():
    print("Execute func1(a, b)")
    func1(1, 2)

    print("Execute func2(a, b=None)")
    func2(3, 4)

    print("Execute func2(a, b=None)")
    func2(3)

    print("Execute func3(*args)")
    func3(6, 7, 8)

    print("Execute func4(**kwargs)")
    func4(a=6, b=7, c=8)

main()



