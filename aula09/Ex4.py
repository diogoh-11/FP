import sys
import bisect


def contar_letras(wordlist):
    # Dicionário para armazenar a contagem de cada letra
    
    try:
        with open(wordlist, "r", encoding="utf-8") as file:
            lista = [line.strip() for line in file]
            
            e = bisect.bisect_left(lista, "ea")
            d = bisect.bisect_left(lista, "eb")
            n = d-e
            print(f"Existem {n} palavras entre ea e eb")
            print(lista[e:d])
                

        # Ordena o dicionário por chaves (letras) em ordem alfabética


    except FileNotFoundError:
        print("O ficheiro não foi encontrado.")


if __name__ == "__main__":
    # Verifica se o nome do arquivo foi fornecido como argumento
    if len(sys.argv) != 2:
        print("Uso: python contar_letras.py <wordlist.txt>")
        sys.exit(1)

    texto = sys.argv[1]
    contar_letras(texto)