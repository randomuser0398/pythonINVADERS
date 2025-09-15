import sys
import random
import pygame
from spaceship import Spaceship
from obstacle import Obstacle
from alien import Alien

pygame.init()

# CONFIGURAÇÕES
screen_width = 750
screen_height = 700
grey = (29, 29, 27)
max_waves = 5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Py Invasores do Espaço")

# SONS
pygame.mixer.music.load("Sounds/music.ogg")
pygame.mixer.music.play(-1)
laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")
explosion_sound = pygame.mixer.Sound("Sounds/explosion.ogg")

# FUNDO
background_raw = pygame.image.load("Graphics/background.png").convert()
background = pygame.transform.scale(background_raw, (screen_width, screen_height))

clock = pygame.time.Clock()

# NAVE
base_ship_speed = 5
spaceship = Spaceship(screen_width, screen_height, laser_sound)
spaceship_group = pygame.sprite.GroupSingle(spaceship)
spaceship_life = 5

# OBSTÁCULOS
obstacles = []
obstacle_positions = [screen_width / 5, screen_width / 2.5, screen_width / 1.7, screen_width / 1.2]
for pos in obstacle_positions:
    obstacle = Obstacle(pos, screen_height - 150)
    obstacles.append(obstacle)

# ALIENS
alien_types = [
    {"image": "Graphics/alien_1.png", "health": 1},
    {"image": "Graphics/alien_2.png", "health": 2},
    {"image": "Graphics/alien_3.png", "health": 3},
]

base_alien_speed = 2
wave_number = 1

def create_wave(speed_multiplier=1):
    aliens = pygame.sprite.Group()
    for row in range(len(alien_types)):
        # usa o tipo de alien de forma invertida
        alien_type = alien_types[len(alien_types) - 1 - row]
        for col in range(8):
            x = 80 + col * 70
            y = 50 + row * 60
            alien = Alien(x, y, alien_type["image"], screen_width, screen_height, health=alien_type["health"])
            alien.speed *= speed_multiplier
            aliens.add(alien)
    return aliens

aliens = create_wave(1)

# EVENTO: tiro dos aliens
ALIEN_SHOOT = pygame.USEREVENT + 1
pygame.time.set_timer(ALIEN_SHOOT, 500)

# GAME STATE
game_over = False
victory = False

font = pygame.font.SysFont(None, 30)

def draw_hud():
    # Vida da nave
    life_text = font.render(f"Life: {spaceship_life}", True, (255,0,0))
    screen.blit(life_text, (10, screen_height - 30))
    # Waves restantes
    waves_left = max_waves - wave_number + 1
    wave_text = font.render(f"Waves left: {waves_left}", True, (255,255,255))
    screen.blit(wave_text, (screen_width - 140, 10))

def reset_game():
    global aliens, wave_number, spaceship_life, game_over, victory, spaceship
    wave_number = 1
    spaceship_life = 5
    spaceship.speed = base_ship_speed
    spaceship.rect.midbottom = (screen_width/2, screen_height - 10)
    spaceship.lasers_group.empty()
    aliens = create_wave(1)
    for obstacle in obstacles:
        obstacle.blocks_group.empty()
        # recriar obstáculos
        for row in range(len(obstacle.blocks_group)):
            pass
    game_over = False
    victory = False

# LOOP PRINCIPAL
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == ALIEN_SHOOT and not game_over:
            if aliens.sprites():
                alien = random.choice(aliens.sprites())
                alien.shoot()
        if event.type == pygame.KEYDOWN:
            if game_over or victory:
                if event.key == pygame.K_r:
                    reset_game()

    if not game_over and not victory:
        # UPDATE
        spaceship_group.update()
        aliens.update()

        # COLISÕES
        for laser in spaceship_group.sprite.lasers_group:
            hit_aliens = pygame.sprite.spritecollide(laser, aliens, False)
            for alien in hit_aliens:
                if alien.hit():  # checa vida do alien
                    explosion_sound.play()
                    alien.kill()
                laser.kill()

        for alien in aliens:
            if pygame.sprite.spritecollide(spaceship_group.sprite, alien.lasers_group, True):
                spaceship_life -= 1
                if spaceship_life <= 0:
                    game_over = True

        for obstacle in obstacles:
            pygame.sprite.groupcollide(spaceship_group.sprite.lasers_group, obstacle.blocks_group, True, True)
            for alien in aliens:
                pygame.sprite.groupcollide(alien.lasers_group, obstacle.blocks_group, True, True)

        # CHECAGEM DE WAVE
        if len(aliens) == 0:
            if wave_number < max_waves:
                wave_number += 1
                aliens = create_wave(speed_multiplier=2 ** (wave_number-1))
                spaceship.speed = base_ship_speed + (wave_number - 1)
            else:
                victory = True

    # DESENHO
    screen.fill(grey)
    screen.blit(background, (0, 0))
    spaceship_group.draw(screen)
    spaceship_group.sprite.lasers_group.draw(screen)
    aliens.draw(screen)
    for alien in aliens:
        alien.lasers_group.draw(screen)
    for obstacle in obstacles:
        obstacle.blocks_group.draw(screen)
    draw_hud()

    # MENSAGEM DE FIM
    if game_over:
        over_text = font.render("GAME OVER! Press R to restart", True, (255,255,0))
        screen.blit(over_text, (screen_width/2 - 120, screen_height/2))
    if victory:
        win_text = font.render("YOU WIN! Press R to restart", True, (0,255,0))
        screen.blit(win_text, (screen_width/2 - 100, screen_height/2))

    pygame.display.update()
    clock.tick(60)
