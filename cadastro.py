from datetime import datetime
from decimal import Decimal, InvalidOperation
from despesas import despesas, salvar_despesas
from opcoes import CATEGORIAS, FORMAS_PAGAMENTO, escolher_opcao


def cadastrar_despesa():
    descricao = input("Descrição: ").strip()

    while True:
        tipo = input("Tipo (fixa/variável): ").strip().lower()

        if tipo == "variavel":
            tipo = "variável"

        if tipo in ["fixa", "variável"]:
            break

        print("Escolha entre 'fixa' ou 'variável'.")

    categoria = escolher_opcao(
        CATEGORIAS,
        "\nEscolha uma categoria:"
    )

    while True:
        try:
            valor = Decimal(input("Valor: ").replace(",", "."))

            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue

            break

        except (ValueError, InvalidOperation):
            print("Digite um valor válido.")

    while True:
        data = input("Data (DD/MM/YYYY): ").strip()

        try:
            datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Digite no formato DD/MM/YYYY.")

    forma_pagamento = escolher_opcao(
        FORMAS_PAGAMENTO,
        "\nEscolha a forma de pagamento:"
    )

    nova_despesa = {
        "descricao": descricao,
        "tipo": tipo,
        "categoria": categoria,
        "valor": valor,
        "data": data,
        "forma_pagamento": forma_pagamento,
    }

    despesas.append(nova_despesa)

    print("\nDespesa cadastrada com sucesso.")