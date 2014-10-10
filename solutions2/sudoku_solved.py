COMPLETE_ROW = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def square_to_row(square):
    new_row = []
    for row in square:
        for number in row:
            new_row.append(number)
    new_row.sort()
    return new_row


def squares_solved(squares):
    for square in squares:
        if not square_to_row(square) == COMPLETE_ROW:
            return False
    return True


def cut_check_squares(sudoku):
    squares = [[], [], []]

    for index, row in enumerate(sudoku):
        if index % 3 == 0 and index != 0:
            if not squares_solved(squares):
                return False
            squares = [[], [], []]

        squares[0].append(row[:3])
        squares[1].append(row[3:6])
        squares[2].append(row[6:])

    return True


def check_rows_columns(sudoku):
    transposed = list(map(list, zip(*sudoku)))

    for row, column in zip(sudoku, transposed):
        row.sort()
        column.sort()
        if row != column or row != COMPLETE_ROW:
            return False

    return True


def sudoku_solved(sudoku):
    return cut_check_squares(sudoku) and check_rows_columns(sudoku)
