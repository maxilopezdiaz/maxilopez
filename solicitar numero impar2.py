#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Usuario
#
# Created:     30/08/2022
# Copyright:   (c) Usuario 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    numero = int(input("ingrese un numero impar "))
    while numero % 2 == 0:
        numero = int(input("ingrese un numero impar "))
    if numero % 2 == 0:
        print ("el nuemro es par")
    else:
        print ("el numero es impar")

if __name__ == '__main__':
    main()
