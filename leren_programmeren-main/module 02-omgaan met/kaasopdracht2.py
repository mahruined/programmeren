from tkinter import Y


geel = input("Is de kaas geel? (y/n)") 

if geel.lower() == "n":
    schimmel = input("heeft de kaas blauwe schimmel?(Y/N)")
    if schimmel == "y":
        korst = input("heeft de kaas een korst? (Y/N)")
        if korst == "y":
            print("Blue de Rochbaron")
        else:
            print("Foume d'Ambert") 
    else:
        korst2 = input("heeft de kaas een korst? (Y/N)")
        if korst2 == "y":
            print("Camembert")
        else:
            print("Mozzarella")
elif geel == "y":
    gaten = input("Zitten er gaten in? (Y/N)")
    if gaten == "y":
        duur = input("Is de kaas belachelijk duur? (Y/N)")
        if duur == "y":
            print("Emmenthaler")
        elif duur == "n":
            pitten = input("zitten er pitten in? (Y/N)")
            if pitten == "y":
                print ("komijnen")
            else: 
                print("Leerdammer")
    else:
        hard = input("Is de kaas hard als steen? (Y/N)")
        if hard == "y":
            print("Parmigiano Reggiano")
        else:
            print("Goudse kaas")
