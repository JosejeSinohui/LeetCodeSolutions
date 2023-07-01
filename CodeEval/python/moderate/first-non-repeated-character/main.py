# Code Eval - First non-repeated characters
# https://www.codeeval.com/open_challenges/12/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    letters = list(test)

    for letter in letters:
        if letters.count(letter) == 1:
            print(letter)
            break

test_cases.close()

