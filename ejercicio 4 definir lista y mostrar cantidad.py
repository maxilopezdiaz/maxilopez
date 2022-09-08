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

colores = ["negro","blaco","gris","amarillo"]

def lista_de_colores(list):
    cantidad = 0
    for cantidaddecolores in list:
        cantidad += 1
    return cantidad

print("cantidad de colores: ", lista_de_colores(colores))

if __name__ == '__main__':
    main()
