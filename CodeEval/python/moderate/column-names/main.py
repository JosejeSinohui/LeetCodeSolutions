# Code Eval - Column Names
# https://www.codeeval.com/open_challenges/197/

import sys

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = int(test)
        number = test
        times = 0
        times1 = 0
        while test > 26:
            test -= 26
            times += 1
            if times == 26:
                times1 += 1
                times = 0
            if times1 == 26:
                break

        if number <= 26:
            print(abc[test - 1])
        elif (26 <= number <= 702):
            print(abc[times-1] + abc[test-1])
        else:
            print(abc[times1-1] + abc[times-1] + abc[test-1])
