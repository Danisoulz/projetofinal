# 🤖 Chatbot de Análise Salarial

Este é um pequeno chatbot criado com Python e Flask que faz uma análise simples de dados salariais a partir de uma planilha CSV hospedada online.

## 🚀 Como funciona?

Você envia uma mensagem para o bot com o comando `carreira`, e ele responde com uma análise baseada nos dados de uma planilha. Essa análise inclui:

- Média salarial por profissão
- Profissão com melhor salário proporcional à experiência
- Média salarial por faixa etária

## 🎯 Objetivo
Oferecer uma solução acessível para consulta de médias salariais por área de atuação, utilizando tecnologias leves e de fácil implantação.

## 🌍 Público-alvo
Estudantes, profissionais em transição de carreira, analistas de RH e demais interessados em comparar faixas salariais com base em dados reais.

## 📥 Como usar

1. **Inicie o servidor Flask** rodando o arquivo `main.py`.
2. **Envie uma requisição POST** para o endpoint:

## POST http://127.0.0.1:5000/chat

## 🛠 Tecnologias usadas
Python 3
Flask
Postman (para testar)
Google Sheets

## 📄 Requisitos
Instale as dependências com:
nginx
Copy
Edit
pip install -r requirements.txt


## 📊 Fonte dos dados
Você pode usar uma planilha personalizada. O formato esperado é:
Colunas: profissao, salario, experiencia (anos), idade

## 👤 Autoria

Desenvolvido por [@Danisoulz](https://github.com/Danisoulz) como parte do projeto final da EDUCAFROTech.
⭐ Se esse projeto te interessou, considere deixar uma estrela.