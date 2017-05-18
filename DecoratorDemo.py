

def decorator_func_v1(orig_func):
    print("decorator_func_v1 execute")

    def wrapper_func_v1():
        print("wrapper_func_v1 execute")
        return orig_func()
    return wrapper_func_v1

def disp_func_v1():
    print("Hello, world")

func_1 = decorator_func_v1(disp_func_v1)
func_1()

@decorator_func_v1
def disp_func_v2():
    print("Hello, Mars")

disp_func_v2()

def decorator_func_v2(orig_func):
    print("decorator_func_v2 execute")

    def wrapper_func_v2(*args, **kwargs):
        print("wrapper_func_v2 execute")
        return orig_func(*args, **kwargs)
    return wrapper_func_v2

@decorator_func_v2
def disp_func_v31():
    print("Hello, Jupiter")

@decorator_func_v2
def disp_func_v32(name, age):
    print("I am {}, {} years old".format(name, age))

disp_func_v31()
disp_func_v32("John", 35)

class MyDecorator():
    def __init__(self, orig_func):
        self.func = orig_func

    def __call__(self, *args, **kwargs):
        print("Warpper is execute")
        return self.func(*args, **kwargs)

@MyDecorator
def disp_func_v31():
    print("Hello, Mercury")

@MyDecorator
def disp_func_v32(name, age):
    print("I am {}, {} years old".format(name, age))

disp_func_v31()
disp_func_v32("Marry", 32)

import time

from functools import wraps

def my_logger(func):
    import logging
    logging.basicConfig(filename="{}.log".format(func.__name__),
                        level=logging.INFO)
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Run {} with args: {}, kwargs: {}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return wrapper

def my_timmer(func):
    import time
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print("{} run in {} seconds".format(func.__name__, (stop - start)))
        return result

    return wrapper

@my_logger
@my_timmer
def my_tfunc(name, age):
    time.sleep(1)
    print("my_tfunc with arguments:({}, {})".format(name, age))

my_tfunc("Tom", 20)


def prefix_decorator_function(prefix):
    def decorator_function(orig):
        def wrapper_function(*args, **kwargs):
            print("{} Execute before {}".format(prefix, orig.__name__))
            result = orig(*args, **kwargs)
            print("{} Execute After {}\n".format(prefix, orig.__name__))
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator_function("Log:")
def display(name, age):
    print("Run display with arguments({}, {})".format(name, age))

display("John", 25)
display("Travis", 30)





