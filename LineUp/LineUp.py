from itertools import cycle

num_of_cus = 15
start_no = 8
every_pass_person_picked = 3
total_person_picked = 9

line = ["" for x in range(num_of_cus)]

index = start_no
line[start_no - 1] = "*"
total_person_picked -= 1
j = 1
result = str(start_no) + ","

while total_person_picked != 0:
    if j == every_pass_person_picked:
        if line[index] != "*":
            j = 1
            line[index] += "*"
            result += str(index + 1) + ","
            total_person_picked -= 1
    else:
        if line[index] != "*":
            j += 1
    if index == (len(line) - 1):
        index = 0
    else:
        index += 1

print(line)
print(result)
