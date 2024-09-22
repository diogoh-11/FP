"""
Crie uma função chamada elementos_unicos() que receba uma lista de listas e retorne um conjunto 
que contém todos os elementos que aparecem exatamente uma vez em todas as listas combinadas. 
Se um elemento aparecer mais de uma vez ao longo de todas as listas, ele não deve ser incluído no conjunto retornado.
Por exemplo, dado [[1, 2, 3], [3, 4, 5], [5, 6, 7]], 
a função deve retornar {1, 2, 4, 6, 7}, pois os números 3 e 5 aparecem mais de uma vez.

"""

def elementos_unicos(lista_de_listas):
    
    todas_as_listas = [elementos for lista in lista_de_listas for elementos in lista ]

    contagem = {elementos : todas_as_listas.count(elementos) for elementos in todas_as_listas}

    conjunto = {elementos for elementos, ocorrencias in contagem.items() if ocorrencias == 1}

    return conjunto

def main():
    listas_teste = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    print(elementos_unicos(listas_teste)) # Deve printar {1, 2, 4, 6, 7}

    listas_teste = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [1, 2, 7]]
    print(elementos_unicos(listas_teste)) # Deve printar {4, 6}

if __name__ == '__main__':
    main()