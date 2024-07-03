""" Transferência das reviews para Excel """
import pandas as pd
from mod_openai import *
from mod_cleansing import *


def exporta_reviews():

    # Lendo todas as reviews que estão no arquivo csv
    reviews = cleansing('raw_reviews.csv')
    respostas = [gpt_classifica(review) for review in reviews]

    sentimento = []
    propensao = []
    aspecto = []

    # Adicionando as análises do GPT às listas que contém as classificações do filme
    for i in range(len(respostas)):
        sentimento.append(respostas[i].split(",")[0])
        propensao.append(respostas[i].split(",")[1])
        aspecto.append(respostas[i].split(",")[2])

    # Colocando os dados em formato de dicionário
    data = {
        'Sentimento': sentimento,
        'Propensão': propensao,
        'Aspecto': aspecto
    }

    # Gerando um dataframe e um arquivo .xlsx com as reviews tratadas
    df = pd.DataFrame(data)

    df.to_excel('polished_reviews.xlsx', index=False)

