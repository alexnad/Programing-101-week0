def is_decreasing(seq):
    previous_element = seq[0]
    for next_element in seq[1:]:
        if previous_element <= next_element:
            return False
        previous_element = next_element

    return True
