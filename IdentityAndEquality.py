s1 = "Hello World"
s2 = "Hello World"
s3 = s1

print("s1 is {}, s2 is {}, s3 is {}".format(s1, s2, s3))
print("s1's Address:{}, s2's Address:{}, s3's Address:{}".format(id(s1), id(s2), id(s3)))
print("is s1 == s2:{}, does s1 is s2: {}".format(s1 == s2, s1 is s2))
print("is s3 == s3:{}, does s1 is s3: {}".format(s1 == s3, s1 is s3))

s1 = "Hello World2"

print("after change s1 to {}".format(s1))
print("s1's Address:{}, s2's Address:{}, s3's Address:{}".format(id(s1), id(s2), id(s3)))
print("is s1 == s2:{}, does s1 is s2: {}".format(s1 == s2, s1 is s2))
print("is s3 == s3:{}, does s1 is s3: {}".format(s1 == s3, s1 is s3))

print("")

n1 = 4
n2 = 4
n3 = n1

print("n1 is {}, n2 is {}, n3 is {}".format(n1, n2, n3))
print("n1's Address:{}, n2's Address:{}, n3's Address:{}".format(id(n1), id(n2), id(n3)))
print("is n1 == n2:{}, does n1 is n2: {}".format(n1 == n2, n1 is n2))
print("is n1 == n3:{}, does n1 is n3: {}".format(n1 == n3, n1 is n3))

n1 = 8
print("after change n1 to {}".format(n1))
print("n1's Address:{}, n2's Address:{}, n3's Address:{}".format(id(n1), id(n2), id(n3)))
print("is n1 == n2:{}, does n1 is n2: {}".format(n1 == n2, n1 is n2))
print("is n1 == n3:{}, does n1 is n3: {}".format(n1 == n3, n1 is n3))

print("")

f1 = 2.2
f2 = 2.2
f3 = f1

print("f1 is {}, f2 is {}, f3 is {}".format(f1, f2, f3))
print("f1's Address:{}, f2's Address:{}, f3's Address:{}".format(id(f1), id(f2), id(f3)))
print("is f1 == f2:{}, does f1 is f2: {}".format(f1 == f2, f1 is f2))
print("is f1 == f3:{}, does f1 is f3: {}".format(f1 == f3, f1 is f3))

f3 = 8.5
print("after change f3 to {}".format(f3))
print("f1's Address:{}, f2's Address:{}, f3's Address:{}".format(id(f1), id(f2), id(f3)))
print("is f1 == f2:{}, does f1 is f2: {}".format(f1 == f2, f1 is f2))
print("is f1 == f3:{}, does f1 is f3: {}".format(f1 == f3, f1 is f3))


print("")

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1

print("l1 is {}, l2 is {}, l3 is {}".format(l1, l2, l3))
print("s1's Address:{}, s2's Address:{}, s3's Address:{}".format(id(l1), id(l2), id(l3)))
print("is s1 = s2:{}, does s1 is s2: {}".format(l1 == l2, l1 is l2))
print("is s3 = s3:{}, does s1 is s3: {}".format(l1 == l3, l1 is l3))

# f1 = Foo()
# f2 = Foo()
# f3 = Foo()
#
# print("f1's Address:{}, f2's Address:{}, is f1 = f2:{}, does f1 is f2:{}".format(id(f1), id(f2), f1 == f2, f1 is f2))
# print("f1's Address:{}, f3's Address:{}, is f1 = f3:{}, does f1 is f3:{}".format(id(f1), id(f3), f1 == f3, f1 is f3))
# print(f3 is f2)
