# Code Eval - swap elements
# https://www.codeeval.com/open_challenges/112/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split(" : ")
        array = test[0].split(" ")
        if len(test[1]) == 3:
            swapCases = [test[1]]
        else:
            swapCases = test[1].split(", ")

        for case in swapCases:
            case = case.split("-")
            array[int(case[0])], array[int(case[1])] = array[int(case[1])], array[int(case[0])]

        print(" ".join(array))
