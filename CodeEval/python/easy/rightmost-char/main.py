# Code Eval - Rightmost Char
# https://www.codeeval.com/open_challenges/31/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    string = test.split(",")[0]
    letter = test.split(",")[1]

    rightmost = -1
    for index, currentLetter in enumerate(string):
        if currentLetter == letter:
            rightmost = index
    print(rightmost)


test_cases.close()
