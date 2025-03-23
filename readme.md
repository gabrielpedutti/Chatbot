# OtakuBot: Assistente Virtual para Animes e Mangás

OtakuBot é um assistente virtual especializado em responder perguntas sobre animes e mangás. Ele utiliza a API do Google Gemini para fornecer respostas baseadas em um conjunto de dados de animes lançados em 2025. O bot pode responder até três perguntas, fornecendo explicações claras e acessíveis, tudo isso de forma interativa no terminal.

## Funcionalidades

- Respostas sobre animes de 2025 e sobre o mundo de animes e mangás em geral.
- Interação no terminal com perguntas e respostas.
- Relatório final gerado com base nas perguntas e respostas discutidas.
- Suporte para usuários iniciantes e experientes no universo otaku.

## Tecnologias

- **Google Gemini API**: Usada para gerar respostas dinâmicas baseadas nas perguntas dos usuários.
- **dotenv**: Para carregar variáveis de ambiente, como a chave da API.
- **JSON**: Para armazenar e manipular dados de animes.
- **Python 3**: Linguagem de programação usada para o desenvolvimento do projeto.

## Como Usar

### Pré-requisitos

1. **Python 3.x** instalado na sua máquina.
2. **Bibliotecas**: Você precisará instalar as dependências do projeto. Use o seguinte comando para instalar:

   ```bash
   pip install google-generativeai python-dotenv

3. **Criar um arquivo .env** Deve ser criado um arquivo `.env` e preencher seu conteúdo com:

    ```env
    GENAI_API_KEY=<SUA_CHAVE_API_AQUI>

## Vídeo demonstrativo de uso

<iframe width="560" height="315" src="https://www.youtube.com/embed/RfAI58XsGUY?si=Axem7O5KNAKSFUNn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>