# Code Eval - Decimal to Binary
# https://www.codeeval.com/open_challenges/27/

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test)
    adjust = 1 #Este valor se multiplica por 10 en cada iteracion para "mover"
    binario = 0 #Valor inicial
    while test > 0:
        residuo = test % 2 
        binario = binario+(adjust*residuo)#Se le agrega el residuo * adjust, para que quede                                           en el lugar adecuado
        test = test // 2 #Test toma el valor de la division (sin el residuo)
        adjust = adjust*10
    print(binario)
test_cases.close()
