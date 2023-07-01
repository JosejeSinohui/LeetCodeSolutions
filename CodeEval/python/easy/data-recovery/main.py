# CodeEval -DataRecovery
# https://www.codeeval.com/open_challenges/140/

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # inicializa oracion
    oracion = ""

    # separa la oracion de los numeros
    test = test.split(";")

    # separa las palabras de la oracion"
    palabras = test[0].split(" ")

    # separa los numeros de la oracion
    # remueve newline del ultimo elemento (CodeEval los manda asi)
    numeros = test[1].split(" ")
    numeros[-1] = numeros[-1].strip()

    # genera la oracion
    for i in range(len(palabras)):
        if str(i + 1) in numeros:
            palabra = palabras[numeros.index(str(i + 1))]
        else:
            palabra = palabras[-1]
        oracion = oracion + palabra + " "

    print(oracion)
