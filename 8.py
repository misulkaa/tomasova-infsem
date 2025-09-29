#Napíš program, kt. vypíše, či je číslo kladné, záporné alebo nula

x = int(input("zadaj cislo"))

if x == 0:
    print("cislo je nula")
elif x % 2 == 0:
    print("cislo je kladne")
else:
    print("cislo je zaporne")