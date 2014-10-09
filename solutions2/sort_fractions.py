def sort_fractions(fractions):
    b = [x/y for x, y in fractions]
    c = {key: value for key, value in zip(b, fractions)}

    return [c[value] for value in b.sort()]
