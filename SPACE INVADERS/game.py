import pygame
import spaceship
class Game:
     def __init__(self):
    
         self.spaceship = Spaceship(self.screen_width, self.screen_height)
         self.spaceship_group = pygame.sprite.GroupSingle()
         self.spaceship_group.add(self.spaceship)
         self.obstacle = Obstacle(100, 100)

     