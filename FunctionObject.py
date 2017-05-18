'''
Reference:
    JavaScript 閉包（Closure) https://openhome.cc/Gossip/JavaScript/Closure.html
'''

def demo_1():
    # outer is a high-order function because it accept a function as parameter
    def outer(func, numbers):
        return func(numbers)

    def my_square(numbers):
        result = []
        for n in numbers:
            result.append(n * n)
        return result

    def my_cube(numbers):
        result = []
        for n in numbers:
            result.append(n * n * n)
        return result

    print(outer(my_square, [1, 2, 3, 4]))

    print(outer(my_cube, [1, 2, 3, 4]))

    # print(outer("abc", [1, 2, 3, 4]))

def demo_2():
    # outer is a high-order function because it return a function as result
    def outer(choice, numbers):
        if choice == 1:
            def my_square():
                result = []
                for n in numbers:
                    result.append(n * n)
                return result
            return my_square
        elif choice == 2:
            def my_cube():
                result = []
                for n in numbers:
                    result.append(n * n * n)
                return result
            return my_cube
        else:
            def do_nothing():
                return numbers
            return do_nothing

    f = outer(1, [1, 2, 3, 4])
    print(f())

    f = outer(2, [1, 2, 3, 4])
    print(f())

    f = outer(3, [1, 2, 3, 4])
    print(f())

def demo_3():
    def outer(choice, numbers):
        if choice == 1:
            def my_square():
                result = []
                for n in numbers:
                    result.append(n * n)
                return result
            return my_square()  # function name with parentheses means that execute this function
        elif choice == 2:
            def my_cube():
                result = []
                for n in numbers:
                    result.append(n * n * n)
                return result
            return my_cube()  # function name with parentheses means that execute this function
        else:
            def do_nothing():
                return numbers
            return do_nothing()  # function name with parentheses means that execute this function

    f = outer(1, [1, 2, 3, 4])
    print(f)

    f = outer(2, [1, 2, 3, 4])
    print(f)

    f = outer(3, [1, 2, 3, 4])
    print(f)

def demo_4():
    def outer():
        var = 5
        print("The value of variable, var, before define inner(): ", var)
        def inner():
            print("The value of variable, var, in inner(): ", var)

        print("The value of variable, var, after define inner(): ", var)
        return inner
    f = outer()
    f()

def demo_5():
    def outer(var):
        print("The value of variable, var, before define inner(): ", var)

        def inner():
            print("The value of variable, var, in inner(): ", var)

        print("The value of variable, var, after define inner(): ", var)
        return inner

    f = outer(10)
    f()

def demo_6():
    def outer(var):
        print("The value of variable, var, before define inner(): ", var)

        def inner():
            var = 12
            print("The value of variable, var, in inner(): ", var)

        print("The value of variable, var, after define inner(): ", var)
        return inner

    f = outer(10)
    f()

def demo_7():
    def outer(var):
        print("The value of variable, var, before define inner(): ", var)

        def inner():
            print("The value of variable, var, in inner(): ", var)

        print("The value of variable, var, after define inner(): ", var)

        print("Assign 12 to variable, var: ", var)
        var = 12

        return inner

    f = outer(10)
    f()

def main():
    splitter = "{:+<200}".format("")

    print("Demo closure and high-order function")

    print("Run demo_1")
    demo_1()
    print(splitter)

    print("Run demo_2")
    demo_2()
    print(splitter)

    print("Run demo_3")
    demo_3()
    print(splitter)

    print("Run demo_4")
    demo_4()
    print(splitter)

    print("Run demo_5")
    demo_5()
    print(splitter)

    print("Run demo_6")
    demo_6()
    print(splitter)

    print("Run demo_7")
    demo_7()
    print(splitter)

if __name__ == "__main__":
    main()