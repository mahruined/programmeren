import random 

naam = input("Wat is je naam? ")
hoeveel_complimenten = int(input("Hoeveel complimenten wil je? "))

lijst = ['je bent knap', 'je bent geweldig', 'je bent echt slim', 'je hebt wel een mooie outfit']
vorige_compliment = 0
for x in range(hoeveel_complimenten):
    randomcompliment = random.choice(lijst)
    while randomcompliment == vorige_compliment:
        randomcompliment = random.choice(lijst)
    if randomcompliment != vorige_compliment:
        print(f"{randomcompliment} {naam}")
    vorige_compliment = randomcompliment