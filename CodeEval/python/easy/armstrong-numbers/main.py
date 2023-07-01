# Code Eval - Armstrong numbers
# https://www.codeeval.com/open_challenges/82/

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    power = int(len(test))

    sum = 0
    for i in test:
        sum +=int(i)**power

    if sum == int(test):
        print(True)
    else:
        print(False)

test_cases.close()
