from operator import attrgetter

class Employee:
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.title = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def __init__(self, id, name, title, salary):
        self.__id = id
        self.__name = name
        self.__title = title
        self.__salary = salary

    def __repr__(self):
        return "Name:{}\r\nTitle:{}\r\nSalary:${} / month\r\n".format(self.__name, self.__title, self.__salary)

def main():

    employs = [
        Employee(1, "John", "President", 6000),
        Employee(2, "Leo", "General Manager", 4200),
        Employee(3, "Adam", "Senior Engineer", 4000),
        Employee(4, "Jim", "Engineer", 2775),
        Employee(5, "Adolf", "Engineer", 2750),
        Employee(6, "Edward", "Engineer", 2760)]
    # employs.sort() # get error: TypeError: unorderable types: Employee() < Employee()

    employs_sort_by_name = sorted(employs, key=get_sorted_key)
    for e in employs_sort_by_name:
        print(e)

    employs_sort_by_name = sorted(employs, key=lambda e: e.name)
    for employ in employs_sort_by_name:
        print(employ)

    employs_sort_by_name = sorted(employs, key=attrgetter("name"))
    for employ in employs_sort_by_name:
        print(employ)


def get_sorted_key(employee):
    return employee.name

main()