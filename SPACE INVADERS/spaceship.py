import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, laser_sound):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("Graphics/spaceship.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.screen_width/2, self.screen_height - 10))
        self.speed = 5
        self.lasers_group = pygame.sprite.Group()
        self.laser_sound = laser_sound

    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_SPACE]:
            # Allow multiple shots by adding a cooldown
            if not hasattr(self, 'last_shot_time'):
                self.last_shot_time = 0
            current_time = pygame.time.get_ticks()
            cooldown = 300  # milliseconds between shots
            if current_time - self.last_shot_time > cooldown:
                laser = Laser(self.rect.center, 5, self.screen_height)
                self.lasers_group.add(laser)
                self.laser_sound.play()
                self.last_shot_time = current_time

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()

    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0
