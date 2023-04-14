from fruitmand import fruitmand
kleuren = []
for fruit in fruitmand:
    if fruit['color'] not in kleuren:
        kleuren.append(fruit['color'])

    loop = True
while loop:
        kleur = input ('kies een kleur in de lijst, yellow, green, red, orange, brown ').lower()
        if kleur in kleuren:
            print(f'je hebt {kleur} gekozen')
            loop = False
        else:
            print('kies een kleur dat in de lijst staat')

rond = 0
niet_rond= 0 
for fruit in fruitmand:
    kleuren = fruit['color']
    if kleuren == kleur:
        fruit['round']
        if fruit['round'] == True:
            rond += 1 
        else:
            niet_rond += 1
print(f'er zijn {rond} rond(e) fruit')
print(f'er zijn {niet_rond} niet rond(e) fruit')            

if rond > niet_rond:
    print(f'er zijn {rond - niet_rond} meer ronde fruit dan niet ronde in {kleur}')
elif rond < niet_rond:
    print(f'er zijn {niet_rond - rond} meer niet ronde fruit dan ronde in {kleur}')
else:
    print(f'er zijn evenveel ronde fruit als niet ronde in {kleur}')
