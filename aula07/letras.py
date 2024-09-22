import sys


def contar_letras(Lusiadas):
    # Dicionário para armazenar a contagem de cada letra
    contagem_letras = {}

    try:
        # Abre o arquivo para leitura
        with open(Lusiadas, 'r', encoding='utf-8') as arquivo:
            # Lê o conteúdo do arquivo
            texto = arquivo.read()

            # Converte todas as letras para minúsculas
            texto = texto.lower()

            # Itera sobre cada caractere no texto
            for char in texto:
                # Verifica se o caractere é uma letra
                if char.isalpha():
                    # Incrementa a contagem da letra no dicionário
                    contagem_letras[char] = contagem_letras.get(char, 0) + 1

    except FileNotFoundError:
        print(f"O arquivo '{Lusiadas}' não foi encontrado.")
        sys.exit(1)

    # Ordena o dicionário por chaves (letras) em ordem alfabética
    contagem_letras_ordenada = dict(sorted(contagem_letras.items()))

    # Imprime a contagem de cada letra
    for letra, contagem in contagem_letras_ordenada.items():
        print(f"{letra}: {contagem}")


if __name__ == "__main__":
    # Verifica se o nome do arquivo foi fornecido como argumento
    if len(sys.argv) != 2:
        print("Uso: python contar_letras.py <Lusiadas.txt>")
        sys.exit(1)

    Lusiadas = sys.argv[1]
    contar_letras(Lusiadas)
