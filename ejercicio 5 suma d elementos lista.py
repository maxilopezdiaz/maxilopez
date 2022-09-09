#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Usuario
#
# Created:     07/09/2022
# Copyright:   (c) Usuario 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
listanumeros = [10,15,22]
def suma (lista):
    resultado = 0
    for listanumeros in lista:
        resultado += listanumeros
    return resultado

print(suma(listanumeros))

if __name__ == '__main__':
    main()
