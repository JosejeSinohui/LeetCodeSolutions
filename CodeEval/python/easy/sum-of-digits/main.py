# code eval - Sum of digits
# https://www.codeeval.com/open_challenges/21/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        sum = 0
        for i in list(test.strip()):
            sum += int(i)

        print(sum)
