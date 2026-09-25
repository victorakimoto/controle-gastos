from despesas import despesas


def total_categoria():
    # O dicionário vazio vai acumular o total de cada categoria
    # no formato {categoria: total_gasto_nela}
    total = {}

    for despesa in despesas:
        categoria = despesa['categoria']
        valor = despesa['valor']
        # .get(categoria, 0) busca o total já acumulado para essa categoria
        # Caso a categoria não exista no dicionário retorna um 0 como valor padrão
        # Depois soma a despesa atual e guarda de volta na mesma chave
        total[categoria] = total.get(categoria, 0) + valor
    return total
