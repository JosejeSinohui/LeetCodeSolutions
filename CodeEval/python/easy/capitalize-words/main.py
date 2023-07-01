# Code Eval
# https://www.codeeval.com/open_challenges/93/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.split(' ')
        for i in test:
            print(i[0].upper(), end="")
            print(i[1:], end=' ')


