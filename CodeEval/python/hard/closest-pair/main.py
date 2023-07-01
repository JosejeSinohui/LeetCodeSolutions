#Code Eval - Closest Pair
#https://www.codeeval.com/open_challenges/51/

import sys

test_cases = open(sys.argv[1], 'r')

def distance(a, b):
    x1 = int(a[0])
    y1 = int(a[1])
    x2 = int(b[0])
    y2 = int(b[1])

    return ((x2-x1)**(2)+(y2-y1)**(2))**(.5)

first = True 
for test in test_cases:
    
    #Si es 0 se acaba el programa
    if test == 0:
        break
    
    #OBTENER EL PNUMERO DE COORDENADAS EN Coords
    if first:
        coords = int(test)
        first = False
        cont = 0;
        coordenadas = []
        continue 

    # Contador, y creacion del arreglo
    cont = cont + 1
    test = test.split(" ")
    test[-1] = test[-1].strip()
    coordenadas.append(test)
    
    #Itera sobre el arreglo usando la funcion distance
    if cont == coords:
        first = True
        shortest = 10000;
        for i in range(len(coordenadas)):
            for j in range(i+1,len(coordenadas)):
                if distance(coordenadas[i],coordenadas[j]) < shortest:
                    shortest = distance(coordenadas[i],coordenadas[j])


        if shortest >= 10000:
            print("INFINITY")
            
        else:
            print("%.4f" % shortest)
