import pygame
class PlayerL:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = 100
        self.y = self.screen_height / 3
        self.width = 20
        self.height = 160
        self.points = 0

    def movement_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and not self.y <= 0 + 10:
            self.y -= 10
        if keys[pygame.K_s] and not self.y >= self.screen_height - self.height - 10:
            self.y += 10

    def draw_player(self):
        pygame.draw.rect(self.screen, 'white', (self.x, self.y, self.width, self.height))

    def update_playerl(self):
        self.draw_player()
        self.movement_player()