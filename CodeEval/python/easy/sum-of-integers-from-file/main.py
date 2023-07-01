# Code Eval - Sum of Integers from File
# https://www.codeeval.com/open_challenges/24/

import sys

suma = 0
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = int(test)
        suma = suma + int(test)
    print (suma)
