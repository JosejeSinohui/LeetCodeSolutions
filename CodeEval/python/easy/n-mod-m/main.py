# Code eval - N mod M without modulus operator
# https://www.codeeval.com/open_challenges/62/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.split(",")
    number = int(test[0])
    divisor = int(test[1])
    print(number - (number//divisor)*divisor)

test_cases.close()