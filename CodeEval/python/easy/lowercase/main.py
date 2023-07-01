# Code eval - lowercase
# https://www.codeeval.com/open_challenges/20/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print(test.lower())

test_cases.close()
