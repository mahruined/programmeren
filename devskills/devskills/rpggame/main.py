import pygame
from pygame.locals import *
from level import Level
from player import Player

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame")

# Define colors
BLACK = (0, 0, 0)

# Game loop
running = True
clock = pygame.time.Clock()
player = Player()
level = Level()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update game logic
    player.update()

    # Render the game
    screen.fill(BLACK)
    level.draw(screen)
    screen.blit(player.image, player.rect)

    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()   