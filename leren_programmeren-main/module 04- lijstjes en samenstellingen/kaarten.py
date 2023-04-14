import itertools
import random

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
deck = []
counter = 0
for suit in suits:
    for value in values:
        deck.append ( f'{value} {suit}' )
    deck.append("joker1")
    deck.append("joker2")
random.shuffle(deck)
for card in range (7):
    randomcard = deck.pop(0)
    counter += 1
    print(f"kaarten {counter} : {randomcard}")

print(deck)