import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image_up = pygame.image.load('images/ship_up.png')
        self.image_down = pygame.image.load('images/ship_down.png')
        self.image_left = pygame.image.load('images/ship_left.png')
        self.image_right = pygame.image.load('images/ship_right.png')

        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
            self.image = self.image_right

        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
            self.image = self.image_left

        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
            self.image = self.image_up

        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.center_y += self.ai_settings.ship_speed_factor
            self.image = self.image_down

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
