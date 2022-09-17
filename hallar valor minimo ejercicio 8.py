#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Usuario
#
# Created:     17/09/2022
# Copyright:   (c) Usuario 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

numeros = [5,10,15,20]

def valor_menor(lista):
    menor = lista[0]

    for i in range(0, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

print(valor_menor(numeros))

if __name__ == '__main__':
    main()
