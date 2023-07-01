# CodeEval Prime Palindrome
# https://www.codeeval.com/open_challenges/3/

def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
def isPrime(n):
    prime = True
    for i in range(n//2,1,-1):
        if n%i == 0:
            prime = False
            break
    return prime   
    
for i in range(1000, 0, -1):
    if isPalindrome(i) and isPrime(i):
        print(i)
        break
    
    
