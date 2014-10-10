def neighbours(matrix, element):
    pass


def bomb_rows(matrix, index):
    return matrix


def bomb_columns(matrix, index):
    return matrix


def matrix_sum(matrix):
    sum_rows = 0
    for row in matrix:
        sum_rows += sum(row)

    return sum_rows


def bomb_neigbours(matrix, index):
    matrix = bomb_rows(matrix, index)
    matrix = bomb_columns(matrix, index)

    return matrix


def matrix_bombing_plan(m):
    bombed_matrix = {}

    for i in range(len(m)):
        for j in range(len(m)):
            bombed_matrix[(i, j)] = matrix_sum(bomb_neigbours(m, (i, j)))

    return bombed_matrix

print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
