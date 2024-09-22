# Este programa demonstra a leitura e utilização de dados de um ficheiro JSON
# com mensagens do Twitter.
# Modifique-o para resolver o problema proposto.

# O módulo json permite descodificar ficheiros no formato JSON.
# São ficheiros de texto que armazenam objetos compostos que podem incluir
# números, strings, listas e/ou dicionários.
import json
from collections import Counter

def main():
    # Abre o ficheiro e descodifica-o criando o objeto twits.
    with open("twitter.json", encoding="utf8") as f:
        twits = json.load(f)

    # Cria uma lista de todas as palavras mencionadas nos twits.
    all_words = []
    for twit in twits:
        all_words.extend(twit["text"].split())

    # Remove caracteres especiais e mantém apenas as palavras começadas por '#'.
    hashtags = [word.lower() for word in all_words if word.startswith("#")]

    # Cria um histograma das hashtags.
    hashtag_counts = Counter(hashtags)
    sorted_hashtags = hashtag_counts.most_common()

    # Encontrar o fator de normalização para o histograma.
    max_count = sorted_hashtags[0][1]
    normalization_factor = 18 / max_count

    # Imprime o histograma normalizado.
    for hashtag, count in sorted_hashtags:
        normalized_count = int(count * normalization_factor)
        histogram = '+' * normalized_count
        print(f"{hashtag.ljust(6)} ({count:3}) {histogram}")

if __name__ == "__main__":
    main()


