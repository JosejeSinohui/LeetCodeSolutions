# Code Eval - As quick as a flash
# https://www.codeeval.com/open_challenges/239/

import sys

def partition(list, low, high):
    global count
    count += 1
    border = low
    for i in range(low, high+1):
        if list[i] < list[low]:
            border += 1
            list[i], list[border] = list[border], list[i]
    list[low], list[border] = list[border], list[low]
    return border

def quickSort(A):
    quick_sort(A, 0, len(A)-1)

def quick_sort(list, low, high):
    if low < high:
        pivot = partition(list, low, high)
        quick_sort(list, low, pivot - 1)
        quick_sort(list, pivot + 1, high)


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        count = 0
        test = [int(i) for i in test.split(" ")]
        quickSort(test)
        print(count)
        print(test)
        count = 0
