# Code eval - jolly jumpers
# https://www.codeeval.com/open_challenges/43/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = [int(i) for i in test.split(" ")]
    values = []
    for i in range(len(test)-1):
        values.append(abs(test[i]-test[i+1]))

    Jolly = True
    for i in range(1,len(test)-1):
        if i not in values:
            Jolly = False
            break

    if Jolly:
        print("Jolly")
    else:
        print("Not jolly")




