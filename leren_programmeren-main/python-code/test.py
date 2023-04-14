from operator import truediv


herhaaling = True
i = 0
while herhaaling:
    quit = input ('do you want to quit? ')
    if quit in  ['yes','y', 'quit', 'ja', 'j']:
        print('bedankt voor je tijd')
        print (f'je hebt {i} keren ingevuld')
        herhaaling = False
    else:
        i += 1