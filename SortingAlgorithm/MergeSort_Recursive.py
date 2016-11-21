import random

def merge(a, b):
    result = []
    i = 0
    j = 0
    while(i < len(a)) and (j < len(b)):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1
    return result

def mergersort(data):
    if len(data) == 1:
        return data
    else:
        a = mergersort(data[:len(data) // 2])
        b = mergersort(data[len(data) // 2:])
        return merge(a, b)

def main():
    data = [random.randrange(0, 100) for _ in range(5)]

    for i in data:
        print(i, end=', ')
    print()

    data = mergersort(data)

    for i in data:
        print(i, end=', ')

main()
