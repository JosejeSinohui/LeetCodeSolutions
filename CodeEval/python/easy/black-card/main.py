# CodeEval Black Card
# https://www.codeeval.com/open_challenges/222/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    names = test.split("|")[0].split(" ")
    number = int(test.split("|")[1])-1
    del names[-1]

    while len(names)!=1:
        i = number
        if len(names)<=number:
            while(i>=len(names)):
                i = i-len(names)
            del names[i]
            continue

        del names[number]
    print(names[0])
