def sevens_in_a_row(arr, n):
    repetition = 0
    for number in arr:
        if number == 7:
            repetition += 1
        else:
            repetition = 0
        if repetition == n:
            return True
    return False
