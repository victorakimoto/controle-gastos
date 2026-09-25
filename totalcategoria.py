from despesas import despesas


def total_categoria():
    total = {}

    for despesa in despesas:
        categoria = despesa['categoria']
        valor = despesa['valor']

        total[categoria] = total.get(categoria, 0) + valor
    return total
