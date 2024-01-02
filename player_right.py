import pygame.draw
class PlayerR:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = self.screen_width - 100
        self.y = self.screen_height / 3
        self.width = 20
        self.height = 160
        self.points = 0

    def draw_player(self):
        pygame.draw.rect(self.screen, 'white', (self.x, self.y, self.width, self.height))

    def movement_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not self.y <= 0 + 10:
            self.y -= 10
        if keys[pygame.K_DOWN] and not self.y >= self.screen_height - self.height - 10:
            self.y += 10

    def update_player(self, playerr, playerl, ball, screen):
        self.draw_player()
        playerl.update_playerl()
        self.movement_player()
        ball.update_ball(playerr, playerl, screen)


