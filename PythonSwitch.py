
def my_func(operator, x, y):
    return {
        "+": lambda: x + y,
        "-": lambda: x - y,
        "*": lambda: x * y,
        "/": lambda: x // y,
        "%": lambda: x % y
    }.get(operator, lambda: None)()

print(my_func("/", 4, 2))

print(my_func("+", 4, 2))