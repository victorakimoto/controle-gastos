[README.md](https://github.com/user-attachments/files/32670734/README.md)
# Controle de Gastos Pessoais

Programa em Python, executado via terminal, para registrar despesas pessoais e consultar quanto foi gasto no total ou por categoria. Os dados são salvos localmente em um arquivo JSON, permanecendo disponíveis entre execuções do programa.

## Funcionalidades

- Cadastrar despesa (descrição, tipo, categoria, valor, data e forma de pagamento)
- Listar todas as despesas cadastradas
- Calcular o total gasto
- Calcular o total gasto por categoria
- Excluir uma despesa
- Persistência automática dos dados em arquivo JSON

## Exemplo do menu

```
------------------------------------------
MENU PRINCIPAL
------------------------------------------
1 - Cadastrar despesa
2 - Listar despesas
3 - Total gasto
4 - Total por categoria
5 - Excluir despesa
0 - Sair
```

## Tecnologias e recursos utilizados

- **Python 3** (sem bibliotecas externas — apenas módulos padrão)
- `decimal.Decimal` — para cálculos monetários com precisão exata, evitando os erros de arredondamento comuns ao usar `float`
- `datetime` — para validar o formato das datas informadas
- `json` — para persistir as despesas em disco entre execuções
- Git e GitHub — controle de versão

## Estrutura do projeto

```
.
├── main.py            # Ponto de entrada do programa
├── menu.py             # Loop principal e exibição do menu
├── cadastro.py          # Cadastro de novas despesas, com validações
├── listagem.py          # Exibição de todas as despesas cadastradas
├── totalgasto.py         # Cálculo do total gasto
├── totalcategoria.py       # Cálculo do total gasto por categoria
├── excluirdespesa.py       # Exclusão de uma despesa existente
├── opcoes.py            # Listas de categorias/formas de pagamento e seleção numerada
├── despesas.py           # Estrutura de dados em memória + persistência em JSON
├── despesas.json          # Dados salvos (gerado automaticamente, ignorado pelo Git)
└── .gitignore
```

## Como executar

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   ```
2. Acesse a pasta do projeto:
   ```
   cd controle-gastos
   ```
3. Execute o programa (requer Python 3 instalado):
   ```
   python main.py
   ```

Não há dependências externas a instalar — o projeto usa apenas a biblioteca padrão do Python.

## Categorias e formas de pagamento disponíveis

**Categorias:** Educação, Lazer, Impostos, Consumo, Transporte, Habitação, Contas Fixas, Alimentação

**Formas de pagamento:** Dinheiro, Cartão de crédito, Cartão de débito, PIX, Boleto

Essas listas ficam centralizadas em `opcoes.py` e podem ser editadas diretamente no código para adicionar novas opções.

## Decisões técnicas

- **`Decimal` em vez de `float`**: valores monetários exigem precisão exata; `float` pode introduzir pequenos erros de arredondamento em operações repetidas, o que é inaceitável ao lidar com dinheiro.
- **Persistência em JSON**: como `Decimal` não é serializável nativamente em JSON, os valores são convertidos para `string` ao salvar e reconvertidos para `Decimal` ao carregar.
- **Separação em módulos**: cada funcionalidade (cadastro, listagem, exclusão, totais) fica em seu próprio arquivo, facilitando manutenção e leitura do código.
- **Dados sensíveis fora do controle de versão**: o arquivo `despesas.json`, por conter informações financeiras reais do usuário, está listado no `.gitignore` e não é versionado.

## Possíveis melhorias futuras

- Migrar a estrutura de dicionários para classes (Programação Orientada a Objetos)
- Substituir o armazenamento em JSON por um banco de dados (ex.: SQLite)
- Adicionar testes automatizados com `pytest`
- Permitir consulta de despesas por período (data inicial/final)
- Interface gráfica (desktop ou web)

## Autor

Desenvolvido como projeto de prática de lógica de programação, estruturas de dados e manipulação de arquivos em Python.
