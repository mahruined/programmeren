import pygame
import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.fullscreen = False
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('RPGtest')
        self.clock = pygame.time.Clock()

        self.level = Level()
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.50)
        main_sound.play(loops=-1)

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.level.toggle_menu()
                    elif event.key == pygame.K_f:
                        self.toggle_fullscreen()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
