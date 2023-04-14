
Appels = int (input ('hoeveel appels'))
appelkst = Appels * 3.40
druiven = int (input('hoeveel druiven'))
druivenkst = druiven * 2.45
bananen = int (input('hoeveel bananen'))
bananenkst = bananen * 1.95
totaalexBTW = appelkst + druivenkst + bananenkst
btw = float (totaalexBTW * 0.09)
totaalincBTW = btw + totaalexBTW
totaalincBTW_round = round(totaalincBTW,2)
print(totaalincBTW_round,'euro')

