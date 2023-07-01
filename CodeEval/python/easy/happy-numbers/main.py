# Code Eval - Happy numbers
# https://www.codeeval.com/open_challenges/39/

import sys

def squareSum(number):
    number = str(number)
    numbers = list(number)
    newNumber = 0
    for num in numbers:
        newNumber += int(num)**2
    return newNumber

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        pastnums = []
        done = False
        while not done:
            test = squareSum(test)
            if test in pastnums:
                print('0')
                done = True
            if test == 1:
                print('1')
                done = True
            pastnums.append(test)
