# CodeEval -Palindromic Ranges
# https://www.codeeval.com/open_challenges/47/


import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # Separa los numeros y creo el contador
    L = int(test.split(" ")[0])
    R = int(test.split(" ")[1])
    contGlobal = 0

    Right = R  # Crea Right para poder "reinicializarla" despues con su valor original

    while (L <= R):  # Recorre los valores por la izquierda de 1 en 1
        while (L <= Right):  # Recorre los de la derecha decreciendo en 1
            Palindrome = 0
            for i in range(L, Right + 1):  # itera sobre el subrango
                if str(i) == str(i)[::-1]:  # checa si es palindromo
                    Palindrome = Palindrome + 1
            if Palindrome % 2 == 0:  # checa si hay un numero par de palindromos
                contGlobal = contGlobal + 1
            Right = Right - 1
        L = L + 1
        Right = R

    print(contGlobal)  # Imprime el numero de rangos interesantes
