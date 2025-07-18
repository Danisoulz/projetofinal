# 💼 Chatbot de Análise Salarial

Este projeto é uma API que funciona como um chatbot: ele recebe uma mensagem com o comando "carreira" e responde com uma análise de dados salariais. Os dados vêm de uma planilha online (Google Sheets em formato CSV).

---

## 🚀 O que este chatbot faz?

Quando você envia o comando `carreira`, ele:

- 📊 Calcula a média salarial por **profissão**
- 🧠 Encontra a **melhor profissão proporcional à experiência**
- 👥 Mostra a média salarial por **faixa etária**

---

## 📌 Como funciona?

1. Você roda o projeto com Python (veja abaixo como instalar).
2. A API fica disponível no endereço `http://127.0.0.1:5000/chat`.
3. Você envia uma requisição POST com o seguinte corpo JSON

---

## 📌 Como rodar o projeto?
Clone este repositório ou baixe os arquivos.
Instale o Python (versão 3.10 ou superior).
Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
venv\Scripts\activate      # no Windows

---

## Instale as dependências:
pip install -r requirements.txt

---

## Rode o servidor:
python main.py

---

🛠️ Tecnologias usadas
Python
Flask
CSV (planilhas simples exportadas do Google Sheets)

---

## 📄 Formato esperado da planilha
A planilha CSV deve ter colunas com esses nomes:
profissao
salario
experiencia (anos)
idade
Cada linha representa uma pessoa.

---

## ✨ Sobre este projeto
Este chatbot foi feito como prática de programação em Python com Flask e manipulação de dados com CSV.
Ele pode ser integrado com outros sistemas no futuro (como WhatsApp, Telegram ou sites).

---

## ✨ Autoria
Projeto desenvolvido por **Daniela**, como prática de programação em Python e automação de análise de dados com Flask.
Aula: EDUCAFROTech
🔗 GitHub:(https://github.com/Danisoulz)
