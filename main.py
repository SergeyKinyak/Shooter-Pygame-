import pygame
import sys

pygame.init()

STEP = 20
screen_fill_color = (32, 32, 42)
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Shotter game")

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()

fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and fighter_x >= STEP:
                fighter_x -= STEP
            if event.key == pygame.K_RIGHT and fighter_x <= screen_width - fighter_width - STEP:
                fighter_x += STEP
    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))

    pygame.display.update()
