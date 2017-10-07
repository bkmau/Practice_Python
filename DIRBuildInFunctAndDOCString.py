'''
Here is module description
'''
import builtins

print(__doc__)

print(dir())

print(dir(builtins))

print(dir(FileNotFoundError))


class People:
    '''
    Here is people define
    '''
    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    def __init__(self, name, gender, age):
        self.__name = name
        self.__gender = gender
        self.__age = age

    @classmethod
    def do_job(cls):
        return "I am working!!"

print(dir(People))
print()
print(People.__dict__)
print(People.__doc__)
