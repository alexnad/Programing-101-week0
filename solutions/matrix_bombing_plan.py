def valid_index(matrix, index, bomb_place):
    print(index[0] >= 0 and index[0] < len(matrix) and index[1] >= 0 \
        and index[1] < len(matrix) and index != bomb_place, index)
    return index[0] >= 0 and index[0] < len(matrix) and index[1] >= 0 \
        and index[1] < len(matrix) and index != bomb_place


def detonate(element, amount):
    if element <= amount:
            return 0
    return element - amount


def plant_bomb(matrix, index):
    bomb_damage = matrix[index[0]][index[1]]

    for i in range(index[0] - 1, index[0] + 2):
        for j in range(index[1] - 1, index[1] + 2):
            if valid_index(matrix, (i, j), index):
                matrix[i][j] = detonate(matrix[i][j], bomb_damage)

    return matrix


def matrix_sum(matrix):
    sum_rows = 0
    for row in matrix:
        sum_rows += sum(row)

    return sum_rows


def matrix_bombing_plan(m):
    bombed_matrix = {}

    for i in range(len(m)):
        for j in range(len(m)):
            bombed_matrix[(i, j)] = matrix_sum(plant_bomb(m, (i, j)))

    return bombed_matrix

print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
[123]
[456]
[789]
