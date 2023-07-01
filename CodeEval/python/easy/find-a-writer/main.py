# Code eval - find a writer
# https://www.codeeval.com/open_challenges/97/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        letters = list(test.split('|')[0])
        numbers = test.split('|')[1].split(' ')
        del numbers[0]
        finalSentence = ''    
        for i in numbers:
           finalSentence += letters[int(i)-1] 
        print(finalSentence)
