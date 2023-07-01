# Code Eval - One Zero, Two Zeros...
# https://www.codeeval.com/open_challenges/217/

import sys

#from decimal to binary, returns string
def toBinary(n):
	binary = 0
	n = int(n)
	adjust = 1
	while(n>0):
		binary = binary + (n%2)*adjust
		n = n//2
		adjust = adjust * 10
	return str(binary)

#opens test cases
test_cases = open(sys.argv[1],'r')

for test in test_cases:
	test = test.strip()
	test = test.split(" ")
	zeros = int(test[0])
	count = test[1]
	test = []
	#Iterates over range of numbers and adds
	#their binary representation to "test"
	for i in range(1, int(count)+1):
		test.append(toBinary(i))
    
    #iterates over binary representations and counts
    #the number of zeros to see if they fit
	count = 0
	for case in test:
		case = list(case)
		if case.count("0") == zeros:
			count = count + 1
	print(count)

test_cases.close()

