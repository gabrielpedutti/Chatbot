import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise ValueError("Erro: GENAI_API_KEY não foi encontrada. Verifique seu arquivo .env")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

with open("data.txt", "r", encoding="utf-8") as file:
    animes_2025 = json.load(file)

PROMPT_BASE = f"""
Você é um assistente especializado em animes e mangás, chamado OtakuBot.
Suas respostas devem ser fáceis de entender e com explicações claras. Evite gírias muito exageradas, mas pode usar termos do mundo Otaku.
Seja educado e evite responder perguntas fora do escopo.

Aqui estão alguns animes de 2025 que você pode utilizar para responder às perguntas:
{json.dumps(animes_2025, indent=2)}

Porém além destes, você pode usar o conhecimento de animes e mangás em geral para responder às perguntas.

Para melhorar a experiência do usuário, que visualizará este chat através do terminal, ao invés de "**" e "*", que não formatarão corretamente, 
utilize as cores ANSI (ex: \033[1;32m) para destacar as mensagens.

Agora, o usuário fará três perguntas sobre esse tema. Responda com base no conhecimento disponível.
Guarde todas as perguntas e respostas para um relatório final que será solicitado posteriormente.
"""

print("\033[1;32mOlá! Sou o OtakuBot e estou pronto para responder suas perguntas sobre animes e mangás.\n\033[0m")

chat.send_message(PROMPT_BASE)

for i in range(1, 4):
    pergunta = input(f"\033[1;34mDigite sua pergunta {i}:\033[0m ")

    print("\033[1;33mProcessando sua pergunta...\033[0m")
    time.sleep(2)

    response = chat.send_message(pergunta)

    resposta = response.text.strip()

    print("\n\033[1;36mResposta:\033[0m")
    print(f"\033[1;37m{resposta}\033[0m")
    print("-" * 50)

resumo_prompt = """Agora, gere um relatório com as 3 perguntas e respostas que discutimos anteriormente. 
Siga o padrão: Relatório de Perguntas e Respostas - OtakuBot
 Pergunta 1: [pergunta] Resposta 1: [resposta] Pergunta 2: [pergunta] Resposta 2: [resposta] Pergunta 3: [pergunta] Resposta 3: [resposta]"""
resumo_response = chat.send_message(resumo_prompt)

print("\n\033[1;32mResumo Final:\033[0m\n")
print(f"\033[1;37m{resumo_response.text}\033[0m")
print("\n\033[1;32mObrigado por usar o OtakuBot! :) Até logo!\033[0m")
