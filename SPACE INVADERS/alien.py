import pygame
from laser import Laser

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, screen_width, screen_height, health=1):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.direction = 1  # 1 → direita, -1 → esquerda
        self.lasers_group = pygame.sprite.Group()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.health = health

    def update(self):
        self.rect.x += self.speed * self.direction
        # Inverter direção e descer
        if self.rect.right >= self.screen_width or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 10
        self.lasers_group.update()

    def shoot(self):
        laser = Laser(self.rect.center, -5, self.screen_height)
        self.lasers_group.add(laser)

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True  # alien morreu
        return False
