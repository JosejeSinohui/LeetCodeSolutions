# CodeEval - Set Intersection
# https://www.codeeval.com/open_challenges/30/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()

        list1 = test.split(";")[0].split(",")
        list2 = test.split(";")[1].split(",")

        result = []

        for i in list1:
            for j in list2:
                if i == j:
                    result.append(i)

        print(','.join(result))
