import pygame

pos = [
    [(1050, 220), (1050, 173), (980, 185), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1],  # 0
    [(1050, 173), (1050, 140), (980, 135), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1],  # 1
    [(980, 185), (980, 135), (920, 150), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1,
     -1, -1, -1, -1],  # 2
    [-1, -1, -1, (1050, 540), (980, 600), (980, 530), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1],  # 3
    [-1, -1, -1, (980, 600), (850, 620), (880, 550), (810, 550), (760, 620), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 4
    [-1, -1, -1, (980, 530), (880, 550), (930, 520), (920, 500), -1, -1, (990, 420), -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 5
    [-1, -1, -1, -1, (810, 550), (920, 500), (860, 470), (740, 510), (765, 460), (945, 400), (850, 420), -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 6
    [-1, -1, -1, -1, (760, 620), -1, (740, 510), (680, 620), (670, 500), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     (620, 550), (560, 640), -1, -1, -1, -1,
     -1, -1, -1, -1],  # 7
    [-1, -1, -1, -1, -1, -1, (765, 460), (670, 500), (680, 460), -1, (780, 410), -1, (730, 410), -1, -1, -1, -1, -1,
     (660, 435), -1, (640, 480), -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 8
    [-1, -1, -1, -1, -1, (990, 420), (945, 400), -1, -1, (940, 370), (895, 370), (870, 330), -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 9
    [-1, -1, -1, -1, -1, -1, (850, 420), -1, (780, 410), (895, 370), (850, 390), (820, 330), (770, 360), -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 10
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, (870, 330), (820, 330), (850, 290), (765, 280), -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 11
    [-1, -1, -1, -1, -1, -1, -1, -1, (730, 410), -1, (770, 360), (765, 280), (740, 300), (715, 280), -1, -1, -1, -1,
     (690, 370), -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 12
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (715, 280), (665, 290), (645, 260), -1, (620, 300), -1, (650, 320),
     -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 13
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (645, 260), (605, 240), (570, 220), (585, 280), -1, -1, -1, -1,
     -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 14
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (570, 220), (500, 210), (550, 270), -1, -1, -1, -1, -1, -1,
     -1, -1, -1,
     (500, 240), (460, 225), (460, 195), (465, 175)],  # 15
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (585, 280), (550, 270), (550, 320), (500, 360), (600, 330),
     (560, 350), -1, -1, -1, -1, -1, -1,
     (510, 310), -1, -1, -1],  # 16
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (620, 300), -1, (500, 360), (480, 390), -1, (515, 390), -1,
     -1, (480, 420), (415, 460), (400, 430), (410, 380),
     (460, 350), -1, -1, -1],  # 17
    [-1, -1, -1, -1, -1, -1, -1, -1, (660, 435), -1, -1, -1, (690, 370), (650, 320), -1, -1, (600, 330), -1, (650, 370),
     (615, 385), (630, 450), -1, -1, -1, -1, -1,
     -1, -1, -1, -1],  # 18
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (560, 350), (515, 390), (615, 385), (570, 380),
     (585, 450), -1, (530, 445), -1, -1, -1,
     -1, -1, -1, -1],  # 19
    [-1, -1, -1, -1, -1, -1, -1, (620, 550), (640, 480), -1, -1, -1, -1, -1, -1, -1, -1, -1, (630, 450), (585, 450),
     (590, 490), (550, 540), (550, 470), -1, -1, -1,
     -1, -1, -1, -1],  # 20
    [-1, -1, -1, -1, -1, -1, -1, (560, 640), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (550, 540), (500, 600),
     (510, 490), (450, 560), -1, -1,
     -1, -1, -1, -1],  # 21
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (480, 420), -1, (530, 445), (550, 470),
     (510, 490), (460, 470), (440, 500), -1, -1,
     -1, -1, -1, -1],  # 22
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (415, 460), -1, -1, -1, (450, 560), (440, 500),
     (400, 540), (360, 550), -1,
     -1, -1, -1, -1],  # 23
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (400, 430), -1, -1, -1, -1, -1, (360, 550),
     (300, 520), (300, 400),
     -1, -1, -1, -1],  # 24
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (410, 380), -1, -1, -1, -1, -1, -1, (300, 400),
     (320, 340),
     (440, 300), (300, 280), -1, -1],  # 25
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (500, 240), (510, 310), (460, 350), -1, -1, -1, -1, -1,
     -1, -1, (440, 300),
     (470, 260), (450, 240), -1, -1],  # 26
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (460, 225), -1, -1, -1, -1, -1, -1, -1, -1, -1,
     (300, 280), (450, 240),
     (350, 245), (350, 200), -1],  # 27
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (460, 195), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     (350, 200),
     (280, 210), (350, 150)],  # 28
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, (465, 175), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1,
     (350, 150), (320, 120)],  # 29
    [(1000, 270), (1000, 90), (870, 120), (1130, 520), -1, (1090, 470), -1, -1, -1, (950, 360), -1, (820, 240),
     (740, 220), (685, 220), (620, 170), (520, 180), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, (320, 70)],  # water
    [(600, 700), (700, 700), (800, 700), (600, 800), (700, 800), (800, 800)]  # hand
]
tokens_in_province = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bt_in_province = []
ct_in_province = []


class BattleToken:
    def __init__(self, screen, caste, visible, typee, power, prov_from, prov_to):
        self.Token_Width = -5
        self.Token_Height = -5
        self.caste = caste
        self.visible = visible
        self.typee = typee
        self.power = power
        if visible == "open":
            self.image = pygame.image.load(f'../resources/{caste}_{typee}_{power}.png')
        else:
            self.image = pygame.image.load(f'../resources/{caste}_bt_close.png')
        self.screen = screen
        self.rect = pygame.Rect((pos[prov_from][prov_to])[0], (pos[prov_from][prov_to])[1], self.Token_Width,
                                self.Token_Height)
        self.screen_rect = screen.get_rect()

    def output(self):
        bt_in_province.append(self)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.screen.blit(self.image, self.rect)


class ControlToken:
    def __init__(self, screen, caste, visible, province):
        self.Token_Width = 16
        self.Token_Height = 16
        self.caste = caste
        self.status = visible
        self.image = pygame.image.load(f'../resources/{caste}_{visible}1.png')
        self.screen = screen
        self.rect = pygame.Rect((pos[province][province])[0], (pos[province][province])[1], self.Token_Width,
                                self.Token_Height)
        self.screen_rect = screen.get_rect()

    def output(self):
        self.screen.blit(self.image, self.rect)


class SpecialToken:
    def __init__(self, screen, type, province):
        self.screen = screen
        self.type = type
        self.province = province
        self.image = pygame.image.load(f'../resources/{type}.png')
        self.rect = pygame.Rect((pos[province][province])[0], (pos[province][province])[1], 30, 30)
        self.screen_rect = screen.get_rect()

    def output(self):
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.screen.blit(self.image, self.rect)
