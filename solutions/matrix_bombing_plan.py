try:
    t=ar[5]
except IndexError:
    print 'sorry, no 5'  


def neighbours(matrix, element):
    try:
        t=ar[5]
    except IndexError:
        return False  


def bomb_rows(matrix, index):
    if index[0] < len(matrix) - 1:
        matrix[index[0] + 1][index[1]] -= matrix[index[0]][index[1]]
    if index[0] > 0:
        matrix[index[0] - 1][index[1]] -= matrix[index[0]][index[1]]

    for row in range(len(matrix)):
        if matrix[row][index[1]] < 0:
            matrix[row][index[1]] = 0

    return matrix
    
    start = [index[0] - 1, index[1] - 1]
    end = [index[0] + 1, index[1] + 1]
    if index[0] == 0:
        start[0] = 0
    if index[0] == len(matrix):
        end[0] = index[0]

    for i


def bomb_columns(matrix, index):
    if index[1] < len(matrix) - 1:
        matrix[index[0]][index[1] + 1] -= matrix[index[0]][index[1]]
    if index[1] > 0:
        matrix[index[0]][index[1] - 1] -= matrix[index[0]][index[1]]
    for column in range(len(matrix)):
        if matrix[index[0]][column] < 0:
            matrix[index[0]][column] = 0

    return matrix


def matrix_sum(matrix):
    sum = 0
    for row in matrix:
        for element in row:
            sum += element

    return sum


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
