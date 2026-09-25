from datetime import datetime
from decimal import Decimal, InvalidOperation
from despesas import despesas, salvar_despesas
from opcoes import CATEGORIAS, FORMAS_PAGAMENTO, escolher_opcao


def cadastrar_despesa():
    # .strip() serve para remover espaços em branco no início ou fim do texto
    descricao = input("Descrição: ").strip()
    # loop até o usuário digitar um tipo válido

    while True:
        tipo = input("Tipo (fixa/variável): ").strip().lower()

        # Aceita o usuário digitar variável sem acento e converte automaticamente
        if tipo == "variavel":
            tipo = "variável"
        # Apenas sai do loop quando um dos dois for aceito
        if tipo in ["fixa", "variável"]:
            break

        print("Escolha entre 'fixa' ou 'variável'.")
    # Delega a função reutilizável em opcoes.py,
    # que já mostra de vez a lista numerada e valida a escolha do usuário
    categoria = escolher_opcao(
        CATEGORIAS,
        "\nEscolha uma categoria:"
    )

    while True:
        try:
            # Esse .replace() serve para o usuário digitar livremente no formato "150,50"
            valor = Decimal(input("Valor: ").replace(",", "."))

            if valor <= 0:
                print("O valor deve ser maior que zero.")
                # Esse 'continue' volta para o início do while true
                # pedindo o valor de novo, sem sair da função
                continue

            break

        except (ValueError, InvalidOperation):
            # Levanta InvalidOperation para entradas inválidas
            print("Digite um valor válido.")

    while True:
        data = input("Data (DD/MM/YYYY): ").strip()

        try:
            # strptime tenta interpretar o texto digitado no formato especificado
            # Se o formato não bater ou dar uma data que não existe, chama o ValueError
            datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Digite no formato DD/MM/YYYY.")

    forma_pagamento = escolher_opcao(
        FORMAS_PAGAMENTO,
        "\nEscolha a forma de pagamento:"
    )
    # Monta um dicionário com todos os dados coletados
    # Estrutura usada em todo o resto do programa
    nova_despesa = {
        "descricao": descricao,
        "tipo": tipo,
        "categoria": categoria,
        "valor": valor,
        "data": data,
        "forma_pagamento": forma_pagamento,
    }

    despesas.append(nova_despesa)

    # Grava a lista imediatamente no arquivo JSON após o cadastro,
    # Para não perder a despesa caso o programa seja fechado
    salvar_despesas()

    print("\nDespesa cadastrada com sucesso.")