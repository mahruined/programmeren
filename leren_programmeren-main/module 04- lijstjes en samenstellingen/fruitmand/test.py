from fruitmand import fruitmand

kleuren = {
    'yellow' : 'geel',
    'green' : 'groen',
    'orange' : 'oranje',
    'red' : 'rood',
    'brown' : 'bruin',
}

for i in range(len(fruitmand)):
    fruitmand[i] = fruitmand[i] | {'color': [kleuren[i]]}

max_lengte = 0
for i in fruitmand:
    if len((i)['name']) > max_lengte:
        max_lengte = len((i)['name'])
        name = i['name']
        kleur = i['color']
        gewicht = i['weight']
print(f'de {name} ({max_lengte} letters) heeft een {kleur} kleur en een gewicht van {gewicht}.')