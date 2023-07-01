# Code Eval - Reverse Groups
# https://www.codeeval.com/open_challenges/71/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    array = test.split(";")[0].split(",")
    times = int(test.split(";")[1])
    temp = []
    j = times
    for i in range(0,len(array),times):
        interval = array[i:j]
        if times > len(interval):
            temp.append(interval)
            continue
        interval.reverse()
        temp.append(interval)
        j+=times

    finished = []
    for i in temp:
        for j in i:
            finished.append(j)
    print(",".join(finished))
test_cases.close()
