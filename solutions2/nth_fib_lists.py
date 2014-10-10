def nth_fib_lists(listA, listB, n):
    for x in range(n-1):
        listB, listA = listA + listB, listB
    return listA
