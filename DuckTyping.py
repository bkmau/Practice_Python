class Duck:
    def quack(self):
        print("Quack, Quack")

    def fly(self):
        print("Flap, Flap")

class People:
    def quack(self):
        print("I'm quacking like a duck")

    # def fly(self):
    #     print("I'm flying my arms!")

def quack_and_fly(thing):
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("Thing has to be a duck")

def quack_and_fly_non_pythonic(thing):
    if hasattr(thing, "quack"):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, "fly"):
        if callable(thing.fly):
            thing.fly()

def quack_and_fly_pythonic(thing):
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

print("Checking Type of parameter")
quack_and_fly(Duck())
quack_and_fly(People())
print()

print("Duck Typing non-pythonic")
quack_and_fly_non_pythonic(Duck())
quack_and_fly_non_pythonic(People())
print()

print("Duck Typing pythonic")
quack_and_fly_pythonic(Duck())
quack_and_fly_pythonic(People())