def func(lst):
    fin = open('f1.txt')
    n = 0
    s = 0
    for x in fin:
        y = int(x)
        print(y, end=',')
        lst.append( y )
        s += y
        n += 1
    print()
    fin.close()
    return s, s/n

li = []
k1, k2 = func(li)
print(k1)
print(k2)
print(len(li))