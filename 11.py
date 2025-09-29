#Napíš funkciu, kde na vstupe sú tri čísla a funkcia vráti hodnotu najväčšieho z nich

a = float(input(" zadaj prve cislo  "))
b = float(input(" zadaj druhe cislo"  ))
c = float(input(" zadaj tretie cislo  "))

if a == b == c:
    print( "cisla su rovnake")
elif a > b > c or a > c > b:
    print(" najvacsie je ", a)
elif b > a > c or b > c > a:
    print("najvacsie cislo je ", b)
else:
    print("najvacsie cislo je ", c)