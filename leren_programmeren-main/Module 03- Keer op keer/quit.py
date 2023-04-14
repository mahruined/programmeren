tries = 0

while True:
    vraag = input("?").lower()
    if vraag != "quit":
        tries = tries + 1
    else:
        print(f"De vraag werd {tries} keer gesteld")
        exit()
    
        
