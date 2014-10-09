def nth_fib_list(listA, listB, n):
    for x in range(n-1):
        listB, listA = listA + listB, listB
    return listA
