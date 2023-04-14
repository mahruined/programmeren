totaalpersonen = int (input ('met hoeveel zijn jullie '))
periode =int (input('hoeveel periodes zijn er in 1 sessie '))
toegangticket = 7.45 
tijdVIPVR = 45
PrijsVIPVR = 0.37

totaalprijs = round (tijdVIPVR / periode * PrijsVIPVR * totaalpersonen + (toegangticket * totaalpersonen), 2)

print ('dit geweldige dagje-uit met', totaalpersonen , 'mensen in de speel hal met 45 min vr kost je maar', totaalprijs , 'euro')
