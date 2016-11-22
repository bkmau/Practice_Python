import random

def swap(a, b):
    for i in b:
        a.append(i)
    i = 0
    while i < (len(a) - 1):
        if a[i] < a[i + 1]:
            break
        else:
            tmp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = tmp
            i += 1
    return a

def bubblesort(data):
    if len(data) == 1:
        return data
    else:
        last = [data[len(data) - 1]]
        b = bubblesort(data[:(len(data) - 1)])
        return swap(last, b)

def main():
    data = [random.randrange(0, 100) for _ in range(5)]
    for i in data:
        print(i, end=', ')
    print()

    data = bubblesort(data)

    for i in data:
        print(i, end=', ')

main()
