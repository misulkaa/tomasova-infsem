#Napíš program, ktorý zistí, či dané číslo x je párne alebo nepárne

x = float(input(" zadaj cislo  "))

if x == 0:
    print("cislo nula neni detitelne")
elif x % 2 == 0:
    print("cislo je parne")
else:
    print("cislo neni parne")