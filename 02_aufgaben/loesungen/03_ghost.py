from random import randint

geist = randint(1, 3)
print(geist)

brave = True
score = 0

print("Geisterspiel")

while brave:
    print("Vor dir sind drei Türen.")
    print("Hinter einer ist ein Geist.")
    print("Welche Tür öffnest du?")

    tuer = input("1, 2 oder 3? ")
    tuer_nummer = int(tuer)

    if tuer_nummer == geist:
        print("Es ist ein Geist!")
        brave = False
    else:
        print("Kein Geist!")
        score += 1

print("Laufe weg!")
print(f"Deine Punkte: {score}")
