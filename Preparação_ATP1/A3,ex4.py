def calculapreco(age):
    if age < 6:
        p = 0
    elif 6 <= age <= 12:
        p = 2.5  # Use um ponto (.) para representar números decimais em Python
    elif 13 <= age <= 35:
        p = 5
    else:
        p = 2.5
    return p


def main():
    x1 = calculapreco(int(input("Qual a tua idade: ")))
    x2 = calculapreco(int(input("Qual a tua idade: ")))
    x3 = calculapreco(int(input("Qual a tua idade: ")))
    x4 = calculapreco(int(input("Qual a tua idade: ")))
    pt = x1+x2+x3+x4
    print("O preço total é de", pt, "€")


main()
