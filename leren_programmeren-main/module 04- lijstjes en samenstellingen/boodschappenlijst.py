boodschappenlijst = {}
doorgaan = True
while doorgaan:
    producten = input('wat wilt u kopen? ').lower()
    hoeveelheid = int(input('hoeveel van het product wilt u? '))
    done = input('bent u klaar? ').lower()
    if producten in boodschappenlijst:
        boodschappenlijst[producten]+=hoeveelheid
    else:
            boodschappenlijst[producten]=hoeveelheid

    if done == 'ja':
        doorgaan = False
    else:
        doorgaan = True 
    
print('-[boodschappenlijst]-')   
print (boodschappenlijst)
print('___________________________________')

