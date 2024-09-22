def pif(n):
    pi = 0
    for i in range(n):
        pi += ((-1)**i) / ((2*i)+1)
    pi *= 4
    return pi


def main():
    n = int(input("Quantas casas decimais queres: "))
    pi_estimado = pif(n)
    print("A estimativa de pi para", n, "casas decimais é de ", pi_estimado)


main()
