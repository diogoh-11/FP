def fib():
    n = int(input("Qual termo: "))
    t1 = 0
    t2 = 1
    o = 2
    while o < n:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        o += 1
    print(t3)


fib()


def fib():
    n = int(input("Qual termo: "))
    
    if n == 1:
        print(0)
    else:
        t1, t2 = 0, 1
        for _ in range(2, n):
            t1, t2 = t2, t1 + t2
        
        print(t2)

fib()
