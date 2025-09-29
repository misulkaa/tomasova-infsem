#Napíš program, kt. zistí, či je číslo delitelné štyrmi alebo siedmimi alebo nie je

x = float(input("zadaj cislo   "))

if x == 0:
    print("cislo nula nie je delitelne")
elif x % 4 == 0 and x % 7 == 0:
    print("cislo je delitelne styrmi a siedmimi")
elif x % 4 == 0:
    print("cislo je delitelne styrmi")
elif x % 7 == 0:
    print("cislo je delitelne siedmimi")
else:
    print("cislo neni delitelne styrmi ani siedmimi")
