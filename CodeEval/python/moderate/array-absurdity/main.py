# Code Eval - Array Absurdity
# https://www.codeeval.com/open_challenges/41/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split(";")
        test = test[1].split(",")
        for i in test:
            if test.count(i) == 2:
                print(i)
                break
