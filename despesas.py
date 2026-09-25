from decimal import Decimal
import json
# Nome do arquivo onde as despesas são salvas permanentemente no disco
# Fica numa constante para facilitar caso o nome do arquivo precise mudar no futuro
# Só altera em um lugar ao em vez de vários pontos do código
ARQUIVO = "despesas.json"

def carregar_despesas():
    # Função que tenta abrir e ler o arquivo JSON com as despesas salvas de outras execuções
    try:
        # with open serve para abrir arquivos de forma segura para depois fechá-los automaticamente
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            # json.load() lê o conteúdo do arquivo e converte para estruturas do Python
            # Nesse caso, lista de dicionários
            dados = json.load(arquivo)
    except FileNotFoundError:
        # Caso não exista arquivo ainda, começa uma lista vazia em vez de quebrar o programa
        return []
    # Como o JSON não sabe representar valor decimal (ele salva como string)
    # Ao carregar de volta, é preciso converter manualmente cada valor
    # de string para decimal, para que os cálculos (soma, total por categoria)
    # continuem funcionando com precisão exata, sem erros de arredondamento com float
    for despesa in dados:
        despesa["valor"] = Decimal(despesa["valor"])

    return dados

def salvar_despesas():
    # Essa função monta uma nova lita para salvar,
    # porque o valor precisa ser convertido para string para fins de gravação em JSON
    # O restante do programa ainda precisa do valor decimal para os cálculos
    dados = []
    for despesa in despesas:
        # .copy() cria uma cópia independente do dicionário.
        # Sem isso, a conversão abaixo alteraria o dicionário original na lista "despesas" em memória,
        # quebrando os cálculos de total (que esperam por um decimal, e não uma string)
        copia = despesa.copy()
        copia["valor"] = str(copia["valor"])
        dados.append(copia)
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        # ensure_ascii=False preserva os acentos corretamente no arquivo
        # indent=4 serve para formatar o arquivo e deixar legível
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
# Ao importar este módulo pela primeira vez, a lista "despesas" já é carregada
# automaticamente a partir do arquivo salvo
# assim, o programa inteiro trabalha com dados mais recentes
despesas = carregar_despesas()

