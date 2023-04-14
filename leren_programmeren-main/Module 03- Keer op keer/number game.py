import random

score = 0
for ronden in range (1,21):
    number = random.randint(1,1001)
    geraden = 0
    getal_geraden = False
    while geraden <10 and not getal_geraden:
        getal = True
        while getal:
            try:
                print (number)
                raden = int(input("raad het getal tussen 1 en 1000 "))
                getal = False 
            except:
                print ("vul een geldig getal in")
            geraden += 1

            verschil = abs (number - raden)

            if raden == number:
                print ("je hebt het getal geraden!")
                score += 1
                getal_geraden = True
            else:
                if verschil <= 20:
                    print("je bent heel warm")
                elif verschil <= 50:
                    print("je bent warm")
                if number > raden:
                    print("Hoger")
                elif raden > number:
                    print("lager")



    if number != raden:
        print (f"je hebt het getal niet geraden het nummer was {number}")
    again = input(f"je hebt nu {ronden} rondes gespeeld, je hebt het getal {score} goed geraden, nog een keer? ")
    if again in ("Nee","n","no","nee"):
        print("doei")
        break


print (f"je hebt {ronden} rondes gespeeld, je eindscore is {score}")
print("doei")
        
                
