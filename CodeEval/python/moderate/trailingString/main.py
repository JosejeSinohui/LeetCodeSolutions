# Code Eval - Trailing String
# https://www.codeeval.com/open_challenges/32/

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if test.split(",")[0].endswith(test.split(",")[1]):
        print(1)
    else:
        print(0)
# lol
test_cases.close()
