# -*- coding: utf-8 -*-
"""TESTE_API_IA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BnhOse2WPZ7JXbn6cx8Au16k8BNJ1JpW
"""

!pip install openai==0.28

import os
import openai

os.environ['OPENAI_API_KEY'] = ''
openai.api_key = os.getenv('OPENAI_API_KEY')

def enviar_mensagem(mensagem, modelo="gpt-3.5-turbo"):
    """
    Envia uma mensagem ao modelo ChatGPT e retorna a resposta.
    """
    try:
        resposta = openai.ChatCompletion.create(
            model=modelo,
            messages=[{"role": "user", "content": mensagem}]
        )
        return resposta.choices[0].message['content']
    except Exception as e:
        return f"Erro ao conectar com a API: {e}"

mensagem_teste = "Olá, ChatGPT! Como você está?"
resposta = enviar_mensagem(mensagem_teste)
print(resposta)
