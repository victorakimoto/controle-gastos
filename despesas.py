from decimal import Decimal
import json

ARQUIVO = "despesas.json"

def carregar_despesas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return []
    for despesa in dados:
        despesa["valor"] = Decimal(despesa["valor"])

    return dados

def salvar_despesas():
    dados = []
    for despesa in despesas:
        copia = despesa.copy()
        copia["valor"] = str(copia["valor"])
        dados.append(copia)
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

despesas = [
    {
        'descricao': 'Mensalidade da Faculdade',
        'tipo': 'fixa',
        'categoria': 'Educação',
        'valor': Decimal('1350.00'),
        'data': '10/xx/xxxx',
        'forma_pagamento': 'Cartão de crédito'
    },
    {
        'descricao': 'Conta de Luz',
        'tipo': 'fixa',
        'categoria': 'Contas Fixas',
        'valor': Decimal('20.00'),
        'data': '20/xx/xxxx',
        'forma_pagamento': 'Cartão de crédito'
    }
]