print('speeltuin entree')

# welkom voor kinderen van 12 of onder de 12, maar alleen met een begeleider van 20 of ouder
# of welkom als ze onder de 14 zijn en een speeltuinpasje hebben
# of welkom als ze een begeleider hebben met de naam Vladimir 

age = int (input ('wat is je leeftijd? '))
pasje = input ('heb je een pasje (y/n)? ')
begeleider = input ('heb je een begeleider met je (y/n)? ')
if begeleider == "y":  
  age_begeleider = int (input('wat is de leeftijd van de begeleider? '))
  naam_begeleider = input ('wat is de naam van de begeleider? ')
else:
  pass

# maak de conditie correct!
if age >= 12 and begeleider == 'y' and age_begeleider >= 20 or age == 14 and pasje == ('y') or naam_begeleider == 'vladimir':
  print('welkom')
else:
  print('sorry, niet welkom')
