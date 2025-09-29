#Naprogramuj funkciu, ktorá zistí, či je dané číslo párne.

x = float(input(" zadaj cislo  "))

if x == 0:
    print("cislo nula neni detitelne")
elif x % 2 == 0:
    print("cislo je parne")
else:
    print("cislo neni parne")