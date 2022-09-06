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

    a = int(input("ingrese un numero impar "))
    while a % 2 == 0:
        a = int(input("ingrese un numero impar"))

print("ingreso un numero par")


if __name__ == '__main__':
    main()
