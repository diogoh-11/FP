def f1(lst):
    fin = open('f1.txt')
    s1 = 0
    s2 = 0
    for x in fin:
        lst.append(int(x))
        s1 += int(x)
        s2 += len(x.rstrip())

    return s1, s2

L = []
k1, k2 = f1(L)
print(k1)
print(k2)
print(len(L))
print(sum(L))
