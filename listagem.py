from despesas import despesas

def listar_despesas():
    if not despesas:
        # Se a lista estiver vazia, avisa o usuário e encerra a função
        # Evita que o for imprima nada sem explicação
        print("Nenhuma despesa cadastrada.")
        return
    for despesa in despesas:
        # Monta a linha formatada com todos os campos da despesa separados em |
        print(f'{despesa["descricao"]} | {despesa["tipo"]} | {despesa["categoria"]} | '
              f'R$ {despesa["valor"]:.2f} | {despesa["data"]} | {despesa["forma_pagamento"]}')
