from number_to_list import number_to_list
from list_to_number import list_to_number


def zero_insert(n):
    a = number_to_list(n)
    new_numbers = [a[0]]
    previous_num = a[0]
    
    for next_num in a[1:]:
        if previous_num == next_num or previous_num + next_num == 10:
            new_numbers.append(0)
        previous_num = next_num
        new_numbers.append(previous_num)

    return list_to_number(new_numbers)
