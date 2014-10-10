def magic_square(matrix):
    transponed = list(map(list, zip(*matrix)))

    sum_rows = 0
    for rows in matrix:
        for number in rows