from nth_fib_lists import nth_fib_list


def member_of_nth_fib_lists(listA, listB, needle):
    case_1 = nth_fib_list(listA, listB, 3) == needle
    case_2 = nth_fib_list(listA, listB, 4) == needle
    return case_1 or case_2
