# Code Eval - minimum coins
# https://www.codeeval.com/open_challenges/74/

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test)
    coins = 0
    while test > 0:
        while test >= 5:
            test -= 5
            coins += 1
        while test >= 3:
            test -= 3
            coins += 1
        while test >= 1:
            coins += 1
            test -= 1
    print(coins)

test_cases.close()