import random

participants = []
ASKTHRESHHOLD = 3

loop = True
while loop:
    name = input('enter a name from one of the participants ')
    if name in participants:
        print('name already entered')
    else:
        participants.append(name)
        if len(participants) >= ASKTHRESHHOLD:
            another_name = input('do you want to enter another participant? ').lower()
            if another_name in ('nee','n','no'):
                loop = False

partners = []
random.shuffle(participants)
len_participants = len(participants)
for number in range (len_participants):
    index = (number +1 )% len_participants
    # print(index)
    partners.append(participants[index])
    # print(partners)


for i in range(len(partners)):
    print(participants[i], "drew", partners[i])