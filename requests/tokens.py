import pygame


class battle_token:
    def __init__(self, screen, caste, status, typee, power):
        self.Token_Width = 30
        self.Token_Height = 30
        self.caste = caste
        self.status = status
        self.typee = typee
        self.power = power
        if caste == "crab":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
            else:
                if typee == "fleet":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "infantry":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "sugendzya":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "piece":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "pogrom":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
        elif caste == "crane":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
            else:
                if typee == "fleet":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "infantry":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "sugendzya":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "piece":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "pogrom":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
        elif caste == "lion":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
            else:
                if typee == "fleet":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "infantry":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "sugendzya":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "piece":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "pogrom":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
        elif caste == "scorpion":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
            else:
                if typee == "fleet":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "infantry":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "sugendzya":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "piece":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "pogrom":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
        elif caste == "unicorn":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
            else:
                if typee == "fleet":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "infantry":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "sugendzya":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "piece":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "pogrom":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
        elif caste == "dragon":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
            else:
                if typee == "fleet":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "infantry":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "sugendzya":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "piece":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "pogrom":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
        elif caste == "phoenix":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
            else:
                if typee == "fleet":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "infantry":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "sugendzya":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "piece":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
                elif typee == "pogrom":
                    self.image = pygame.image.load('BattleForRokugan_content/??.jpg')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def output(self):

        self.screen.blit(self.image, self.rect)


class control_token:
    def __init__(self, screen, caste, status, province):
        self.Token_Width = 16
        self.Token_Height = 16
        self.caste = caste
        self.status = status
        if caste == "crab":
            if status == 0:  # close
                self.image = pygame.image.load(
                    'BattleForRokugan_content/crab_close1.png')
            else:
                self.image = pygame.image.load('BattleForRokugan_content/crab_open1.png')
        elif caste == "crane":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/crane_close1.png')
            else:
                self.image = pygame.image.load('BattleForRokugan_content/crane_open1.png')
        elif caste == "lion":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/lion_close1.png')
            else:
                self.image = pygame.image.load('BattleForRokugan_content/lion_open1.png')
        elif caste == "scorpion":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/scorp_close1.png')
            else:
                self.image = pygame.image.load('BattleForRokugan_content/scorp_open1.png')
        elif caste == "unicorn":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/unic_close1.png')
            else:
                self.image = pygame.image.load('BattleForRokugan_content/unic_open1.png')
        elif caste == "dragon":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/drago_close1.png')
            else:
                self.image = pygame.image.load('BattleForRokugan_content/drago_open1.png')
        elif caste == "phoenix":
            if status == 0:  # close
                self.image = pygame.image.load('BattleForRokugan_content/phoenix_close1.png')
            else:
                self.image = pygame.image.load('BattleForRokugan_content/phoenix_open1.png')
        self.screen = screen
        x = [100, ...]  # эта и ниже - покоординатная отрисовка токена
        y = [100, ...]
        self.rect = pygame.Rect(x[province - 1], y[province - 1], self.Token_Width, self.Token_Height)
        self.screen_rect = screen.get_rect()

    def output(self):

        self.screen.blit(self.image, self.rect)
