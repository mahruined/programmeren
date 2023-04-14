diepte = float (input('hoe diep moet het zwembad zijn? '))
lengte = float (input('hoe lang moet het zwembad zijn? '))
breedte = float (input('hoe breed moet het zwembad zijn? '))
kleur = input ('welke kleur tegels wilt u? ')
afstand = float (input('hoe ver woont u in KM? '))
hoeveelvierkantmeter = lengte * breedte * diepte
if afstand <50 and hoeveelvierkantmeter <20:
    prijsperkm = 1.25
elif afstand <=50 and hoeveelvierkantmeter <20:
    prijsperkm = 1.15
elif afstand <50 and hoeveelvierkantmeter <=20:
    prijsperkm = 2.15
else:
    prijsperkm = 2.05

kostenuitgraven = 25 * hoeveelvierkantmeter
kostenafvoerengrond = 32.50 * hoeveelvierkantmeter
kostenperkm = round (prijsperkm * afstand, 2)
if hoeveelvierkantmeter < 20 and kleur == 'rood':
    prijsperM = 250 * hoeveelvierkantmeter
    MeerprijsRoodPM = 25 * hoeveelvierkantmeter
    totaalprijs = kostenuitgraven + kostenafvoerengrond + kostenperkm + prijsperM + MeerprijsRoodPM
    print (f'uitgraven {kostenuitgraven}euro ')
    print (f'afvoeren grons {kostenafvoerengrond}euro')
    print (f'voorijkosten {kostenperkm}euro')
    print (f'beton + tegel {MeerprijsRoodPM}euro')
    print (f'totaal prijs is {totaalprijs}euro')

elif hoeveelvierkantmeter >= 20 and kleur == 'rood':
    prijsperM = 200 * hoeveelvierkantmeter
    MeerprijsRoodPM = 20 * hoeveelvierkantmeter
    totaalprijs = kostenuitgraven + kostenafvoerengrond + kostenperkm + prijsperM + MeerprijsRoodPM
    print (f'uitgraven {kostenuitgraven}euro ')
    print (f'afvoeren grons {kostenafvoerengrond}euro')
    print (f'voorijkosten {kostenperkm}euro')
    print (f'beton + tegel {MeerprijsRoodPM}euro')
    print (f'totaal prijs is {totaalprijs}euro') 

elif hoeveelvierkantmeter < 20 :
    prijsperM = 250 * hoeveelvierkantmeter
    MeerprijsKleurKeuze = 100
    totaalprijs = kostenuitgraven + kostenafvoerengrond + kostenperkm + prijsperM + MeerprijsKleurKeuze
    print (f'afvoeren grons {kostenafvoerengrond}euro')
    print (f'voorijkosten {kostenperkm}euro')
    print (f'beton + tegel {MeerprijsKleurKeuze}euro')
    print (f'totaal prijs is {totaalprijs}euro')
else:
    prijsperM = 200 * hoeveelvierkantmeter
    MeerprijsKleurKeuze = 125
    totaalprijs = kostenuitgraven + kostenafvoerengrond + kostenperkm + prijsperM + MeerprijsKleurKeuze
    print (f'afvoeren grons {kostenafvoerengrond}euro')
    print (f'voorijkosten {kostenperkm}euro')
    print (f'beton + tegel {MeerprijsKleurKeuze}euro')
    print (f'totaal prijs is {totaalprijs}euro')
