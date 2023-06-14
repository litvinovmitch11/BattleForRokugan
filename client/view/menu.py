import pygame_menu
import pygame
import sys
from pygame_menu.examples import create_example_window

from facade_client import Client


class Menu:
    def __init__(self, client_object: Client, login, password, size=(600, 400)):
        pygame.font.init()
        self.login = login
        self.password = password
        self.surface = create_example_window('Battle for Rokugan', size)
        self.client = client_object
        self.client_id = -1
        self.user_name = None
        self.user_name_val = "Juk"
        self.lobby_id = None
        self.lobby_id_val = -1

        self.menu = pygame_menu.Menu(
            height=size[1],
            theme=pygame_menu.themes.THEME_BLUE,
            title='Welcome',
            width=size[0]
        )

    def create_error_window(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
            f1 = pygame.font.Font(None, 30)
            text1 = f1.render('Connection lost...', True, (0, 0, 0))
            text2 = f1.render('Restart client and try again', True, (0, 0, 0))
            text3 = f1.render('Possible problems:', True, (0, 0, 0))
            text4 = f1.render('connection to the server lost, wrong lobby ID, etc...', True, (0, 0, 0))
            self.surface.fill((192, 192, 192))
            self.surface.blit(text1, (10, 50))
            self.surface.blit(text2, (10, 100))
            self.surface.blit(text3, (10, 150))
            self.surface.blit(text4, (10, 200))
            pygame.display.update()

    def start_game(self):
        self.user_name_val = self.user_name.get_value()
        self.client_id = self.client.get_unique_id(game_id=self.lobby_id_val).player_id
        self.client.add_player(player_id=self.client_id, name=self.user_name_val, game_id=self.lobby_id_val,
                               login=self.login, password=self.password)
        self.menu.disable()

    def set_lobby_id_and_start(self):
        self.lobby_id_val = int(self.lobby_id.get_value())
        try:
            self.start_game()
        except:
            self.create_error_window()

    def create_lobby_and_start(self):
        try:
            self.lobby_id_val = self.client.create_new_game_session().game_id
            self.start_game()
        except:
            self.create_error_window()

    def create_menu(self):
        self.user_name = self.menu.add.text_input('Name: ', default='Juk', maxchar=10)
        self.menu.add.button('Create lobby', self.create_lobby_and_start)
        self.lobby_id = self.menu.add.text_input('Lobby ID: ', default='0', maxchar=10)
        self.menu.add.button('Connect', self.set_lobby_id_and_start)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def run_menu(self):
        self.menu.mainloop(self.surface)

    def get_params(self):
        return self.lobby_id_val, self.client_id, self.user_name_val
