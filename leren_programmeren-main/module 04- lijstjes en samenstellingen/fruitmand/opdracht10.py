from fruitmand import fruitmand
from operator import itemgetter
fruitmand = sorted(fruitmand , key = itemgetter('weight'),reverse=True)
for fruit in fruitmand:
        print(fruit['name'],fruit['weight'])