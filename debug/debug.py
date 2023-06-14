import sys

sys.path.append('../server/model')
sys.path.append('../common')
sys.path.append('../server')

from facade import *

if __name__ == "__main__":
    local_p = have_land_way

    facade = GameFacade()
    for i in range(2):
        ind = facade.get_unique_id()
        facade.add_player(ind, "KAm" + str(ind), "login", "password")
    p = facade.get_players()
    players = []
    for player in p:
        facade.swap_player_readiness_value(player.player_id)
        players.append(player.player_id)
    for id_player in players:
        facade.set_caste(id_player, facade.get_free_caste()[0])

    while facade.get_round() != 1:
        id_player = facade.whose_move()
        if id_player == 0:
            for i in [24, 25, 26]:
                facade.put_control_token(0, i)
        r = random.randint(0, 29)
        if r in [24, 25, 26]:
            continue
        if facade.put_control_token(id_player, random.randint(0, 29)):
            # print("OK", id_player)
            pass
    for q in range(5):

        cas = dict()
        for id_player in players:
            cas[facade.board.players[id_player].caste] = []
        for token in facade.get_all_control_token():
            if token.province_id != -1:
                cas[token.caste].append(token)
        for cast in cas:
            print(cast, len(cas[cast]))

        print(facade.get_round(), facade.get_phase())
        while facade.get_phase() == 1:
            id_player = facade.whose_move()
            if id_player == 0:
                if facade.use_card(0, 1, list(map(int, input("Enter card data:\n").split()))):
                    print("USED!")
            facade.unused_card(id_player)
        # for player in players:
        #     print(len(facade.get_player_active(player)))
        # for token in facade.get_player_active(player):
        #     print(token.caste, end=" ")
        # print()
        while facade.get_phase() == 2:
            f = random.randint(0, 30)
            t = random.randint(0, 30)
            was = False

            active = []
            id_player = facade.whose_move()
            for battle_token in facade.board.players[id_player].active:
                ind = battle_token.id
                if facade.put_battle_token(id_player, ind, f, t):
                    # print("OK", str(id_player), ind)
                    was = True
                    break
        while facade.get_phase() == 3:
            for id_p in players:
                facade.swap_player_readiness_value(id_p)
    print(facade.get_score())
    print(facade.get_winner())
