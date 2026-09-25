# Essas são as listas de opções pré-definidas para o usuário escolher
# Evita que o usuário digite livremente nessas opções
# Também evita que crie categorias diferentes para a mesma coisa (educação, Educação ou EDUCAÇÃO)

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
    # Essa é uma função reutilizável, que serve tanto para escolher categoria quanto forma de pagamento
    # recebendo qual lista usar (opcoes) e qual texto mostrar (mensagem)
    # Evita duplicar a lógica duas vezes em cadastro.py
    print(mensagem)
    # enumerate(opcoes, start=1) numera a lista a partir de 1
    # entregando o índice e o item juntos
    for indice, opcao in enumerate(opcoes, start=1):
        print(f"{indice} - {opcao}")

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            # Verifica se o número digitado está dentro do intervalo válido
            # Entre 1 e a quantidade de itens da lista
            if 1 <= escolha <= len(opcoes):
                # Converte de volta o número escolhido (base 1)
                # para o índice real da lista (base 0), e retorna o texto correspondente
                return opcoes[escolha - 1]

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas números válidos.")