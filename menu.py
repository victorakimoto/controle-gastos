from cadastro import cadastrar_despesa
from listagem import listar_despesas
from totalgasto import total_gasto
from totalcategoria import total_categoria
from excluirdespesa import excluir_despesa

def linha(tam = 42):
    return '-' * tam

txt = 'MENU PRINCIPAL'

def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())

def menu():
    print("1 - Cadastrar despesa")
    print("2 - Listar despesas")
    print("3 - Total gasto")
    print("4 - Total por categoria")
    print("5 - Excluir despesa")
    print("0 - Sair")
def executar_menu():
    while True:
        cabecalho(txt)
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            continue
        if opcao == 1:
            cadastrar_despesa()
        elif opcao == 2:
            listar_despesas()
        elif opcao == 3:
            print(f" Total gasto: R$ {total_gasto():.2f}")
        elif opcao == 4:
            totais = total_categoria()
            if not totais:
                print("Nenhuma despesa foi cadastrada.")
            else:
                for categoria, valor in totais.items():
                    print(f" - {categoria}: R$ {valor:.2f}")
        elif opcao == 5:
            excluir_despesa()
        elif opcao == 0:
            print("Sair")
            break
        else:
            print("Essa opção é inválida. Tente novamente.")

