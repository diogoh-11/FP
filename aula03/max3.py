a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
def max2(a, b, c):
    maior = a    
    if a < b:
       maior = b
    if a < c:
       maior = c
    print(maior)   
max2(a, b, c)

