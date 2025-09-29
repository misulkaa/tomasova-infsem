#Napíš funkciu, ktorá má na vstupe tri koeficienty a,b,c, ktoré sú koeficientami kvadratickej rovnice.
# Funkcia vypíše hodnoty korenov kvadratickej funkcie ax2+bx+c=0 , ak existujú

import math

a = float(input("koeficient a  "))
b = float(input("koeficient b  "))
c = float(input("koeficient c  "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print(x1, x2, "su korene")
elif D == 0:
    x = (-b / 2*a)
    print(x, "je koren")
else:
    print("v obore realnych cisel neexistuje riesenie")
