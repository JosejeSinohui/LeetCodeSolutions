# Code Eval - Swap numbers
# https://www.codeeval.com/open_challenges/196/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        words = test.strip().split(" ")
        for word in words:
            word = list(word)
            word[-1], word[0] = word[0], word[-1]
            print("".join(word),end = ' ')
        print("")
