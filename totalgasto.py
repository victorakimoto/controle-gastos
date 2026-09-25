from despesas import despesas


def total_gasto():
    # O sum() soma todos os valores gerados pela expressão dentro dos parênteses
    # 'despesa['valor'] for despesa in despesas' é um generator expression
    # Percorre cada despesa da lista e extrai só o campo 'valor'
    return sum(despesa['valor'] for despesa in despesas)