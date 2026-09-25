from despesas import despesas, salvar_despesas


def excluir_despesa():
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return
    for indice, despesa in enumerate(despesas, start=1):
        print(f"{indice} - {despesa['descricao']} | R$ {despesa['valor']:.2f}")
    try:
        numero = int(input("Digite o número da despesa que você quer excluir: "))
    except ValueError:
        print("Digite apenas números válidos.")
        return
    if numero < 1 or numero > len(despesas):
        print("Número inválido.")
        return
    indice = numero - 1
    despesa_excluida = despesas.pop(indice)
    salvar_despesas()

    print(
        f"Despesa: '{despesa_excluida['descricao']}'"
        f" no valor de R$ {despesa_excluida['valor']:.2f}"
        " foi excluída com sucesso."
    )