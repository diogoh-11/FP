def calcular_preco(idade):
    if idade < 6:
        return 0
    elif 6 <= idade <= 12:
        return 2.50
    elif 13 <= idade <= 65:
        return 5.00
    else:
        return 2.50

def calcular_preco_total():
    total = 0
    idade = int(input("Idade da pessoa 1: "))
    total += calcular_preco(idade)
    
    idade = int(input("Idade da pessoa 2: "))
    total += calcular_preco(idade)
    
    idade = int(input("Idade da pessoa 3: "))
    total += calcular_preco(idade)
    
    idade = int(input("Idade da pessoa 4: "))
    total += calcular_preco(idade)
    return total

preco_total = calcular_preco_total()
print(f"Preço total a pagar: {preco_total} €")









        
    
