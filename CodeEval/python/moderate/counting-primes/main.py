# Code Eval- Counting Primes
# https://www.codeeval.com/open_challenges/63/

import sys

test_cases = open(sys.argv[1], 'r')

def isPrime(n):
    prime = True
    cont = n//2
    while(prime and cont>1):
        if n % cont == 0:
            prime = False
            break
        cont = cont - 1

    return prime
    

for test in test_cases:
    test=test.split(",")
    cont = 0
    for i in range(int(test[0]),int(test[1])+1):
        if isPrime(i):
            cont = cont + 1
    print (cont)
        
