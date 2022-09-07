#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Usuario
#
# Created:     06/09/2022
# Copyright:   (c) Usuario 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def suma(num1, num2):
    return num1+num2

def resta(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

num1 = int(input("ingrese el primer numero "))

resultado =(input("introduce la operacion (suma,resta,multiplicar)"))

while resultado != (suma,resta,multiplicar):
    print ("introduce una opcion valida")
    break
resultado =(input("introduce la operacion (suma,resta,multiplicar)"))

num2 = int(input("ingrese el segundo numero"))


if resultado=="suma":
    print ("el resultado es " + str(suma(num1,num2)))

if resultado=="resta":
    print ("el resultado es " + str(resta(num1,num2)))

if resultado=="multiplicar":
    print ("el resultado es " + str(multiplicar(num1,num2)))




if __name__ == '__main__':
    main()
