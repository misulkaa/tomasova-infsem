#Napíš program, vypíše, ak súčin dvoch ľubovoľných čísel “presiahol 100”  a ak nepresiahol, vypíše “nepresiiahol 100”

x = float(input("napis cinitela  "))
y = float(input("zapis druheho cinitela "))

z = x * y

if z < 100:
    print( z, "nepriesiahol 100")
else:
    print( z, "presiahlo 100")




