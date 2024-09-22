"""
Desenvolva uma função recursiva chamada contar_digitos_recursivo() que receba 
um número inteiro positivo e retorne a quantidade de dígitos que esse número possui.    
Por exemplo, para o número 12345, a função deve retornar 5. Se o número for negativo, 
a função deve tratar como se fosse positivo (ignorando o sinal).
"""

def contar_digitos_recursivo(n):
    # ToDo: Implemente a função

    if 0 < n < 10:
        return 1
    else:
        if n < 0:
            n = -n    

        return contar_digitos_recursivo(n//10) + 1

def main():
    testes_digitos = [12345, 7, 100000, -54321]
    resultados_digitos = {n: contar_digitos_recursivo(n) for n in testes_digitos}
    print(resultados_digitos) # Deve printar {12345: 5, 7: 1, 100000: 6, -54321: 5}

if __name__ == '__main__':
    main()