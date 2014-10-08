def iterations_of_nan_expand(expanded):
    expanded = list(expanded.split())
    not_count = 0
    a_count = 0
    for word in expanded:
        if word == 'Not':
            not_count += 1
        elif word == 'a':
            a_count += 1
        elif word == 'NaN' and not_count == a_count and not_count > 0:
            return not_count
        else:
            return False