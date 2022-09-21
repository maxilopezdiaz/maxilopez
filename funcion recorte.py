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

def recortar (num,lim_inf,lim_sup):
    return max(min(num,lim_sup),lim_inf)


print (recortar (5,0,20))



if __name__ == '__main__':
    main()
