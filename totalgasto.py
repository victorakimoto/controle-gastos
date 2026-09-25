from despesas import despesas


def total_gasto():
    return sum(despesa['valor'] for despesa in despesas)