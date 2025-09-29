#Napíš program, kt. má na vstupe dve čísla a vypíše hodnotu väčšieho z nich. Ak sú čísla rovnaké, text “sú rovnaké”

x = float(input("zadaj cislo  "))
y = float(input("zadaj druhe cislo  "))

if x == y:
    print("cisla su rovnake")
elif x > y:
    print("hodnota", x, "je vacsia")
else:
    print("hodnota", y, "je vacsia")