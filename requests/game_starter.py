from config import HOST, PORT
from facade_client import Client
from registration_client import RegistrationClient
from registration import Login
from menu import Menu
from view_model import Register, ViewModelSystem, ViewModelHand, ViewModelBoard
from game import run_game
from threading import Thread


def draw(cl: Client, reg: Register):
    menu = Menu(cl)
    menu.create_menu()
    menu.run_menu()

    game_id, player_id, name = menu.get_params()
    vms = ViewModelSystem(game_id=game_id, player_id=player_id, client_object=cl)
    vmh = ViewModelHand(game_id=game_id, player_id=player_id, client_object=cl)
    vmb = ViewModelBoard(game_id=game_id, player_id=player_id, client_object=cl)

    run_game(player_id, name, game_id, reg, vms, vmh, vmb)  # Пока вот так вот рисуем...


def send(reg: Register, delay=0.1):
    reg.run(delay)


def registration_window_run(host='localhost', port='8889'):
    client = RegistrationClient(host=host, port=port)

    login_form = Login(client, 'Login', 600, 400)
    login_form.run_form()

    return login_form.get_login()


def game_window_run(host='localhost', port='8888'):
    result = []

    client = Client(host=host, port=port)
    register = Register()

    t1 = Thread(target=draw, args=(client, register,))
    t2 = Thread(target=send, args=(register, 1,), daemon=True)

    t1.start()
    t2.start()

    t1.join()

    return result


if __name__ == "__main__":
    my_login = registration_window_run()

    winner = game_window_run()  # host=HOST, port=PORT

    print(f"Game over! My login: {my_login}... Winner: {winner}")
