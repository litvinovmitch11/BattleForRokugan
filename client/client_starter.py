import sys
from threading import Thread

sys.path.append('../common/')
sys.path.append('../debug')
sys.path.append('../client/')
sys.path.append('../client/requests/')
sys.path.append('../client/view/')
sys.path.append('../client/view_model/')
sys.path.append('../resources/')

from player_config import *
from facade_client import Client
from registration_client import RegistrationClient
from registration import Login
from menu import Menu
from view_model import Register, ViewModelSystem, ViewModelHand, ViewModelBoard
from game import run_game
from console_view import ConsoleDraw


def draw(cl: Client, reg: Register, login, password):
    menu = Menu(cl, login, password)
    menu.create_menu()
    menu.run_menu()

    game_id, player_id, name = menu.get_params()
    vms = ViewModelSystem(game_id=game_id, player_id=player_id, client_object=cl)
    vmh = ViewModelHand(game_id=game_id, player_id=player_id, client_object=cl)
    vmb = ViewModelBoard(game_id=game_id, player_id=player_id, client_object=cl)

    if RUNKEY == "VIEW":
        run_game(player_id, name, game_id, reg, vms, vmh, vmb)
    elif RUNKEY == "CONSOLE":
        cd = ConsoleDraw(player_id, name, game_id, reg, vms, vmh, vmb)
        cd.register()
        cd.run()


def send(reg: Register, delay=0.1):
    reg.run(delay)


def registration_window_run(client: RegistrationClient):
    login_form = Login(client)
    login_form.run_form()

    return login_form.login, login_form.password


def game_window_run(client: Client, login='guest', password=''):
    register = Register()

    t1 = Thread(target=draw, args=(client, register, login, password,))
    t2 = Thread(target=send, args=(register,), daemon=True)

    t1.start()
    t2.start()

    t1.join()


if __name__ == "__main__":
    if DISABLE_REGISTRATION:
        game_client = Client(HOST, PORTGM)
        game_window_run(game_client)
    else:
        reg_client = RegistrationClient(HOST, PORTDB)
        my_login, my_password = registration_window_run(reg_client)

        game_client = Client(HOST, PORTGM)
        game_window_run(game_client, my_login, my_password)
