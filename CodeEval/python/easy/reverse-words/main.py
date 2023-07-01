# Code Eval Reverse Words
# https://www.codeeval.com/open_challenges/8/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.split(" ")
    test[-1] = test[-1].strip() #CodeEval gives a newline at the end
    print(" ".join(test[::-1]))
    
    

