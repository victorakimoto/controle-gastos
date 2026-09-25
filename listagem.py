from despesas import despesas

def listar_despesas():
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return
    for despesa in despesas:
        print(f'{despesa["descricao"]} | {despesa["tipo"]} | {despesa["categoria"]} | '
              f'R$ {despesa["valor"]:.2f} | {despesa["data"]} | {despesa["forma_pagamento"]}')
