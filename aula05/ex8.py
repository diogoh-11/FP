def evenThenOdd(s):
    # Obtém os caracteres das posições pares (0, 2, 4, ...) usando slicing
    even_chars = s[::2]

    # Obtém os caracteres das posições ímpares (1, 3, 5, ...) usando slicing
    odd_chars = s[1::2]

    # Concatena os caracteres pares e ímpares
    result = even_chars + odd_chars

    return result


# Teste
input_string = "abcd"
output_string = evenThenOdd(input_string)
print(output_string)


def removeAdjacentDuplicates(s):
    # Se a string for vazia, não há nada a fazer
    if not s:
        return ""

    # Inicializa a string resultante com o primeiro caractere da string original
    result = s[0]

    # Itera sobre os caracteres da string original, começando do segundo caractere
    for char in s[1:]:
        # Verifica se o caractere atual é igual ao último caractere adicionado à string resultante
        if char != result[-1]:
            result += char  # Adiciona o caractere à string resultante se não for duplicado

    return result


# Teste
input_string = "Mississippi"
output_string = removeAdjacentDuplicates(input_string)
print(output_string)


def generate_pattern(n):
    result = []

    for i in range(1, n + 1):
        repeated_numbers = [i] * i
        result.extend(repeated_numbers)

    return result


# Teste
n = 4
result_list = generate_pattern(n)
print(result_list)
