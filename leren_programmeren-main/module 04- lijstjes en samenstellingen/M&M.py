import random

kleuren = ["Oranje", "Blauw", "Groen", "Bruin","rood"]
hoeveelheid = int(input("Hoeveel M&m's? "))
zak = {}
for mms in range(4):
    value = random.randint(0,hoeveelheid)
    hoeveelheid -= value
    kleur = random.choice(kleuren)
    kleuren.remove(kleur)
    zak[kleur] = value


print(f"er zitten {zak} M&Ms in de zak")