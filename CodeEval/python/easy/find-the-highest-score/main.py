# Code Eval - Find the Highest Score
# https://www.codeeval.com/open_challenges/208/

import sys

def deleteWhite(list):
    while '' in list:
        list.remove('')

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip().split("|")
    rows = []
    for i in range(len(test)):
        numbers = test[i].split(' ')
        deleteWhite(numbers)
        rows.append(numbers)

    rowsLength = len(rows)
    columnsLenght = len(rows[1])
    maxValues = []

    for i in range(len(rows[1])):
        columnValues = []
        for j in range(len(rows)):
            columnValues.append(int(rows[j][i]))
        maxValues.append(str(max(columnValues)))
    print(" ".join(maxValues))

test_cases.close()
