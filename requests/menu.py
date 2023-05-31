import pygame_menu
from game import run_game
from pygame_menu.examples import create_example_window
from main_client import Client


class Menu:
    def __init__(self, size=(600, 400), host="localhost", port="8888"):
        self.surface = create_example_window('Battle for Rokugan', size)
        self.client = Client(host=host, port=port)
        self.client_id = -1
        self.user_name = None
        self.user_name_val = "Bob"
        self.lobby_id = None
        self.lobby_id_val = -1

        self.menu = pygame_menu.Menu(
            height=size[1],
            theme=pygame_menu.themes.THEME_BLUE,
            title='Welcome',
            width=size[0]
        )

    def start_game(self):
        self.user_name_val = self.user_name.get_value()
        self.client_id = self.client.get_unique_id().player_id
        self.client.add_player(self.client_id, self.lobby_id_val)
        print(f"My lobby number {self.lobby_id_val}")
        run_game()

    def set_lobby_id_and_start(self):
        self.lobby_id_val = self.lobby_id.get_value()
        self.start_game()

    def create_lobby_and_start(self):
        self.lobby_id_val = self.client.create_new_game_session().game_id
        self.start_game()

    def create_menu(self):
        self.user_name = self.menu.add.text_input('Name: ', default='Bob', maxchar=10)
        self.menu.add.button('Create lobby', self.create_lobby_and_start)
        self.lobby_id = self.menu.add.text_input('Lobby ID: ', default='0', maxchar=10)
        self.menu.add.button('Connect', self.set_lobby_id_and_start)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def run_menu(self):
        self.menu.mainloop(self.surface)


if __name__ == "__main__":
    menu = Menu()
    menu.create_menu()
    menu.run_menu()
