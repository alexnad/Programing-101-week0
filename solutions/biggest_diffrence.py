def biggest_difference(arr):
    minimum = 0
    begin = 1
    for num1 in arr:
        a = int(num1)
        for num2 in arr[begin:]:
            a = int(num2)
            begin += 1
            if a - b < minimum or b - a < minimum:
                minimum = -abs(a - b)

    return minimum
