# CodeEval String Mask
# https://www.codeeval.com/open_challenges/199/
# FIRST CHALLENGE!! 

import sys

test_cases = open(sys.argv[1], 'r') # < test cases!

for test in test_cases:
    Sep = test.split(' ')
    Palabra = ''
    for i in range(len(Sep[0])):
        Letra = Sep[0][i]
        if Sep[1][i] == '1':
            Palabra = Palabra + Letra.upper()
        else:
            Palabra = Palabra + Letra
    print(Palabra)

test_cases.close()
