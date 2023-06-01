from main_client import Client
from view_model import Game
from all_include import Caste

client1 = Client()
client2 = Client()
client3 = Client()

game_id = client1.create_new_game_session().game_id

client1_id = client1.get_unique_id(game_id=game_id).player_id
client1.add_player(player_id=client1_id, name="Pupa", game_id=game_id)
game1 = Game(game_id, client1_id)

client2_id = client2.get_unique_id(game_id=game_id).player_id
client2.add_player(player_id=client2_id, name="Lupa", game_id=game_id)
game2 = Game(game_id, client2_id)

client3_id = client3.get_unique_id(game_id=game_id).player_id
client3.add_player(player_id=client3_id, name="Aboba", game_id=game_id)
game3 = Game(game_id, client3_id)

client1.swap_player_readiness_value(player_id=client1_id, game_id=game_id)
client2.swap_player_readiness_value(player_id=client2_id, game_id=game_id)
client3.swap_player_readiness_value(player_id=client3_id, game_id=game_id)

game1.update_players(client1.get_players(game1.ind).name)
game2.update_players(client2.get_players(game2.ind).name)
game3.update_players(client3.get_players(game3.ind).name)

caste1 = client1.get_free_caste(game1.ind).caste[0]
if client1.set_caste(game1.my_player_id, caste1, game1.ind):
    caste = Caste(caste1)
    game1.players[game1.my_player_id].set_caste(caste)

caste2 = client2.get_free_caste(game2.ind).caste[0]
if client2.set_caste(game2.my_player_id, caste2, game2.ind):
    caste = Caste(caste2)
    game2.players[game2.my_player_id].set_caste(caste)

caste3 = client3.get_free_caste(game3.ind).caste[0]
if client3.set_caste(game3.my_player_id, caste3, game3.ind):
    caste = Caste(caste3)
    game3.players[game3.my_player_id].set_caste(caste)

for i in game1.players:
    print(i, game1.players[i].caste)
    # пупупууууу... Ошибка! Наша вью модель не знает про то, что обновились другие игроки
