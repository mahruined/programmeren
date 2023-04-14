
print ('Hallo typ je bestelling in')

croisantjesprijs = 0.39
aantalcroisantjes = int (input('hoeveel croisantjes wilt u '))
totaalprijscroisant = croisantjesprijs * aantalcroisantjes
prijsstokbrood = 2.78
aantalstokbrood = int (input('hoeveel stokbrood wilt u '))
totaalprijsstokbrood = prijsstokbrood * aantalstokbrood
kortingsbon = 0.50
korting_bonnen = int (input('hoeveel bonnen heeft u '))
korting_totaal = korting_bonnen * kortingsbon

totaal = round(totaalprijsstokbrood + totaalprijscroisant - korting_totaal, 2)

print('De feestlunch kost je bij de bakker', totaal, 'euro', 'voor de', aantalcroisantjes,'croisanten', 'en de', aantalstokbrood,'stokbrooden', 'als de', korting_bonnen, 'kortings bonnen nog geldig zijn'   )