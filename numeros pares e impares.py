#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      Usuario
#
# Created:     18/09/2022
# Copyright:   (c) Usuario 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

numeros = [18, 24, 33, 66, 57, 203, 1]

def separar(num):
    lista = sorted(num)
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return pares, impares

pares, impares = separar(numeros)
print(pares)
print(impares)

if __name__ == '__main__':
    main()
