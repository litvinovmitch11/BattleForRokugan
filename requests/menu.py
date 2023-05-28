import pygame_menu
from pygame_menu.examples import create_example_window
from main_client import Client

surface = create_example_window('Example - Simple', (600, 400))


class ClientMenu:
    def __init__(self, host="localhost", port="8888"):
        self.client = Client(host=host, port=port)
        self.game_id = -1
        self.id = -1

    def create_lobby(self):
        self.game_id = self.client.create_new_game_session().game_id
        print(f"Your game id: {self.game_id}")

    def set_game(self, game_id):
        self.game_id = game_id
        print(f"Your game id: {self.game_id}")

    def start_game(self):
        self.id = self.client.get_unique_id().player_id
        self.client.add_player(self.id, self.game_id)
        self.client.swap_player_readiness_value(self.id, self.game_id)


client = ClientMenu(host="localhost", port="8888")

menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=400
)

menu.add.button('Create lobby', client.create_lobby)
# lobby_id = int(menu.add.text_input('Lobby ID: ', default=0, maxchar=10).get_value())
# menu.add.button('Set lobby', client.set_game(lobby_id))
menu.add.button('Start Game', client.start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
