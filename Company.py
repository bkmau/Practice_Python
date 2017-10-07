class Employee:

    regular_raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = "{}.{}@company.com".format(first, last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        self.email = value

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, value):
        self.salary = value

    def apply_raise_1(self):
        self.salary = self.salary * self.regular_raise_amount

    def apply_raise_2(self):
        self.salary = self.salary * Employee.regular_raise_amount

    @classmethod
    def from_info_string(cls, info):
        first, last, salary = info.split("-")
        return cls(first, last, salary)

    # The goal of __str__() is to be readable. The goal of __repr__() is to be unambiguous.
    def __str__(self):
        return "Hi, My name is {} {} and email is {}. I get ${:,.1f} for a month.".format(
            self.first, self.last, self.email, self.salary)

class Engineer(Employee):

    technological_bonus = 100

    def __init__(self, first, last, salary, *prog_skill):
        super().__init__(first, last, salary)

        self.prog_skill = prog_skill

    def prog_skill(self):
        print("I am familir with {}".format(",".john(self.prog_skill)))

    def prog_skill(self, *skills):
        if skills:
            for skill in skills:
                self.__prog_skill.append(skill)

    def apply_raise_2(self):
        self.salary = super().salary + self.technological_bonus * len(self.prog_skill)

    def __str__(self):
        if self.__prog_skill:
            return "{} I am familiar with {}.".format(
                super().__str__(), ", ".join(self.prog_skill))
        else:
            return "{} I an new in programming.".format(super().__str__())

class Manager(Employee):

    regular_raise_amount = 1.05

    def __init__(self, first, last, department, base_salary, subordinates=None):
        super().__init__(first, last, department, base_salary)

        if subordinates:
            self.__subordinates = subordinates
        else:
            self.__subordinates = []

    @property
    def subordinates(self):
        return self.__subordinates

    @subordinates.setter
    def subordinates(self, *subordinates):
        for subordinate in subordinates:
            self.__subordinates.append(subordinate)

    def subordinates_resign(self, *subordinates):
        for subordinate in subordinates:
            if subordinate in self.__subordinates:
                print("{} resigned from our company.".format(subordinate.fullname))
                self.__subordinates.pop(self.__subordinates.index(subordinate))
            else:
                print("Who is {}".format(subordinate.fullname))

    def __str__(self):
        if self.__subordinates:
            return "{} I am manager of {} dept, {} works for me. I get pay ${:,.2f} this year.".format(
                super().__str__(), self.department,
                ", ".join(subordinate.fullname for subordinate in self.__subordinates), 5000)
        else:
            return "{} ".format(super().__str__())


def main():
    john = Employee("John", "Richard", 1000)
    mary = Employee("Mary", "Jensen",  1000)

    print("instance.method() vs class.method(instance)")
    print("John is work on {} depart.".format(john.department))
    john.shift_department("Admin.")
    print("John is work on {} depart.".format(john.department))
    Employee.shift_department(john, "R&D")
    print("John is work on {} depart.".format(john.department))

    print()

    print("Class variable...")
    print("Namespace...")
    print(Employee.__dict__)
    print(john.__dict__)
    print(mary.__dict__)

    print("Before run Employee.regular_raise_amount = 120")
    print("Employee.regular_raise_amount is {}".format(Employee.regular_raise_amount))
    print("john.regular_raise_amount is {}".format(john.regular_raise_amount))
    print("mary.regular_raise_amount is {}".format(mary.regular_raise_amount))

    print("After run Employee.regular_raise_amount = 120")
    Employee.regular_raise_amount = 1.05
    print("Employee.regular_raise_amount is {}".format(Employee.regular_raise_amount))
    print("john.regular_raise_amount is {}".format(john.regular_raise_amount))
    print("mary.regular_raise_amount is {}".format(mary.regular_raise_amount))

    print("Print namespace of john, instance of class Employee, after run john.regular_raise_amount = 1.06")
    john.regular_raise_amount = 1.06
    print(john.__dict__)
    print("And variable regular_raise_amount is...")
    print("Employee.regular_raise_amount is {}".format(Employee.regular_raise_amount))
    print("john.regular_raise_amount is {}".format(john.regular_raise_amount))
    print("mary.regular_raise_amount is {}".format(mary.regular_raise_amount))

    print("Use class method, from_info_string, to create a Employee instance")
    jim = Employee.from_info_string("Jim-Hall-1200")
    print(jim.__dict__)
    
if __name__ == '__main__':
    main()

