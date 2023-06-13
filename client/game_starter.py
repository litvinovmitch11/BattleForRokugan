import sys
from threading import Thread

sys.path.append('../common/')
sys.path.append('./requests/')
sys.path.append('./view/')
sys.path.append('../resources')

from facade_client import Client
from registration_client import RegistrationClient
from registration import Login
from menu import Menu
from view_model import Register, ViewModelSystem, ViewModelHand, ViewModelBoard
from game import run_game
from player_config import HOST, PORTDB, PORTGM

sys.path.append('../debug')
from console_view import ConsoleDraw


def draw(cl: Client, reg: Register, login, password):
    menu = Menu(cl, login, password)
    menu.create_menu()
    menu.run_menu()

    game_id, player_id, name = menu.get_params()
    vms = ViewModelSystem(game_id=game_id, player_id=player_id, client_object=cl)
    vmh = ViewModelHand(game_id=game_id, player_id=player_id, client_object=cl)
    vmb = ViewModelBoard(game_id=game_id, player_id=player_id, client_object=cl)

    # Pygame draw (comment cd and uncomment run_game)
    run_game(player_id, name, game_id, reg, vms, vmh, vmb)

    # Console draw (comment run_game and uncomment cd)
    # cd = ConsoleDraw(player_id, name, game_id, reg, vms, vmh, vmb)
    # cd.register()
    # cd.run()


def send(reg: Register, delay=0.1):
    reg.run(delay)


def registration_window_run(client: RegistrationClient):
    login_form = Login(client)
    login_form.run_form()

    return login_form.login, login_form.password


def game_window_run(client: Client, login='guest', password=''):
    result = False
    register = Register()

    t1 = Thread(target=draw, args=(client, register, login, password))
    t2 = Thread(target=send, args=(register,), daemon=True)

    t1.start()
    t2.start()

    t1.join()

    return result


if __name__ == "__main__":
    reg_client = RegistrationClient()
    my_login, my_password = registration_window_run(reg_client)

    game_client = Client()
    winner = game_window_run(game_client, my_login, my_password)
