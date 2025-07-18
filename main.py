from flask import Flask, request, jsonify
from analisador_carreira import processar_dados_carreira
# Cria uma aplicação Flask
app = Flask(__name__)

# Link da planilha CSV já publicado
LINK_PADRAO = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRlU4nbdalSzsbkpv9cSiCFy4HFlSNGPp9Oor_yYYMaolTZUNLRS7p3K7RLjvyt_Pt9YOU0RGAvI-N0/pub?output=csv"

# Cria a rota da API que responde ao comando do usuário
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensagem = data.get('mensagem', '').strip()
    
    # Verifica se a mensagem começa com "carreira" ou "4"
    if mensagem.lower().startswith("carreira") or mensagem.startswith("4"):
        partes = mensagem.split()

        # Se não foi passado um link, usa o link padrão
        if len(partes) < 2:
            url = LINK_PADRAO
        else:
            url = partes[1]

         # Chama a função que processa os dados da planilha
        resultado, erro = processar_dados_carreira(url)

        # Se deu erro ao processar, retorna a mensagem de erro
        if erro:
            return jsonify({"resposta": f"❌ Erro: {erro}"})
            
        # Se deu tudo certo, retorna o resultado
        return jsonify({"resposta": resultado})
    
    # Se a mensagem não for reconhecida, envia uma dica
    return jsonify({
        "resposta": (
            "❓ Comando não reconhecido.\n"
            "Use: carreira ou carreira <link_para_planilha_CSV>\n"
            f"Exemplo:\ncarreira {LINK_PADRAO}"
        )
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)



