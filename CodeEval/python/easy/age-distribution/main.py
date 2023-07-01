# Code Eval - Age Distribution
# https://www.codeeval.com/open_challenges/152

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = int(test)

        if 100 >= test >= 66:
            print('The Golden Years')
        elif 65 >= test >= 23:
            print('Working for the man')
        elif 22 >= test >= 19:
            print('College')
        elif 18 >= test >= 15:
            print('High school')
        elif 14 >= test >= 12:
            print('Middle school')
        elif 11 >= test >= 5:
            print('Elementary school')
        elif 4 >= test >= 3:
            print('Preschool maniac')
        else:
            print('Still in Mama\'s arms')
