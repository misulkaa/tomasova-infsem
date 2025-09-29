#Napíš funkciu, kde a vstupe sú 3 čísla. Funkcia vypíše “je to trojuholnik” ak tieto čísla môžu byť stranami
#trojuholníka a a ak áno, tak akého (pravouhlého, rovnoramenného, rovnostranného ap.) funkcia vypíše
# “nie je to trojuholník” , ak strany nie sú stranami troj.(neplatí trojuholníková nerovnosť)

a = float(input("zadaj stranu a  "))
b = float(input("zadaj stranu b  "))
c = float(input("zadaj stranu c  "))

if a + b <= c or a + c <= b or b + c <= a:
    print("nie je to trojuholnik")
elif a == b == c:
    print( "je to rovnostranny trojuholnik")
elif a**2 + b**2 == c**2:
    print( "je to pravouhly trojuholnik")
elif a == b or a == c or b == c:
    print( "je to rovnoramenny trojuholnik")
else:
    print("je to trojuholnik")