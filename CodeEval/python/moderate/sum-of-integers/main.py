# Code Eval - sum of integers
# https://www.codeeval.com/open_challenges/17/
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = [int(i) for i in test.split(",")]
        greatest = -1000000
        R = len(test)
        L = 0
        while L <= R:
            while L <= R:
                sum = 0
                for i in range(L, R):
                    sum += test[i]

                if sum > greatest and sum != 0:
                    greatest = sum

                R -= 1
            L += 1
            R = len(test)
        if greatest == -1000000:
            print(0)
            continue
        print(greatest)
