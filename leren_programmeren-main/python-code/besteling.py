print('Hello, typ je besteling in')
croissantjes = int(input('hoeveel croissantjes wilt u?'))
crtotaal = croissantjes * 0.39
stokbrood = int(input('hoeveel stokbrood wilt u?'))
stoktotaal = stokbrood * 2.78
aantal_kortingsbonen = int(input('hoeveel kortings bonnen heeft uw?'))
korting = int(input('hoeveel cent zijn ze waard?'))
korting_total = aantal_kortingsbonen * korting / 100

totaal= stoktotaal + crtotaal - korting_total
print({totaal},'euro')