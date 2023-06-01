import starter_pb2 as pb2
import starter_pb2_grpc as pb2_grpc
from facade import StarterFacade
from facade import GameFacade


class StarterService(pb2_grpc.StarterServicer):

    def __init__(self, games, *args, **kwargs):
        self.games = games
        self.ind = -1

    def CreateNewGameSession(self, request, context):
        print("CreateNewGameSession")
        self.ind += 1
        self.games[self.ind] = StarterFacade()
        result = {"game_id": self.ind}
        return pb2.Empty(**result)

    def GetUniqueId(self, request, context):
        print("GetUniqueId")
        result = {"player_id": self.games[request.game_id].get_unique_id()}
        return pb2.PlayerId(**result)

    def AddPlayer(self, request, context):
        print("AddPlayer")
        result = {"key": self.games[request.game_id].add_player(request.player_id, request.name)}
        return pb2.Key(**result)

    def SwapPlayerReadinessValue(self, request, context):
        print("SwapPlayerReadinessValue")
        result = {"key": self.games[request.game_id].swap_player_readiness_value(request.player_id)}
        return pb2.Key(**result)

    def GetPlayers(self, request, context):
        print("GetPlayersIds")
        list_int = pb2.ListName(
            name=[pb2.Name(player_id=item[0], name=item[1]) for item in self.games[request.game_id].get_players()])
        return list_int

    def ShouldStartGame(self, request, context):
        print("ShouldStartGame")
        key = self.games[request.game_id].should_start_game()
        if key:
            self.games[request.game_id] = GameFacade(self.games[request.game_id].get_players_ids())
        result = {"key": key}
        return pb2.Key(**result)
