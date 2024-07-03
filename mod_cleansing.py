""" Limpeza dos dados e organização em lista """

import pandas as pd


def cleansing(a):
    # Leitura do arquivo Excel especificado pelo argumento 'a'
    reviews = pd.read_csv(a)

    # Transformar cada linha em uma lista de strings e depois em uma lista única
    lista_de_reviews = reviews.apply(lambda row: ' '.join(map(str, row)), axis=1).tolist()
    reviews_limpa = []

    for review in range(len(lista_de_reviews)):

        # Substituir todas as ocorrências de "'" por ""
        reviews = lista_de_reviews[review].replace("'", "")

        # Converter a string da review em uma lista de caracteres
        reviews = list(reviews)

        # Encontrar o índice do primeiro espaço (' ')
        whitespace_index = reviews.index(' ')

        # Adicionar à lista reviews_limpa conteúdo da review a partir da sua numeração, separada do texto por um espaço
        reviews_limpa.append(''.join(reviews[(whitespace_index + 1):]))
    return reviews_limpa
