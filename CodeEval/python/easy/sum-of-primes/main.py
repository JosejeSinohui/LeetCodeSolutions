#codeEval- Sum of Primes
#https://www.codeeval.com/open_challenges/4/

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

contador = 0
num = 0
suma = 0
while(contador<1000):
    if isPrime(num):
        contador = contador + 1
        suma = suma + num
    num = num + 1
print(suma)    
