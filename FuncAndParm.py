"""
SEE
PEP 3102 -- Keyword-Only Arguments
https://www.python.org/dev/peps/pep-3102/

PEP 3107 - Function Annotations
https://www.python.org/dev/peps/pep-3107/

More Control Flow Tools in Python 3.5.3 documentation
https://docs.python.org/3.5/tutorial/controlflow.html#defining-functions
"""

def func1(a, b):
    print("a = {}, b = {}".format(a, b))


def func2(a, b=None):
    print("a = {}, b = {}".format(a, b))


def func3(*args):
    for index, element in enumerate(args):
        print("index = {} value = {}".format(index, element))


def func4(**kwargs):
    # kwargs = keyword arguments
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



