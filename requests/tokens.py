import pygame

pos = [
    [(1050, 200), (1050, 153), (980, 165), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1],  # 0
    [(1050, 153), (1050, 120), (980, 115), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1],  # 1
    [(980, 165), (980, 115), (920, 130), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1,
     -1, -1, -1, -1],  # 2
    [-1, -1, -1, (1050, 520), (980, 580), (980, 510), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1],  # 3
    [-1, -1, -1, (980, 580), (850, 600), (880, 530), (810, 530), (760, 600), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 4
    [-1, -1, -1, (980, 510), (880, 530), (930, 500), (920, 480), -1, -1, (990, 400), -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 5
    [-1, -1, -1, -1, (810, 530), (920, 480), (860, 450), (740, 490), (765, 440), (945, 380), (850, 400), -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 6
    [-1, -1, -1, -1, (760, 600), -1, (740, 490), (680, 600), (670, 480), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     (620, 530), (560, 620), -1, -1, -1, -1,
     -1, -1, -1, -1],  # 7
    [-1, -1, -1, -1, -1, -1, (765, 440), (670, 480), (680, 440), -1, (780, 390), -1, (730, 390), -1, -1, -1, -1, -1,
     (660, 415), -1, (640, 460), -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 8
    [-1, -1, -1, -1, -1, (990, 400), (945, 380), -1, -1, (940, 350), (895, 350), (870, 310), -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 9
    [-1, -1, -1, -1, -1, -1, (850, 400), -1, (780, 390), (895, 350), (850, 370), (820, 310), (770, 340), -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 10
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, (870, 310), (820, 310), (850, 270), (765, 260), -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 11
    [-1, -1, -1, -1, -1, -1, -1, -1, (730, 390), -1, (770, 340), (765, 260), (740, 280), (715, 260), -1, -1, -1, -1,
     (690, 350), -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 12
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (715, 260), (665, 270), (645, 240), -1, (620, 280), -1, (650, 300),
     -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 13
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (645, 240), (605, 220), (570, 200), (585, 260), -1, -1, -1, -1,
     -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 14
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (570, 200), (500, 190), (550, 250), -1, -1, -1, -1, -1, -1,
     -1, -1, -1,
     (500, 220), (460, 205), (460, 175), (465, 155)],  # 15
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (585, 260), (550, 250), (550, 300), (500, 340), (600, 310),
     (560, 330), -1, -1, -1, -1, -1, -1,
     (510, 290), -1, -1, -1],  # 16
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (620, 280), -1, (500, 340), (480, 370), -1, (515, 370), -1,
     -1, (480, 400), (415, 440), (400, 410), (410, 360),
     (460, 330), -1, -1, -1],  # 17
    [-1, -1, -1, -1, -1, -1, -1, -1, (660, 415), -1, -1, -1, (690, 350), (650, 300), -1, -1, (600, 310), -1, (650, 350),
     (615, 365), (630, 430), -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 18
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (560, 330), (515, 370), (615, 365), (570, 360),
     (585, 430), -1, (530, 425), -1, -1, -1,
     -1, -1, -1, -1],  # 19
    [-1, -1, -1, -1, -1, -1, -1, (620, 530), (640, 460), -1, -1, -1, -1, -1, -1, -1, -1, -1, (630, 430), (585, 430),
     (590, 470), (550, 520), (550, 450), -1, -1, -1,
     -1, -1, -1, -1],  # 20
    [-1, -1, -1, -1, -1, -1, -1, (560, 620), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (550, 520), (500, 580),
     (510, 470), (450, 540), -1, -1,
     -1, -1, -1, -1],  # 21
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (480, 400), -1, (530, 425), (550, 450),
     (510, 470), (460, 450), (440, 480), -1, -1,
     -1, -1, -1, -1],  # 22
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (415, 440), -1, -1, -1, (450, 540), (440, 480),
     (400, 520), (360, 530), -1,
     -1, -1, -1, -1],  # 23
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (400, 410), -1, -1, -1, -1, -1, (360, 530),
     (300, 500), (300, 380),
     -1, -1, -1, -1],  # 24
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (410, 360), -1, -1, -1, -1, -1, -1, (300, 380),
     (320, 320),
     (440, 280), (300, 260), -1, -1],  # 25
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (500, 220), (510, 290), (460, 330), -1, -1, -1, -1, -1,
     -1, -1, (440, 280),
     (470, 240), (450, 220), -1, -1],  # 26
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (460, 205), -1, -1, -1, -1, -1, -1, -1, -1, -1,
     (300, 260), (450, 220),
     (350, 225), (350, 180), -1],  # 27
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (460, 175), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     (350, 180),
     (280, 190), (350, 130)],  # 28
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (465, 155), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1,
     (350, 130), (320, 100)],  # 29
    [(1000, 250), (1000, 70), (870, 100), (1130, 500), -1, (1090, 450), -1, -1, -1, (950, 340), -1, (820, 220),
     (740, 200), (685, 200), (620, 150), (520, 160), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, (320, 50)]  # water
    ]


class battle_token:
    def __init__(self, screen, caste, status, typee, power, prov_from, prov_to):
        self.Token_Width = -5
        self.Token_Height = -5
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
                    if power == 1:
                        self.image = pygame.image.load('BattleForRokugan_content/crane_trooper_1.png')
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
                    if power == 1:
                        self.image = pygame.image.load('BattleForRokugan_content/unic_infantry_1.png')
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
        self.rect = pygame.Rect((pos[prov_from][prov_to])[0], (pos[prov_from][prov_to])[1], self.Token_Width,
                                self.Token_Height)
        self.screen_rect = screen.get_rect()

    def output(self):

        self.screen.blit(self.image, self.rect)


class control_token():
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
