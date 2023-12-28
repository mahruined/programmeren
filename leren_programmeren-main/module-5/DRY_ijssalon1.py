while True:
    bolletjes = input("Hoeveel bolletjes wilt u bestellen? ")

    if bolletjes.isdigit():
        bolletjes = int(bolletjes)
        
        if bolletjes in range(1, 4):
            bakje_of_hoorntje = input("Wilt u een bakje of een hoorntje? ")
            print("Hier is uw ijsje in een " + str(bakje_of_hoorntje) + " met " + str(bolletjes) + " bolletjes.")
        elif bolletjes in range(4, 9):
            print("Hier is uw ijsje in een bakje met " + str(bolletjes) + " bolletjes.")
        elif bolletjes >= 9:
            print("Sorry, zulke grote bakken hebben we niet.")
            continue
        if bolletjes < 9:
            meer_bestellen = input("Wilt u meer bolletjes bestellen? (ja/nee) ")
            if meer_bestellen.lower() != "ja":
                print("Bedankt en tot ziens!")
                break  # Stop de loop als het antwoord geen "ja" is
    else:
        print("Sorry, dat snap ik niet.")
