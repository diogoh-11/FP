import sys

def letras_possiveis_apos_prefixo(wordlist, prefix):
    try:
        with open(wordlist, "r", encoding="utf-8") as file:
            # Lê todas as palavras do arquivo e as armazena em uma lista
            lista = [line.strip() for line in file]

            # Filtra as palavras que começam com o prefixo
            palavras_com_prefixo = [word for word in lista if word.startswith(prefix)]

            # Extrai as letras que ocorrem imediatamente após o prefixo
            letras_possiveis = set(word[len(prefix)] for word in palavras_com_prefixo if len(word) > len(prefix))

            return list(letras_possiveis)

    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        return []

if __name__ == "__main__":
    # Verifica se o nome do arquivo foi fornecido como argumento
    if len(sys.argv) != 3:
        print("Uso: python letras_apos_prefixo.py <wordlist.txt> <prefixo>")
        sys.exit(1)

    arquivo = sys.argv[1]
    prefixo = sys.argv[2]

    letras_possiveis = letras_possiveis_apos_prefixo(arquivo, prefixo)
    print(f"Letras possíveis após o prefixo '{prefixo}': {letras_possiveis}")

