import urllib.request
import csv
import io

# Baixa o conteúdo do CSV da internet
def baixar_csv(url):
    try:
        with urllib.request.urlopen(url) as resposta:
            conteudo = resposta.read().decode('utf-8')
        return conteudo
    except Exception as e:
        return None

# Converte o CSV para uma lista de dicionários (parecido com JSON)
def transformar_em_lista_dicionarios(conteudo_csv):
    arquivo = io.StringIO(conteudo_csv)
    leitor = csv.reader(arquivo)
    dados = []
    cabecalhos = []

    for i, linha in enumerate(leitor):
        if i == 0:
            cabecalhos = linha  # A primeira linha são os nomes das colunas
        else:
            if len(linha) == len(cabecalhos):
                item = {cabecalhos[i]: linha[i] for i in range(len(cabecalhos))}
                dados.append(item)

    return dados

# Calcula a média salarial de cada profissão
def media_por_profissao(dados):
    estatisticas = {}
    for linha in dados:
        profissao = linha.get('profissao')
        try:
            salario = float(linha.get('salario', 0))
        except:
            continue # Se não conseguir transformar em número, ignora
        if not profissao:
            continue
        if profissao not in estatisticas:
            estatisticas[profissao] = {'soma_salario': 0, 'quantidade': 0}
        estatisticas[profissao]['soma_salario'] += salario
        estatisticas[profissao]['quantidade'] += 1

    for profissao in estatisticas:
        soma = estatisticas[profissao]['soma_salario']
        qtd = estatisticas[profissao]['quantidade']
        estatisticas[profissao]['media'] = soma / qtd

    return estatisticas

# Identifica a profissão com melhor salário por ano de experiência
def melhor_por_experiencia(dados):
    melhor_profissao = None
    melhor_valor = 0
    for linha in dados:
        try:
            salario = float(linha.get('salario', 0))
            experiencia = float(linha.get('experiencia (anos)', 0))
            if experiencia > 0:
                valor = salario / experiencia
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_profissao = linha.get('profissao')
        except:
            continue
    return melhor_profissao, melhor_valor

# Calcula a média salarial por faixa etária
def media_por_faixa_etaria(dados):
    faixas = {
        '20-30': {'quantidade': 0, 'soma_salario': 0},
        '31-40': {'quantidade': 0, 'soma_salario': 0},
        '41+': {'quantidade': 0, 'soma_salario': 0},
    }

    for linha in dados:
        try:
            idade = int(linha.get('idade', 0))
            salario = float(linha.get('salario', 0))
        except:
            continue

        if 20 <= idade <= 30:
            faixa = '20-30'
        elif 31 <= idade <= 40:
            faixa = '31-40'
        elif idade >= 41:
            faixa = '41+'
        else:
            continue

        faixas[faixa]['quantidade'] += 1
        faixas[faixa]['soma_salario'] += salario

    for faixa in faixas:
        qtd = faixas[faixa]['quantidade']
        if qtd > 0:
            faixas[faixa]['media'] = faixas[faixa]['soma_salario'] / qtd
        else:
            faixas[faixa]['media'] = 0

    return faixas

# Junta todas as análises e monta a resposta final
def processar_dados_carreira(url_planilha):
    conteudo_csv = baixar_csv(url_planilha)
    if not conteudo_csv:
        return None, "Erro ao baixar a planilha."

    dados = transformar_em_lista_dicionarios(conteudo_csv)
    if not dados:
        return None, "Nenhum dado encontrado na planilha."

    estatisticas = media_por_profissao(dados)
    melhor_prof, melhor_valor = melhor_por_experiencia(dados)
    faixas = media_por_faixa_etaria(dados)

    resposta = ["📊 *Análise de Perfil Salarial:*\n"]

    resposta.append("💼 Média salarial por profissao:")
    for prof, info in estatisticas.items():
        resposta.append(f"- {prof}: R$ {info['media']:.2f}")

    if melhor_prof:
        resposta.append(f"\n🏅 Melhor profissão por experiência:\n- {melhor_prof}: R$ {melhor_valor:.2f} por ano")

    resposta.append("\n👥 Média por faixa etária:")
    for faixa, info in faixas.items():
        resposta.append(f"- {faixa}: R$ {info['media']:.2f}")

    return "\n".join(resposta), None
