# Code eval - mersenne prime
# https://www.codeeval.com/open_challenges/240/

import sys

def isPrime(n):
    if n < 2:
        return False
    prime = True
    cont = n//2
    while(prime and cont>1):
        if n % cont == 0:
            prime = False
            break
        cont = cont - 1

    return prime

marsennePrimes = []
for i in range(1,13):
    if isPrime((2**i)-1):
        marsennePrimes.append((2**i)-1)



with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = int(test)
        result = []
        for i in marsennePrimes:
            if i < test:
                result.append(i)
        result = map(str, result)
        print(', '.join(result))

