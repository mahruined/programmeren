from fruitmand import fruitmand
for fruit in fruitmand:
    roundness = fruit["round"]
    if roundness == True:
        print(fruit["name"])