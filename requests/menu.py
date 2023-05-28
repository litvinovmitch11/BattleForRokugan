import pygame_menu
import start_game
from pygame_menu.examples import create_example_window
from typing import Tuple, Any

surface = create_example_window('Battle for Rokugan', (600, 400))


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    global user_name
    global lobby_id
    print(f'{lobby_id.get_value()}, Do the job here!')
    print(f'{user_name.get_value()}, Do the job here!')
    start_game.run()


def create_lobby() -> None:
    global lobby_id
    print(f'{lobby_id.get_value()}, Do the job here!')
    start_game.run()

    pass


menu = pygame_menu.Menu(
    height=400,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=600
)

user_name = menu.add.text_input('Name: ', default='Player', maxchar=10)
lobby_id = menu.add.text_input('Lobby ID: ', default='1', maxchar=10)
menu.add.button('Connect', start_the_game)
menu.add.button('Create lobby', create_lobby)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
