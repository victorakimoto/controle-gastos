# Importa a função que contém o loop principal do menu em menu.py
from menu import executar_menu
# O 'if' serve para garantir que esse código só rode nesse arquivo
# Executa diretamente dando um play no main.py
# Se o main.py fosse importado por outro arquivo no futuro, essa linha não executaria automaticamente
if __name__ == '__main__':
    executar_menu()