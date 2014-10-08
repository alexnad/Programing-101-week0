def sort_fractions(fractions):
    b = [x/y for x, y in fractions]
    print(b)
    c = {key: value for key, value in zip(b, fractions)}

    new_fractions = []
    b.sort()
    for a in b:
        new_fractions.append(c[a])

    return new_fractions

print(sort_fractions([(2, 3), (1, 2)]))
print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
