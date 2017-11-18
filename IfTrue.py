
class foo:
    pass

s1 = ""

if s1:
    print("Hello s1")

s2 = "s2"

if s2:
    print("Hello s2")

n1 = 0

if n1:
    print("Hello n1")

n2 = 1

if n2:
    print("Hello n2")

n3 = 5

if n3:
    print("Hello n3")

n4 = -1

if n4:
    print("Hello n4")

n5 = -8

if n5:
    print("Hello n5")

l1 = []

if l1:
    print("Hello l1")

l2 = ['']

if l2:
    print("Hello l2")

obj1 = None

if obj1:
    print("Hello obj1")

obj2 = foo

if obj2:
    print("Hello obj2")

s = ""
for index, i in enumerate(range(20)):
    s += "{}, {}".format(i, "\r\n" if index % 5 == 4 else "")
print(s)

print(11 % 5)