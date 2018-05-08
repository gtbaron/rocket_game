import pygame


class Rocket:

    def __init__(self, settings, screen):
        self.screen = screen
        self.ai_settings = settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def update(self):
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)
