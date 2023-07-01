# Code Eval - Prime Numbers
# https://www.codeeval.com/open_challenges/46/

import sys

test_cases = open(sys.argv[1], 'r')


def isPrime(n):
    prime = True
    cont = 2
    while prime and cont < (n//2) + 1:
        if n % cont == 0:
            prime = False
            break
        cont = cont + 1
    return prime

for test in test_cases:
    finished = ""
    for i in range(2, int(test)):
        if isPrime(i):
            finished = finished + str(i)+","

    print(finished[:-1])
