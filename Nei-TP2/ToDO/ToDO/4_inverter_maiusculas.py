"""
Escreva uma expressão que utilize uma função lambda para realizar a seguinte tarefa: 
dada uma lista de strings, retorne uma nova lista com cada string revertida e convertida para maiúsculas, 
mas apenas para aquelas strings que tenham um número ímpar de caracteres. 
As strings com um número par de caracteres devem permanecer inalteradas.
"""

# Lista de strings
lista_strings = ["Python", "is", "fun", "cool", "awesome"]

# Deve printar ['Python', 'is', 'NUF', 'cool', 'EMOSEWA']



lista_nova = [x[::-1].upper() if len(x) % 2 != 0 else x for x in lista_strings]

print(lista_nova)


