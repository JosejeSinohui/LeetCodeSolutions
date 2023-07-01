# Code eval - self describing numbers
# https://www.codeeval.com/open_challenges/40/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    selfDescribing = True
    for index, number in enumerate(test):
        if  test.count(str(index)) != int(number):
            selfDescribing = False
    if selfDescribing:
        print(1)
    else:
        print(0)