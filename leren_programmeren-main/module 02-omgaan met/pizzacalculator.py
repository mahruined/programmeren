print ('welkom bij dominos kan ik u bestelling opnemen')
#input dat vraagt hoeveel pizzas je wilt van elke grote
while True: 
    try:
        aantalsmallpizzas = int (input ('hoeveel kleine pizzas wilt u '))
        break
    except ValueError: print('gebruik hele getallen AUB.')
while True:
    try:
        aantalmediumpizzas = int (input ('hoeveel medium pizzas wilt u '))
        break
    except ValueError: print('gebruik hele getallen AUB')
while True:
    try:
        aantallargepizzas = int (input ('hoeveel grote pizzas wilt u '))
        break
    except ValueError: print('gebruik helen getallen AUB')

#groote van de pizza's en prijs
small = 5
medium = 7.50
large = 10

#calculatie voor de prijzen
totaalprijssmall = small * aantalsmallpizzas
totaalprijsmedium = medium * aantalmediumpizzas
totaalprijslarge = large * aantallargepizzas

#calculatie van de totaal prijs
totaalprijs = totaalprijssmall + totaalprijsmedium + totaalprijslarge
#de bonnetje
print ('--------------------------------------------------------------')
print ('                        dominos pizza      ')
print (aantalsmallpizzas, 'kleine pizzas', totaalprijssmall, 'euro')
print (aantalmediumpizzas,'medium pizzas', totaalprijsmedium, 'euro')
print (aantallargepizzas, 'large pizzas', totaalprijslarge, 'euro')
print ('het totaal prijs is', totaalprijs, 'euro')
print ('---------------------------------------------------------------')