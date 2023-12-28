import pygame
class Damage_Number(pygame.sprite.Sprite):
    def __init__(self, position, damage):
        super().__init__()
        self.font = pygame.font.Font(None, 24)
        self.damage = damage
        self.image = self.font.render(str(damage), True, (255, 0, 0))
        self.rect = self.image.get_rect(center=position)
        self.speed = pygame.math.Vector2(0, -1)  # Adjust the speed as needed

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.y < -self.rect.height:
            self.kill()