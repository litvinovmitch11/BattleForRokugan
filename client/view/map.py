import pygame

pygame.init()


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('../resources/MAP31.jpg')
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
        self.image = pygame.image.load(f'../resources/{caste}_shirm.png')
        self.rect = pygame.Rect(1000, 700, 200, 200)

    def output(self):
        self.screen.blit(self.image, self.rect)


'''class Button:
    def __init__(self, surface, color, x, y, length, height, width, text, text_color):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
    def create_button(self):
        surface = self.draw_button(self.surface, self.color, self.length, self.height, self.x, self.y, self.width)
        surface = self.write_text(surface, self.text, self.text_color, self.length, self.height, self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length // len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, True, text_color)
        surface.blit(myText, ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):
        for i in range(1, 10):
            s = pygame.Surface((length + (i * 2), height + (i * 2)))
            s.fill(color)
            alpha = (255 / (i + 2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i), width)
            surface.blit(s, (x - i, y - i))
        pygame.draw.rect(surface, color, (x, y, length, height), 0)
        pygame.draw.rect(surface, (190, 190, 190), (x, y, length, height), 1)
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print("Some button was pressed!")
                        return True
        return False
'''


class Button:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.inactive_clr = (13, 162, 58)
        self.active_clr = (23, 204, 58)

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(self.screen, self.active_clr, (x, y, self.width, self.height))

                if click[0] == 1:
                    print("Done")
                    pygame.draw.rect(self.screen, (255, 160, 122), (x, y, self.width, self.height))
                    pygame.time.delay(300)
                    if action is not None:
                        action()
        else:
            pygame.draw.rect(self.screen, self.inactive_clr, (x, y, self.width, self.height))


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
                elif event.key == pygame.K_BACKSPACE:
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
