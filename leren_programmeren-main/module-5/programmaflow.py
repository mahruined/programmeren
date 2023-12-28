from functies import bestel_ijs

while True:
    bestel_ijs()
    meer_bestellen = input("Wilt u meer bolletjes bestellen? (ja/nee) ")
    if meer_bestellen.lower() != "ja":
        print("Bedankt en tot ziens!")
        break