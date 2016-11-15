message = input("Please input a string to hide in uppercase:")
secret = ""
original = ""
code = []
len_code_per_word = 0

for char in message:
    code.append(ord(char))
    if len_code_per_word < len(str(ord(char))):
        len_code_per_word = len(str(ord(char)))

f = "{:0>" + str(len_code_per_word) + "}"
for c in code:
    secret += f.format(c)
print("Secret Message: {}".format(secret))

for i in range(0, len(secret), len_code_per_word):
    original += chr(int(secret[i:(i + len_code_per_word)]))
print("Original Message: {}".format(original))
