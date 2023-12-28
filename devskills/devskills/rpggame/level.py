import pygame

class Level:
    def __init__(self):
        self.obstacles = pygame.sprite.Group()
        # Add your level design code here
        # Example: self.obstacles.add(Obstacle(x, y, width, height))

    def draw(self, screen):
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (255, 255, 255), obstacle.rect)