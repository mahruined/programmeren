def vraag_aantal_bolletjes():
    while True:
        bolletjes = input("Hoeveel bolletjes wilt u bestellen? ")
        if bolletjes.isdigit():
            return int(bolletjes)
        else:
            print("Sorry, dat snap ik niet.")

def vraag_bakje_of_hoorntje():
    bakje_of_hoorntje = input("Wilt u een bakje of een hoorntje? ")
    return bakje_of_hoorntje

def bestel_ijs():
    bestellen = True
    while bestellen:
        aantal_bolletjes = vraag_aantal_bolletjes()
        if aantal_bolletjes in range(1, 4):
            bakje_of_hoorntje = vraag_bakje_of_hoorntje()
            print(f"Hier is uw ijsje in een {bakje_of_hoorntje} met {aantal_bolletjes} bolletjes.")
        elif aantal_bolletjes in range(4, 9):
            print(f"Hier is uw ijsje in een bakje met {aantal_bolletjes} bolletjes.")
        elif aantal_bolletjes >= 9:
            print("Sorry, zulke grote bakken hebben we niet.")
            continue
        bestellen = False

