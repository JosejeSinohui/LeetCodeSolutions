# Code Eval - Flavius Josephus
# https://www.codeeval.com/open_challenges/75/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip().split(",")
    people = list(range(int(test[0])))
    kill = int(test[1])

    order = []
    step = kill - 1
    dels = 0
    while len(people) > 0:
        while step >= len(people):
            step -= len(people)
        order.append(str(people[step]))
        del people[step]
        step += kill - 1
    print(" ".join(order))

test_cases.close()
