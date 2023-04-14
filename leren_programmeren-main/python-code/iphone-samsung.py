#inputs prijs
iphoneprijs = int(input ('hoeveel kost de iphone '))
samsungprijs = int(input ('hoeveel kost de samsung '))

#prijs verschil
verschil = iphoneprijs - samsungprijs

if iphoneprijs > samsungprijs:
    print (f'de iphone is het duurst de telefoon kost {iphoneprijs}')
