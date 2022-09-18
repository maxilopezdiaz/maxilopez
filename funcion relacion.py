#-------------------------------------------------------------------------------
# Name:        module4
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

def relacion (num1,num2):

    if num1 > num2 :
        return 1

    elif num1 < num2 :
        return -1

    else:
        return 0

print (relacion(10,20))
print (relacion(40,30))
print (relacion(50,50))

if __name__ == '__main__':
    main()
