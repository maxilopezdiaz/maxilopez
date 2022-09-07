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

email = False

usuario = input("ingrese su correo de email ")

for correo in usuario:
    if(correo=="@"):
        email = True

if email:
    print (f"el mail {usuario}  es correcto")

else:
    print (f"el email {usuario} es invalido")

if __name__ == '__main__':
    main()
