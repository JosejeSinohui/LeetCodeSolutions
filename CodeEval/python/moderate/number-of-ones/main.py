#Code Eval - Number of Ones
#https://www.codeeval.com/open_challenges/16/

import sys

def toBinary(n):
    n = int(n)
    adjust = 1 #Este valor se multiplica por 10 en cada iteracion para "mover"
    binary = 0 #Valor inicial
    while n > 0:
        residuo = n % 2 
        binary = binary + (adjust * residuo)#Se le agrega el residuo * adjust, para que quede en el lugar adecuado
        n = n // 2 #Test toma el valor de la division (sin el residuo)
        adjust = adjust*10
    return(str(binary))

test_cases = open(sys.argv[1],'r')

for test in test_cases:
	test = toBinary(test)
	ones = 0
	for i in test:
		if i == "1":
			ones = ones +1

	print(ones)

test_cases.close()
