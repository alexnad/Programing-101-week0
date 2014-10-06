def biggest_diffrence(arr):
    minimum = 0
    begin = 1
    for num1 in arr:
        for num2 in arr[begin:]:
            a,b = int(num1), int(num2)
            begin += 1
            if a - b < minimum or b - a < minimum:
                minimum = -abs(a - b)

    return minimum