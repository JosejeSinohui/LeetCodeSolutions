# Code Eval - Compressed Sequence
# https://www.codeeval.com/open_challenges/128/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        test = test.split(" ")
        test.append("nomasparaqueelfordeotravueltajeje")
        result = []
        times = 0
        first = True
        for j, i in enumerate(test):
            if first:
                currentchar = i
                first = False
            if currentchar == i:
                times += 1
            if currentchar != i or j == len(test)-1:
                result.append(times)
                result.append(currentchar)
                currentchar = i
                times = 1

        result = map(str, result)
        print(" ".join(result))
