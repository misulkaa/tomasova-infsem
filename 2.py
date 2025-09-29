#Napíš program, ktorý vráti prevrátenú hodnotu daného čísla. / t.j. 1/x

x = float(input("zadaj cislo na prevratenu hodnotu  "))
if x == 0:
    print("nulou nedelime")
else:
    print(1/x)