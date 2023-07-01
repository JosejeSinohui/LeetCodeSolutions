# CodeEval Reverse and Add
# https://www.codeeval.com/open_challenges/45/

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test)
    i = 0;
    while(True):
        backwardsTest = str(test)[::-1]
        if str(test) == backwardsTest:
            break;
        test = test + int(backwardsTest)
        i = i + 1

    print(str(i) + " " + str(test))

test_cases.close()

