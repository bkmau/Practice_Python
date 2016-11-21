import random

def swap(data, i, j):
    tmp = data[j]
    data[j] = data[i]
    data[i] = tmp
    return data

def main():
    data = [random.randrange(0, 100) for _ in range(5)]

    for i in data:
        print(i, end=', ')
    print()

    i = len(data) - 1
    while i >= 0:
        j = 0
        while j < i:
            if data[j] > data[j + 1]:
                swap(data, j, j + 1)
            j += 1
        i -= 1

    for i in data:
        print(i, end=', ')

main()
