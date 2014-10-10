def magic_square(matrix):
    transposed = list(map(list, zip(*matrix)))

    square_sum = sum(matrix[0])
    for row in matrix[1:]:
        if square_sum != sum(row):
            return False

    for column in transposed:
        if square_sum != sum(column):
            return False

    diagonal_sum = 0
    reversed_diagonal = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
        reversed_diagonal += list(reversed(matrix))[i][i]

    return reversed_diagonal == square_sum == diagonal_sum
