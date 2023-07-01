# Code Eval Stepwise Word
# https://www.codeeval.com/open_challenges/202/
 
import sys

test_cases = open(sys.argv[1],'r')

for test in test_cases:
	test = test.strip()
	test = test.split(" ")
	longest = ""
	for word in test:
		if len(word)>len(longest):
			longest = word

	for i in range(len(longest)):
		print(i*"*"+longest[i]+" ",end="")
	print("")

