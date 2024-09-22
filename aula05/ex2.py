def inputFloatList():
    n = input("Introduz um número ")
    lst = []
    while n != "":
        lst.append(float(n))
        n = input("Introduz um número ")

    print(lst)
    return (lst)


def countLower(lst, v):
    t = 0
    for c in range(len(lst)):
        if lst[c] > v:
            t += 1
    return t


def minmax(lst):

    min_val = lst[0]
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
    for c in range(1, len(lst)):
        if lst[c] > max_val:
            max_val = lst[c]

    return max_val, min_val


numbers = inputFloatList()
result = countLower(numbers, 4)
print(result)
print(minmax(numbers))
