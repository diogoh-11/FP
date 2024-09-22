import sys


def contar_letras(wordlist):
    # Dicionário para armazenar a contagem de cada letra
    contagem_letras = {}
    
    try:
        with open(wordlist, "r", encoding="utf-8") as file:
            for line in file:
                for character in line:
                    if character.isalpha():
                        if not character.lower() in contagem_letras:
                            contagem_letras[character.lower()] = 1
                        else:
                            contagem_letras[character.lower()] += 1

        # Ordena o dicionário por chaves (letras) em ordem alfabética
        contagem_letras_ordenada = dict(sorted(contagem_letras.items(), key= lambda contagem: contagem[1], reverse=True))

        # Imprime a contagem de cada letra
        for letra, contagem in contagem_letras_ordenada.items():
            print(f"{letra}: {contagem}")


    except FileNotFoundError:
        print("O ficheiro não foi encontrado.")


if __name__ == "__main__":
    # Verifica se o nome do arquivo foi fornecido como argumento
    if len(sys.argv) != 2:
        print("Uso: python contar_letras.py <wordlist.txt>")
        sys.exit(1)

    Lusiadas = sys.argv[1]
    contar_letras(Lusiadas)