import pygame as pg
from main_client import Client
import pygame_menu
import grpc


class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pg.draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)


if __name__ == '__main__':
    pg.init()

    size = (800, 600)
    screen = pg.display.set_mode(size)
    ARIAL_50 = pg.font.SysFont('arial', 50)
    client = Client()
    menu = pygame_menu.Menu('Welcome', 1280, 720,
                            theme=pygame_menu.themes.THEME_BLUE)
    # menu = Menu()
    # menu.append_option('Add Player', client.add_player(client.get_unique_id()))
    # menu.append_option('Get Unique Id', client.get_unique_id())
    # menu.append_option('Get Ready', client.swap_player_readiness_value(client.get_unique_id()))
    menu.add.text_input('Name :', default='Battle For Rokugan')
    menu.add.button('Add Player', client.add_player(client.get_unique_id()))
    menu.add.button('Get Unique Id', client.get_unique_id())
    menu.add.button('Get Ready', client.swap_player_readiness_value(client.get_unique_id()))
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(pg.surface)

    # menu.append_option('Quit', quit)

    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_w:
                    menu.switch(-1)
                elif e.key == pg.K_s:
                    menu.switch(1)
                elif e.key == pg.K_SPACE:
                    menu.select()

        screen.fill((0, 0, 0))

        menu.draw(screen, 100, 100, 75)

        pg.display.flip()
    pg.quit()
