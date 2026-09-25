from despesas import despesas, salvar_despesas


def excluir_despesa():
    if not despesas:
        # Se não há despesas, não há o que excluir
        print("Nenhuma despesa cadastrada.")
        return
    # Mostra a lista numerada começando em 1 para o usuário escolher visualmente
    # qual despesa quer remover sem precisar saber o índice interno da lista
    for indice, despesa in enumerate(despesas, start=1):
        print(f"{indice} - {despesa['descricao']} | R$ {despesa['valor']:.2f}")
    try:
        numero = int(input("Digite o número da despesa que você quer excluir: "))
    except ValueError:
        print("Digite apenas números válidos.")
        return
    # Garante que o número digitado seja um número real da lista exibida
    if numero < 1 or numero > len(despesas):
        print("Número inválido.")
        return
    # Converte o número mostrado ao usuário (1) para o índice real em Python (0)
    indice = numero - 1
    # .pop() remove o item da lista e retorna o item removido
    # permite usar seus dados na mensagem de confirmação abaixo
    despesa_excluida = despesas.pop(indice)
    # Persiste a exclusão no arquivo para que ela não volte na próxima vez que o programa seja executado
    salvar_despesas()

    print(
        f"Despesa: '{despesa_excluida['descricao']}'"
        f" no valor de R$ {despesa_excluida['valor']:.2f}"
        " foi excluída com sucesso."
    )