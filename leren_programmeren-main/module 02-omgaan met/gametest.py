import sys
import time
import extra
starttext = 'thats the spirit!!\n'+\
'now first things first let me give you a debrief of the situation real quick\n'+\
'the monster we are hunting today is called a Rathalos. Rathalos are large, bipedal wyverns with a spiny, armored hide covering their body.\n'+\
'Rathalos also possess a flame sac which is used to produce deadly flaming projectiles from the mouth. The talons upon their feet are highly poisonous and are known to inflict toxic mortal wounds on larger prey.\n'+\
'so you better be carefull not to get hit by any of those. it lives in the very depths of the acient forest fiercely protecting its territory,\n'
def print_delay(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.00)
health = 100
attackdamage = 10
health2 = 200
attackdamage2 = 60
enemyhealth = 20
enemyattackdamage = 5
rathalosHP = 120
rathalosHP2 = 120
rathalosDMG = 50
heal =  + 5
heal2 = + 50
print('''welcome to 
 _   _                                                     _     _ 
| | | |                                                   | |   | |
| |_| |__   ___   _ __   _____      __ __      _____  _ __| | __| |
| __| '_ \ / _ \ | '_ \ / _ \ \ /\ / / \ \ /\ / / _ \| '__| |/ _` |
| |_| | | |  __/ | | | |  __/\ V  V /   \ V  V / (_) | |  | | (_| |
 \__|_| |_|\___| |_| |_|\___| \_/\_/     \_/\_/ \___/|_|  |_|\__,_|
''')
print_delay ('''this is the new world a place where monsters roam the lands freely, from small insectoids to giant dragons,primates,dinosaurs and reptiles,\n''')
print_delay ('its a dangerous world out there are you sure you can do this (y/n)\n ')
start = input ()
if start == ('y'):
    print_delay(starttext)
    name = input('how rude of me ive never aske you for your name, mind if you tell me hunter\n')
    print_delay (f'ah {name}!! that name sounds like the name of a solid hunter. now off you go hunter\n')
else:
    print_delay ('''what a shame we could have used someone of your caliber\n''')
    import extra
    exit (0)
print_delay ('after flying for a while you start seeing glimpses of the Ancient forest\n')
print_delay ('while you fly above the ancient forest you start scouting the area from above for possible pathways\n')
print_delay ('after flying for a while you finally land and you waste no time you start stretching your legs and prepare for the hunt\n')
print_delay ('you finally leave camp and start heading for the plains of the ancient forest its unsually quiet with a distinct sound seemingly comming closer towards you \n ')
print_delay ('what do you decide to do (check out/hide)\n ')
Sound = input ()
if Sound == 'check out':
    print_delay ('you decide to check out whats going on \n')
    print_delay ('as you walk closer a huge group of monsters are all running past you seemingly ignoring you but why?\n')
    print_delay ('after a few seconds passed you understand why they were running away, they were being chased by a huge T-rex looking monster you quickly identify it as deviljho\n')
    print_delay ('Deviljho is an super apex predatory that roams the land in search of food for it ever lasting hunger \n')
    print_delay ('you decide to make a run for it but its futile the monster got to you and ate you up in one bite leaving nothing left for others to find \n')
    import extra
    exit(0)
elif Sound == ('hide'):
    print_delay ('your instincts tell you to hide and so you go hide behind a boulder out of sight\n')
    print_delay ('as you wait a few seconds you see a group of monster all running the same direction with a huge T-rex looking monster you identify as a deviljho chasing them \n')
    print_delay ('you are relieved you hid as fast as you did, if you took a few seconds longer you could have been dead, you decide to wait a bit until you cant hear the sounds of feet stomping the ground anymore \n')


print_delay ('you come out of hiding and start making your way towards the entrance of the forest\n')
print_delay ('you start walking into the forest and you see a group of small predators attacking what seems to look like a palico \n')

print_delay ('will you help the small palico? (y/n) \n')
help = input ()
if help == ('n'):
    print_delay ('you decide to leave it up to the little palicos faith and continue moving on\n ')
elif help == ('y'):
    print_delay ('you decide to help the poor palico and start fighting the group of small predators\n')
    print_delay ('you make a loud noise to attract the predators attention they all turn around and stare at you\n')
    print_delay ('battle starts\n')
    while True:
        if enemyhealth <= 0:
                break
        else:
            move = input ('do you want to attack or heal?')
            if move == 'attack':
                    enemyhealth = enemyhealth - attackdamage 
                    print_delay (f'you did {attackdamage} damage the enemy has {enemyhealth} health left\n ')
                    health = health - enemyattackdamage
                    print_delay (f'you took {enemyattackdamage} damage and you have {health} health left\n')
            elif move == 'heal':
                health = health + heal
                print_delay (f'you heal yourself and healed {heal} damage you have {health} health left ')
                health = health - enemyattackdamage
                print_delay (f'you took {enemyattackdamage} damage and you have {health} health left\n')
            else: 
                print_delay('choose a valid move\n')
    print_delay ('the hoard of monsters has been slain by your swift strikes\n')
    print_delay ('you saved the palico\n ')
    print_delay ('after healing its wounds and your own it decides to join you in your adventure \n')
print_delay ('as you walk through the forest you encounter 2 path ways\n')
print_delay ('you can either go to the left or to the right where do you go? (left/right)\n')
pathway = input ()
if pathway == 'right':
    print_delay ('you choose to follow the right path\n')
    print_delay ('as you keep walking through this path you start seeing an open field\n')
    print_delay ('as you continue walking towards to open area you see you arrive at a cliff, a dead end \n')
    print_delay ('just when you were about to turn around and backtrack a group of huge monsters corner you\n')
    print_delay ('while standing on the edge of the cliff cornered by monsters\n')
    print_delay ('you are trying to think of ways to get out of this situation but its futile, you are backed into a corner and the monsters got to close\n')
    print(extra.gameover)
    exit(0)
else:
    print_delay('you decide to go left\n')
    print_delay ('you continue to walk forward, you can see the den of the rathalos where your target resides\n')
    print_delay ('as you are at the foot of the Rathalos territory you can see your target fly towards its resting place, you decide to make a run for it and follow the beast\n')
    print_delay ('there you are at the resting place of the Rathalos, you steel your resolve and decide to engage in battle\n')
while health >0:
        move = print ('do you want to attack or heal?')
        move = input ()
        if move == 'attack':
                health = health - rathalosDMG
                print_delay (f'you did 0 damage to the rathalos it seems like its armor is too tough for you to strike through\n')
                print_delay (f'you took {rathalosDMG} damage and you have {health} health left\n')
        elif move == 'heal':
            health = health + heal
            print_delay (f'you heal yourself and healed {heal} damage you have {health} health left\n ')
            health = health - rathalosDMG
            print_delay (f'you took {rathalosDMG} damage and you have {health} health left\n')    
        else: 
            print_delay('choose a valid move\n')

print_delay('after a fierce battle you are on your last legs, as the rathalos is charging its final attack you start seeing your life flash before you\n ')
if help == 'y':
    print_delay ('just as you thought your life was over and you were about to die a surge of power starts flowing through you\n')
    print_delay ('you are wondering where this power comes from and start looking around  and you see its your partner\n')
    print_delay ('and thats when you realized that your partner palico has the ability to heal you and buff you for a short amount of time\n')
else:
    import extra
    exit(0) 
while True:
    if rathalosHP2 <= 0:
            break
    else:
        move = print ('do you want to attack or heal?')
        move = input ()
        if move == 'attack':
                rathalosHP2 = rathalosHP2 - attackdamage2
                print_delay (f'you did {attackdamage2} damage to the rathalos it has {rathalosHP2} health left\n')
                health2 = health2 - rathalosDMG
                print_delay (f'you took {rathalosDMG} damage and you have {health2} health left\n')
        elif move == 'heal':
            health2 = health2 + heal2
            print_delay (f'you heal yourself and healed {heal2} damage you have {health2} health left\n ')
            health2 = health2 - rathalosDMG
            print_delay (f'you took {rathalosDMG} damage and you have {health2} health left\n')
            
        else: 
            print_delay('choose a valid move\n')
print_delay ('you finally beat the fearsome beast and slain it after catching your breath you decide to take a trophy by cutting parts of the rathalos body to take home\n')
print_delay ('you also decide to take the palico home and make it your partner for life as its obvious after it saved your life\n')
print ('''
 _____ _   _  _____   _____ _   _______ 
|_   _| | | ||  ___| |  ___| \ | |  _  \ 
  | | | |_| || |__   | |__ |  \| | | | |
  | | |  _  ||  __|  |  __|| . ` | | | |
  | | | | | || |___  | |___| |\  | |/ / 
  \_/ \_| |_/\____/  \____/\_| \_/___/  
                                        
                                        
''')
