import pygame

pygame.init()


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('../client/resources/MAP31.jpg')
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect_center_x = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect = pygame.Rect(250, 20, 600, 600)

    def output(self):
        self.screen.blit(self.image, self.rect)


class PlayersAbility:
    def __init__(self, screen, caste):
        self.screen = screen
        self.caste = caste
        self.image = pygame.image.load(f'../client/resources/{caste}_shirm.png')
        self.rect = pygame.Rect(1000, 700, 200, 200)

    def output(self):
        self.screen.blit(self.image, self.rect)


class Button:
    def __init__(self, screen, button_type, width, height):
        self.screen = screen
        self.button_type = button_type
        self.width = width
        self.height = height
        self.inactive_clr = (13, 162, 58)
        self.active_clr = (23, 204, 58)
        self.message = None
        self.clicked = False

    def draw(self, x, y):
        def print_text():
            f1 = pygame.font.Font(None, 36)
            color = (0, 77, 255)
            if self.button_type == 'UnuseCard':
                return f1.render('Unuse cards', True, color)
            elif self.button_type == 'ReadyButton':
                if self.clicked:
                    return f1.render('Ready', True, color)
                return f1.render('Not ready', True, color)
            elif self.button_type == 'ApplyButton':
                return f1.render('Apply', True, color)
            elif self.button_type == 'Choose_crab':
                if not self.clicked:
                    return f1.render('Choose Crab', True, color)
                return f1.render('', True, color)
            elif self.button_type == 'Choose_crane':
                if not self.clicked:
                    return f1.render('Choose Crane', True, color)
                return f1.render('', True, color)
            elif self.button_type == 'Choose_dragon':
                if not self.clicked:
                    return f1.render('Choose Dragon', True, color)
                return f1.render('', True, color)
            elif self.button_type == 'Choose_lion':
                if not self.clicked:
                    return f1.render('Choose Lion', True, color)
                return f1.render('', True, color)
            elif self.button_type == 'Choose_phoenix':
                if not self.clicked:
                    return f1.render('Choose Phoenix', True, color)
                return f1.render('', True, color)
            elif self.button_type == 'Choose_scorpion':
                if not self.clicked:
                    return f1.render('Choose Scorpion', True, color)
                return f1.render('', True, color)
            elif self.button_type == 'Choose_unicorn':
                if not self.clicked:
                    return f1.render('Choose Unicorn', True, color)
                return f1.render('', True, color)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.message = print_text()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(self.screen, self.active_clr, (x, y, self.width, self.height))
                self.screen.blit(self.message, (x, y))
                if click[0] == 1:
                    self.clicked = True
                    pygame.draw.rect(self.screen, (255, 160, 122), (x, y, self.width, self.height))
                    self.screen.blit(self.message, (x, y))
                    pygame.time.delay(300)
                    # if action is not None:
                    #  action()
        else:
            if not self.clicked:
                pygame.draw.rect(self.screen, self.inactive_clr, (x, y, self.width, self.height))
                self.screen.blit(self.message, (x, y))


COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Card:
    def __init__(self, screen, card_id, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.card_id = card_id
        if card_id == 1:
            self.image = pygame.image.load('../client/resources/get_2_ct_special_card.png')
        if card_id == 2:
            self.image = pygame.image.load('../client/resources/del_piece_special_card.png')
        if card_id == 3:
            self.image = pygame.image.load('../client/resources/del_burned_earth_special_card.png')
        if card_id == 4:
            self.image = pygame.image.load('../client/resources/replace_2_ct_special_card.png')
        if card_id == 5:
            self.image = pygame.image.load('../client/resources/harbor_special_card.png')
        if card_id == 6:
            self.image = pygame.image.load('../resources/battlefield_special_card.png')
        if card_id == 7:
            self.image = pygame.image.load('../client/resources/1_points_special_card.png')
        if card_id == 8:
            self.image = pygame.image.load('../client/resources/get_2_ct_to_1_prov_special_card.png')
        if card_id == 9:
            self.image = pygame.image.load('../client/resources/2_points_special_card.png')
        if card_id == 10:
            self.image = pygame.image.load('../client/resources/del_2_special_tokens_special_card.png')
        if card_id == 11:
            self.image = pygame.image.load('../client/resources/del_2_bt_special_card.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(x, y, 100, 200)

    def output(self):
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.screen.blit(self.image, self.rect)
