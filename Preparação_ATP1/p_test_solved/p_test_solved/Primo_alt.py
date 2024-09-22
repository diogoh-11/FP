def primo():
    n = int(input("Digite um númrto: "))
    c = 2
    if n < 2:
        return False
    for c in range(c, n):
        if n % c == 0:
            return False
        else:
            c += 1
    return True


print(primo())
