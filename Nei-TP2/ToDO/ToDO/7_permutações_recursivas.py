"""
Crie uma função recursiva chamada permutacoes_recursivas que receba uma string 
e retorne todas as permutações possíveis dessa string. 
Uma permutação é um rearranjo das letras da string.                                                                                                                    Por exemplo, as permutações da string "abc" seriam "abc", "acb", "bac", "bca", "cab", "cba". A função deve retornar uma estrutura que não contenha elementos repetidos.
Se for testada a string "aab" apenas deve ser retornado "aab", "aba", "baa"
"""

def permutacoes_recursivas(s):
    if len(s) <=1:
        return s# ToDo: Implemente a função
    
    return { c[:n]+ s[-1] + c[n:] for c in permutacoes_recursivas(s[:-1]) for n in range(len(s))}




def main():
    exemplo = "abc"
    print(permutacoes_recursivas(exemplo)) # Deve printar {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}

    exemplo = "aab"
    print(permutacoes_recursivas(exemplo)) # Deve printar {'aab', 'aba', 'baa'}

    exemplo = "aaa"
    print(permutacoes_recursivas(exemplo)) # Deve printar {'aaa'}


if __name__ == '__main__':
    main()