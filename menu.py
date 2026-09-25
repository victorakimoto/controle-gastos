# Importa cada função das suas respectivas partes do programa
# Cada arquivo tem uma responsabilidade só
# Isso se chama separação de responsabilidades

from cadastro import cadastrar_despesa
from listagem import listar_despesas
from totalgasto import total_gasto
from totalcategoria import total_categoria
from excluirdespesa import excluir_despesa

def linha(tam = 42):
    # Função que gera uma linha de traços
    # parâmetro tam tem um valor padrão 42
    return '-' * tam

txt = 'MENU PRINCIPAL' # Texto fixo do título do menu

def cabecalho(txt):
    # Função que imprime uma linha decorativa, com o título recebido como parâmetro
    print(linha())
    print(txt)
    print(linha())

def menu():
    # Função que exibe as opções disponíveis para o usuário
    # Apenas mostra a lista
    print("1 - Cadastrar despesa")
    print("2 - Listar despesas")
    print("3 - Total gasto")
    print("4 - Total por categoria")
    print("5 - Excluir despesa")
    print("0 - Sair")
def executar_menu():
    # Essa é a função que roda o loop principal do programa, ela roda infinitamente até o usuário digitar 0 para sair
    while True:
        cabecalho(txt)
        menu()
        try:
            # Isso converte a entrada do usuário para um número inteiro
            # Caso o usuário digite uma letra o int() retorna o ValueError
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            # Esse 'continue' serve para pular o restante do loop e volta novamente para o início
            continue
        if opcao == 1:
            cadastrar_despesa()
        elif opcao == 2:
            listar_despesas()
        elif opcao == 3:
            # Essa função retorna um valor decimal, e aqui foi formatado para ter duas casas decimais
            print(f" Total gasto: R$ {total_gasto():.2f}")
        elif opcao == 4:
            # total_categoria() retorna um dicionário {categoria: total}
            totais = total_categoria()
            if not totais:
                # Se não tem despesas, então nenhuma despesa foi cadastrada
                print("Nenhuma despesa foi cadastrada.")
            else:
                # Esse .items() serve para percorrer o dicionário, retornando a chave e o valor juntos
                # Permite imprimir a categoria e seu respectivo total
                for categoria, valor in totais.items():
                    print(f" - {categoria}: R$ {valor:.2f}")
        elif opcao == 5:
            excluir_despesa()
        elif opcao == 0:
            print("Sair")
            # O break serve para interromper o while true, assim encerrando o programa
            break
        else:
            print("Essa opção é inválida. Tente novamente.")

