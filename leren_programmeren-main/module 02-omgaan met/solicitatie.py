name = input("Wat is uw naam?")
name = name.lower()
diploma = input("Heeft u een MBO-4 diploma ondernemen? (Y/N)")
bewijs = input("Heeft u een vrachtwagen rjibewijs? (Y/N)")
hoed = input("Heeft u een hoge hoed? (Y/N)")
man = input("Bent u een man? (Y/N)")
starsign = input("wat is je starsign")
jim = input("ga je naar de jim? (Y/N)")
if jim == "N":
    raise NameError("ga jimmen L+Bozo+Ratio")
if man == "Y":
    raise NameError('we hebben al teveel mannen in dit gebouw')
if starsign == 'aquarius':
    raise NameError('aquariuses zijn niet welkom')
if man == "Y":
    snor = int( input("Hoe breed is uw snor?(cm)") )

else:
    haar = input("Is uw haar rood en krullig(Y/N)")
    haar2 = int( input("Hoe lang is uw haar?(CM)") )

lengte = int( input("Hoe lang bent u? (CM)") )
gewicht = int (input("Hoe zwaar bent u? (KG)") )
certificaat = input("Heeft u het certificaat, 'overleven met gevaarlijk personeel'? (Y/N)")

ervaring = int( input("Hoeveel jaar heeft u evaring met dieren-dressuur?") )
ervaring2 = int( input("Hoeveel jaar heeft u ervaring met jongeleren?") )
ervaring3 = int( input("Hoeveel jaar ervaring heeft u met de acrobatiek?") )

score  = 0 #score teller voor de resultaten
if ervaring > 3 or ervaring2 > 4 or ervaring3 > 5:
 score +=1
if diploma == "y":
    score += 1

if bewijs == "y":
    score += 1

if hoed == "y":
    score += 1

if man == "y":
    if snor > 10:
        score += 1

if man == "n":
    if haar == "y":
        score += 1

    if haar2 > 20:
        score += 1

if lengte > 150:
    score += 1

if gewicht > 90:
    score += 1

if certificaat == "y":
    score += 1

if man == "y":
    if score>= 8:
        print("U mag gaan soliciteren!", score)
    else:
        print("U mag helaas niet gaan soliciteren!", score)

else:
    if score>= 9:
        print("U mag gaan soliciteren!", score)
    
    else:
        print("U mag helaas niet soliciteren", score)