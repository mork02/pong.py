import pygame

class Ball:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_widht = screen_width
        self.screen_height = screen_height
        self.x = self.screen_widht / 2
        self.y = self.screen_height / 2
        self.p1 = True
        self.p2 = False
        self.top = False
        self.bottom = True
        self.ball_is_moving = False
        self.first_hit = True
        self.score_playerl = 0
        self.score_playerr = 0
        self.space_text = True
        self.winner = False
        self.ball_speed = 0

    def get_winner(self,screen):
        if self.winner:
            if self.score_playerl == 9:
                press = pygame.font.Font(None, 50)
                pygame.draw.rect(screen, 'white', (self.screen_widht / 3 - 40, self.screen_height / 5 - 40, 440, 40))
                draw_press = press.render('WINNER IS PLAYER LEFT!', True, (0, 0, 0))
                screen.blit(draw_press, (self.screen_widht / 3 - 40, self.screen_height / 5 - 40))
            if self.score_playerr == 9:
                press = pygame.font.Font(None, 50)
                pygame.draw.rect(screen, 'white', (self.screen_widht / 3 - 40, self.screen_height / 5 - 40, 440, 40))
                draw_press = press.render('WINNER IS PLAYER RIGHT!', True, (0, 0, 0))
                screen.blit(draw_press, (self.screen_widht / 3 - 40, self.screen_height / 5 - 40))

    def draw_map_line(self,screen):
        pygame.draw.rect(screen, 'white', (self.screen_widht / 2 - 1, 0, 2, self.screen_height))

    def draw_press_button_text(self, screen):
        if not self.winner:
            if self.space_text:
                press = pygame.font.Font(None, 50)
                pygame.draw.rect(screen, 'white', (self.screen_widht / 3 - 30, self.screen_height / 5 - 40, 375,40))
                draw_press = press.render('Press "Space" to start!', True, (0, 0, 0))
                screen.blit(draw_press, (self.screen_widht / 3 - 30, self.screen_height / 5 - 40))

    def start_game(self):
        if not self.winner:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.ball_is_moving = True
                self.space_text = False

    def draw_score(self,screen):
        score_l = pygame.font.Font(None, 70)
        score_draw_l = score_l.render(str(self.score_playerl), True, (0,0,0))
        pygame.draw.rect(screen, 'white', (0,550, 45,45))
        screen.blit(score_draw_l, (5,550))

        score_r = pygame.font.Font(None, 70)
        score_draw_r = score_r.render(str(self.score_playerr), True, (0, 0, 0))
        pygame.draw.rect(screen, 'white', (self.screen_widht - 45, 550, 45, 45))
        screen.blit(score_draw_r, (995 - 30, 550))

    def draw_ball(self):
        pygame.draw.circle(self.screen, 'white', (self.x, self.y), 12)

    def movement_ball(self, playerr, playerl):
        if self.ball_is_moving:
            if self.p1:
                if self.ball_speed == 0:
                    self.x += 5
                elif self.ball_speed == 1:
                    self.x += 10
                elif self.ball_speed == 2:
                    self.x += 15
                elif self.ball_speed >= 3:
                    self.x += 20
                if self.x >= playerr.x and self.y >= playerr.y and self.y <= playerr.y + playerr.height:
                    self.p1 = False
                    self.p2 = True
                    self.first_hit = False
                    self.ball_speed += 1
                if self.x >= self.screen_widht - 60:
                    self.x = self.screen_widht / 2
                    self.y = self.screen_height / 2
                    self.score_playerl += 1
                    self.ball_is_moving = False
                    self.first_hit = True
                    self.space_text = True
                    self.ball_speed = 0

            if self.p2:
                if self.ball_speed == 0:
                    self.x -= 5
                elif self.ball_speed == 1:
                    self.x -= 10
                elif self.ball_speed == 2:
                    self.x -= 15
                elif self.ball_speed >= 3:
                    self.x -= 20
                if self.x <= playerl.x + playerl.width and self.y < playerl.y + playerl.height and self.y > playerl.y:
                    self.p1 = True
                    self.p2 = False
                    self.first_hit = False
                    self.ball_speed += 1
                if self.x <= 60:
                    self.x = self.screen_widht / 2
                    self.y = self.screen_height / 2
                    self.score_playerr += 1
                    self.ball_is_moving = False
                    self.first_hit = True
                    self.space_text = True
                    self.ball_speed = 0

            if not self.first_hit:
                if self.top:
                    if self.ball_speed <= 2:
                        self.y += 5
                    elif self.ball_speed >= 3:
                        self.y += 8
                    if self.y >= self.screen_height - 12:
                        self.top = False
                        self.bottom = True
                if self.bottom:
                    if self.ball_speed <= 2:
                        self.y -= 5
                    elif self.ball_speed >= 3:
                        self.y -= 8
                    if self.y <= 0 + 12:
                        self.top = True
                        self.bottom = False
            if self.score_playerr == 9 or self.score_playerl == 9:
                self.winner = True

    def update_ball(self, playerr, playerl, screen):
        self.draw_map_line(screen)
        self.get_winner(screen)
        self.draw_press_button_text(screen)
        self.draw_score(screen)
        self.start_game()
        self.draw_ball()
        self.movement_ball(playerr, playerl)