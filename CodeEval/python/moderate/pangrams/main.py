# Code Eval - pangrams
# https://www.codeeval.com/open_challenges/37/

import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.lower()
        missing = []
        for letter in alphabet:
            if letter not in test:
                missing.append(letter)

        if not missing:
            print("NULL")
        else:
            print("".join(missing))