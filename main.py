import pygame
from sys import exit
from player_right import PlayerR
from player_left import PlayerL
from ball import Ball

pygame.init()

screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong von Marki Mark')

player_R = PlayerR(screen, screen_width, screen_height)
player_L = PlayerL(screen, screen_width, screen_height)
ball = Ball(screen, screen_width, screen_height)
fps = pygame.time.Clock()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()
    screen.fill((0,0,0))
    fps.tick(60)

    player_R.update_player(player_R, player_L, ball, screen)

    pygame.display.update()