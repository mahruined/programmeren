import random


score = 0
for rondes in range(1,21):
    nummer = random.randint(1,1000)
    for geraden in range(10):
        raden = int(input("Raad het getal tussen 1 en 1000  "))
        verschil = abs (nummer - raden)

        if nummer > raden:
            print("Hoger!")
        if raden > nummer:
            print("Lager!")
        elif raden == nummer:
            print("je hebt het geraden!")
            score += 1
            break

        if verschil <=20:
            print("Je bent heel warm!")
        elif verschil <=50:
            print("Je bent warm!")

    if nummer != raden:
        print("Je hebt het getal niet geraden!")
    if rondes == 20:
        print(f"Je hebt {rondes} rondes gespeeld! Je eindscore is {score}")

    opnieuw = input(f"Je score is nu {score}. Wil je nog een keer?")
    if opnieuw in ("No", "n","Nee","nee"):
        print(f"Je hebt {rondes} rondes gespeeld! Je eindscore is {score}")
        print("END")
        exit()


print(f"Je hebt {rondes} rondes gespeeld! Je eindscore is {score}")