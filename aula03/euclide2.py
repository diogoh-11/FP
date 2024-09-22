def mdc_euclides(a, b):
    while b != 0:
        a, b = b, a % b
    print(a)
    return a
    
    
def variaveis():
    a = float(input("Qual é o valor de a:"))
    b = float(input("Qual é o valor de b:"))
    return(a,b)

def main():
    a,b=variaveis()
    mdc_euclides(a, b)
main()
