from menu import Menu
from view_model import *
from game import run_game
from threading import Thread


def draw(cl: Client, reg: Register):
    menu = Menu(cl)
    menu.create_menu()
    menu.run_menu()

    game_id, player_id, name = menu.get_params()
    vms = ViewModelSystem(game_id=game_id, player_id=player_id, client_object=client)
    vmh = ViewModelHand(game_id=game_id, player_id=player_id, client_object=client)
    vmb = ViewModelBoard(game_id=game_id, player_id=player_id, client_object=client)

    run_game(player_id, name, game_id, reg, vms, vmh, vmb)


def send(reg: Register):
    reg.run(1)


if __name__ == "__main__":
    client = Client()
    register = Register()

    t1 = Thread(target=draw, args=(client, register,))
    t2 = Thread(target=send, args=(register,))

    t1.start()
    t2.start()
