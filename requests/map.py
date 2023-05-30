import pygame

class Map:

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('BattleForRokugan_content/MAP31.jpg')
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect_centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect = pygame.Rect(250, 20, 600, 600)

    def output(self):
        self.screen.blit(self.image, self.rect)


class PlayersAbuility:
    def __init__(self, screen, caste):
        self.screen = screen
        self.caste = caste
        if caste == "unicorn":
            self.image = pygame.image.load('BattleForRokugan_content/unic-shirm.png')
        elif caste == "crab":
            self.image = pygame.image.load('BattleForRokugan_content/??')
        elif caste == "crane":
            self.image = pygame.image.load('BattleForRokugan_content/??')
        elif caste == "lion":
            self.image = pygame.image.load('BattleForRokugan_content/??')
        elif caste == "scorpion":
            self.image = pygame.image.load('BattleForRokugan_content/??')
        elif caste == "dragon":
            self.image = pygame.image.load('BattleForRokugan_content/??')
        elif caste == "phoenix":
            self.image = pygame.image.load('BattleForRokugan_content/??')
        self.rect = pygame.Rect(1000, 700, 200, 200)

    def output(self):
        self.screen.blit(self.image, self.rect)
