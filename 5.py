#Napíš program, kt. zistí , či je číslo delitelné troma alebo nie

x = float(input(" zadaj cislo  "))

if x == 0:
    print("cislo nula neni detitelne")
elif x % 3 == 0:
    print("cislo je delitelne tromi")
else:
    print("cislo nie je delitelne tromi")
