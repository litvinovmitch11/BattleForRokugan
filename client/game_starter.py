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


def draw(cl: Client, reg: Register):
    menu = Menu(cl)
    menu.create_menu()
    menu.run_menu()

    game_id, player_id, name = menu.get_params()
    vms = ViewModelSystem(game_id=game_id, player_id=player_id, client_object=cl)
    vmh = ViewModelHand(game_id=game_id, player_id=player_id, client_object=cl)
    vmb = ViewModelBoard(game_id=game_id, player_id=player_id, client_object=cl)
    reg.add(vms)
    run_game(player_id, name, game_id, reg, vms, vmh, vmb)  # Пока вот так вот рисуем...


def send(reg: Register, delay=0.1):
    reg.run(delay)


def registration_window_run(client: RegistrationClient):
    login_form = Login(client)
    login_form.run_form()

    return login_form.login


def game_window_run(client: Client):
    result = []

    register = Register()

    t1 = Thread(target=draw, args=(client, register,))
    t2 = Thread(target=send, args=(register,), daemon=True)

    t1.start()
    t2.start()

    t1.join()

    return result


if __name__ == "__main__":
    reg_client = RegistrationClient()
    my_login = registration_window_run(reg_client)

    game_client = Client()
    winner = game_window_run(game_client)

    if my_login != "guest":
        reg_client.update_result(my_login, False)
