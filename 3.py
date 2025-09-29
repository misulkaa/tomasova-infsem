#Napíš program, ktorý zistí, či dané číslo x patrí do intervalu <a,b>

a = float(input(" zadaj zaciatok intervalu  "))
b = float(input(" zadaj zkoniec intervalu "))
x = float(input(" zadaj cislo  "))

if a <= x <= b:
    print( "cislo do intervalu patri")
else:
    print( "cislo do intervalu nepatri")