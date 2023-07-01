# Code Eval - number pairs
# https://www.codeeval.com/open_challenges/34/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    sum = test.split(";")[1]
    numbers = test.split(";")[0].split(",")
    finished = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if int(numbers[i]) + int(numbers[j]) == int(sum):
                finished.append(numbers[i] + "," + numbers[j])

    if finished == []:
        print("NULL")
    else:
        print(";".join(finished))
