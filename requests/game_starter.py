from config import *
from menu import Menu
from view_model import *
from game import run_game
from threading import Thread
from register import Login


def draw(cl: Client, reg: Register):
    menu = Menu(cl)
    menu.create_menu()
    menu.run_menu()

    game_id, player_id, name = menu.get_params()
    vms = ViewModelSystem(game_id=game_id, player_id=player_id, client_object=client)
    vmh = ViewModelHand(game_id=game_id, player_id=player_id, client_object=client)
    vmb = ViewModelBoard(game_id=game_id, player_id=player_id, client_object=client)

    run_game(player_id, name, game_id, reg, vms, vmh, vmb)  # Пока вот так вот рисуем...


def send(reg: Register, delay=0.1):
    reg.run(delay)


if __name__ == "__main__":
    login_form = Login('Login', 600, 400)
    login_form.run_form()
    my_login = login_form.get_login()

    client = Client()  # host=HOST, port=PORT
    register = Register()

    t1 = Thread(target=draw, args=(client, register,))
    t2 = Thread(target=send, args=(register, 1,), daemon=True)

    t1.start()
    t2.start()

    t1.join()

    print("LOLOLOLOLOLOLOL")
