from facade import *

if __name__ == "__main__":
    facade = GameFacade()
    for i in range(3):
        ind = facade.get_unique_id()
        facade.add_player(ind, "KAm" + str(ind))
    p = facade.get_players()
    players = []
    for player in p:
        facade.swap_player_readiness_value(player.player_id)
        players.append(player.player_id)
    for id_player in players:
        facade.set_caste(id_player, facade.get_free_caste()[0])

    while facade.get_round() != 1:
        was = False
        for i in range(1000):
            for id_player in players:
                if facade.put_control_token(id_player, i, i % 30):
                    print("OK", str(id_player), i)
                    was = True
                    break
            if was:
                break
    # print(facade.round_count(), facade.board.state.phase)

    for q in range(5):
        print(facade.get_round(), facade.board.state.phase)
        for i in range(10):
            for id_player in players:
                facade.unused_card(id_player)
        while facade.board.state.phase == 2:
            f = random.randint(0, 29)
            t = random.randint(0, 29)
            was = False
            for id_player in players:
                active = []
                for token in facade.board.battle_tokens.values():
                    if token.caste == facade.board.players[id_player].caste and token.in_active:
                        active.append(token)
                for battle_token in facade.board.players[id_player].active:
                    ind = battle_token.id
                    if facade.put_battle_token(id_player, ind, f, t):
                        print("OK", str(id_player), ind)
                        was = True
                        break
                if was:
                    break
        facade.do_execution_phase()
    print(facade.get_winner())
