# Code Eval - Longes Lines
# https://www.codeeval.com/open_challenges/2/

import sys

test_cases = open(sys.argv[1], 'r')
test_cases1 = []
for test in test_cases:
    test_cases1.append(test)

test_cases1.append("1")  # chusco D:
First = True
for test in test_cases1:
    test = test.strip()
    if First:
        times = int(test)
        lines = []
        finished = ""
        First = False
        continue
    if test.isdigit():
        count = 0
        while count != times:
            longest = ""
            for line in lines:
                if len(line) > len(longest):
                    longest = line
            print(longest)
            lines.remove(longest)
            count = count + 1
        lines = []
        finished = ""
        times = int(test)
        continue
    lines.append(test)
