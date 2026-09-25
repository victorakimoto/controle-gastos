CATEGORIAS = [
    "Educação",
    "Lazer",
    "Impostos",
    "Consumo",
    "Transporte",
    "Habitação",
    "Contas Fixas",
    "Alimentação"
]

FORMAS_PAGAMENTO = [
    "Dinheiro",
    "Cartão de crédito",
    "Cartão de débito",
    "PIX",
    "Boleto"
]


def escolher_opcao(opcoes, mensagem):
    print(mensagem)

    for indice, opcao in enumerate(opcoes, start=1):
        print(f"{indice} - {opcao}")

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))

            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas números válidos.")