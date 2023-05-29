import pygame

pos = [[(1050, 200), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, (1050, 120), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, -1, (920, 130), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, -1, -1, (1050, 520), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, -1, -1, -1, (850, 600), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, -1, -1, -1, -1, (930, 500), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, -1, -1, -1, -1, -1, (860, 450), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, (680, 600), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, (680, 440), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, (940, 350), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (850, 370), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (850, 270), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (740, 280), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (665, 270), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (605, 220), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (500, 190), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (550, 300), -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (480, 370), -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (650, 350), -1, -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (570, 360), -1, -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (590, 470), -1, -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (500, 580), -1, -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (460, 450), -1, -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (400, 520), -1, -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (300, 500), -1,
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (320, 320),
        -1, -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        (470, 240), -1,
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        (350, 225),
        -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        (280, 190), -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, (320, 100)],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1]
       ]


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
        self.rect = pygame.Rect((pos[province][province])[0], (pos[province][province])[1], self.Token_Width,
                                self.Token_Height)
        self.screen_rect = screen.get_rect()

    def output(self):

        self.screen.blit(self.image, self.rect)
