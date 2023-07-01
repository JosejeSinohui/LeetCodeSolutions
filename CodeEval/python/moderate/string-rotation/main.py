# Code Eval - String rotation
# https://www.codeeval.com/open_challenges/76/

import sys

def rotate(str,n):
	return str[n:]+str[:n]

with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		test = test.strip()
		test = test.split(",")
		oracion = test[0]
		rotated = test[1]
		condition = False
		for i in range(0, len(oracion)):
			if rotated == rotate(oracion,i):
				condition = True
				break
		print(condition)
		


	test_cases.close()