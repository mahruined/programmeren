diepte = float (input('hoe diep moet het zwembad zijn? '))
lengte = float (input('hoe lang moet het zwembad zijn? '))
breedte = float (input('hoe breed moet het zwembad zijn? '))
kleur = input ('welke kleur tegels wilt u? ')
afstand = float (input('hoe ver woont u in KM? '))
hoeveelkubiekemeter = lengte * breedte * diepte
ho
if afstand <50 and hoeveelkubiekemeter   <20:
    prijsperkm = 1.25
elif afstand <=50 and hoeveelkubiekemeter    <20:
    prijsperkm = 1.15
elif afstand <50 and hoeveelkubiekemeter     <=20:
    prijsperkm = 2.15
else:
    prijsperkm = 2.05

kostenuitgraven = 25 * hoeveelkubiekemeter  
kostenafvoerengrond = 32.50 * hoeveelkubiekemeter   
kostenperkm = round (prijsperkm * afstand, 2)
if hoeveelkubiekemeter   < 20 and kleur == 'rood':
    prijsperM = 250 * hoeveelkubiekemeter   
    MeerprijsRoodPM = 25 * hoeveelkubiekemeter  
    totaalprijs = kostenuitgraven + kostenafvoerengrond + kostenperkm + prijsperM + MeerprijsRoodPM
    print (f'uitgraven {kostenuitgraven}euro ')
    print (f'afvoeren grons {kostenafvoerengrond}euro')
    print (f'voorijkosten {kostenperkm}euro')
    print (f'beton + tegel {MeerprijsRoodPM}euro')
    print (f'totaal prijs is {totaalprijs}euro')

elif hoeveelkubiekemeter     >= 20 and kleur == 'rood':
    prijsperM = 200 * hoeveelkubiekemeter   
    MeerprijsRoodPM = 20 * hoeveelkubiekemeter  
    totaalprijs = kostenuitgraven + kostenafvoerengrond + kostenperkm + prijsperM + MeerprijsRoodPM
    print (f'uitgraven {kostenuitgraven}euro ')
    print (f'afvoeren grons {kostenafvoerengrond}euro')
    print (f'voorijkosten {kostenperkm}euro')
    print (f'beton + tegel {MeerprijsRoodPM}euro')
    print (f'totaal prijs is {totaalprijs}euro') 

elif hoeveelkubiekemeter     < 20 :
    prijsperM = 250 * hoeveelkubiekemeter   
    MeerprijsKleurKeuze = 100
    totaalprijs = kostenuitgraven + kostenafvoerengrond + kostenperkm + prijsperM + MeerprijsKleurKeuze
    print (f'afvoeren grons {kostenafvoerengrond}euro')
    print (f'voorijkosten {kostenperkm}euro')
    print (f'beton + tegel {MeerprijsKleurKeuze}euro')
    print (f'totaal prijs is {totaalprijs}euro')
else:
    prijsperM = 200 * hoeveelkubiekemeter   
    MeerprijsKleurKeuze = 125
    totaalprijs = kostenuitgraven + kostenafvoerengrond + kostenperkm + prijsperM + MeerprijsKleurKeuze
    print (f'afvoeren grons {kostenafvoerengrond}euro')
    print (f'voorijkosten {kostenperkm}euro')
    print (f'beton + tegel {MeerprijsKleurKeuze}euro')
    print (f'totaal prijs is {totaalprijs}euro')
