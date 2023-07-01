# Code Eval - Remove Characters
# https://www.codeeval.com/open_challenges/13/

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    string = list(test.split(", ")[0])
    characters = test.split(", ")[1].strip()

    for i in characters:
        while i in string:
            string.remove(i)
    print("".join(string))
