s = "abc"
print("string s: {}, address of string s is {}".format(s, hex(id(s))))

s = "def"
print("string s: {}, address of string s is {}".format(s, hex(id(s))))

s += "ghi"
print("string s: {}, address of string s is {}".format(s, hex(id(s))))

s = s.join("jkl")
print("string s: {}, address of string s is {}".format(s, hex(id(s))))

s = "abc"
for index, item in enumerate(s):
    print("string s: {0}, address of string s is {1}; s[{2}]: {3}, address of s[{2}] is {4}({5})".format(
        s, hex(id(s)), index, s[index], hex(id(s[index])), id(s[index])))

try:
    s[0] = "i"
except TypeError as e:
    print(e)

s = ["a", "b", "c"]
for index, item in enumerate(s):
    print("string s: {0}, address of string s is {1}; s[{2}]: {3}, address of s[{2}] is {4}({5})".format(
        s, hex(id(s)), index, s[index], hex(id(s[index])), id(s[index])))

try:
    s[0] = "z"
except TypeError as e:
    print(e)

for index, item in enumerate(s):
    print("string s: {0}, address of string s is {1}; s[{2}]: {3}, address of s[{2}] is {4}({5})".format(
        s, hex(id(s)), index, s[index], hex(id(s[index])), id(s[index])))

n = 8
print("number n: {}, address of number n is {}".format(n, hex(id(n))))
n = 9
print("number n: {}, address of number n is {}".format(n, hex(id(n))))
n += 3
print("number n: {}, address of number n is {}".format(n, hex(id(n))))
