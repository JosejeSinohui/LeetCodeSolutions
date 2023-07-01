# CodeEval Penultimate Word
# https://www.codeeval.com/open_challenges/92/

import sys

test_cases = open(sys.argv[1], 'r') 

for test in test_cases:
    print(test.split(" ")[-2])#lol
