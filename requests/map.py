import pygame


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('BattleForRokugan_content/MAP31.jpg')
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect_centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect = pygame.Rect(250, 0, 600, 600)

    def output(self):
        self.screen.blit(self.image, self.rect)
