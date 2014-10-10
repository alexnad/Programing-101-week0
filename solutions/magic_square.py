

def magic_square(matrix):
    transponed = list(map(list, zip(*matrix)))

    square_sum = sum(matrix[0])
    for rows in matrix:
        if sum != sum_of_rows:
            return False