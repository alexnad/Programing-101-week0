def sum_matrix(m):
    sum_of_rows = 0
    for row in m:
        sum_of_rows += sum(row)

    return sum_of_rows
