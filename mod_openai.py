""" Geração de Insights Usando a API da OpenAI """
from openai import OpenAI


def gpt_classifica(comment):

    client = OpenAI(api_key="INSIRA SUA CHAVE AQUI")

    # Definindo o prompt que analisará as reviews

    prompt = [{
        "role": "user",
        "content": f'Chat, voce vai analisar uma review deixada por um espectador do filme "Paris, Texas" e retornar 3 classificações no formato "Classificação 1, Classificação 2, Classificação 3" sem NENHUM complemento antes ou depois e em formato de título. A primeira classificação é o Sentimento, que deve ser avaliado entre "Detestei", "Não gostei", "Apático", "Gostei" ou "Amei". A segunda classificação é a Propensão, que deve ser avaliada entre "Veria Novamente" ou "Não Veria Novamente". A última classificação é o Aspecto, que deve ser avaliado entre "Roteiro", "Fotografia", "Originalidade", "Atuação", "Emoção". O comentário é {comment}\n'
        }]

    response = client.chat.completions.create(
        model='gpt-3.5-turbo-0125',
        messages=prompt,
        max_tokens=600,
        temperature=1
    )

    resposta_do_chat = response.choices[0].message.content

    return resposta_do_chat
