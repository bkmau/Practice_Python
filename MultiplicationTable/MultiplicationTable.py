multiTable = [[0] * 9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        multiTable[i][j] = (i + 1) * (j + 1)

for i in multiTable:
    for j in i:
        print("{:>2}, ".format(j), end="")
    print()
