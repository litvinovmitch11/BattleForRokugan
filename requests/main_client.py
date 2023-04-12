import grpc
import starter_pb2 as pb2
import starter_pb2_grpc as pb2_grpc

from all_include import Caste
from model import ControlToken


class Client(object):

    def __init__(self, port=8888):
        self.host = 'localhost'
        self.port = port
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.stub = pb2_grpc.StarterStub(self.channel)

    def get_unique_id(self):
        print("GetUniqueId")
        return self.stub.GetUniqueId(pb2.Empty())

    def add_player(self, player_id):
        print("AddPlayer")
        return self.stub.AddPlayer(pb2.PlayerId(player_id=player_id))

    def swap_player_readiness_value(self, player_id):
        print("SwapPlayerReadinessValue")
        return self.stub.SwapPlayerReadinessValue(pb2.PlayerId(player_id=player_id))

    def get_free_caste(self):
        print("GetFreeCaste")
        return self.stub.GetFreeCaste(pb2.Empty())

    def set_caste(self, player_id, caste):
        print("SetCaste")
        return self.stub.SetCaste(pb2.Caste(player_id=player_id, caste=caste))

    def get_possible_positions_control_token(self):
        print("GetPossiblePositionsControlToken")
        return self.stub.GetPossiblePositionsControlToken(pb2.Empty())

    def put_control_token(self, player_id, control_token, province_id):
        print("PutControlToken")
        token = pb2.ControlToken(visible=control_token.visible, on_board=control_token.on_board,
                                 power=control_token.power, caste=str(control_token.caste))
        return self.stub.PutControlToken(
            pb2.AddControlToken(player_id=player_id, control_token=token, province_id=province_id))

    def round_count(self):
        print("RoundCount")
        return self.stub.RoundCount(pb2.Empty())


if __name__ == '__main__':
    client = Client()

    # Debug client...
    # cmd - number of command from starter facade (or command name)
    # If you want to break client write -1

    your_id = -1
    cmd = input()
    while cmd != '-1':
        if cmd == '1' or cmd == 'get_unique_id':
            your_id = client.get_unique_id().player_id
            print(f'Your id: {your_id}')
        elif (cmd == '2' or cmd == 'add_player') and your_id != -1:
            key = client.add_player(your_id).key
            print(f'Add player with id {your_id}\nIs ok? {key}')
        elif (cmd == '3' or cmd == "swap_player_readiness_value") and your_id != -1:
            key = client.swap_player_readiness_value(your_id).key
            print(f'Correct? {key}')
        elif cmd == '4' or cmd == "get_free_caste":
            free_caste = client.get_free_caste().caste
            print(f'Free caste: {free_caste}')
        elif (cmd == '5' or cmd == 'set_caste') and your_id != -1:
            your_caste = input("Enter caste: ")
            key = client.set_caste(your_id, your_caste).key
            print(f'Correct? {key}')
        elif cmd == '6' or cmd == "get_possible_positions_control_token":
            list_token = client.get_possible_positions_control_token().token
            print(f'List of possible position control tokens: {list_token}')
        elif (cmd == '7' or cmd == "put_control_token") and your_id != -1:
            print("Enter control token parameters and province id: ")
            visible = bool(input("Visible: "))
            on_board = bool(input("On_board: "))
            power = int(input("Power: "))
            your_caste = input("Caste: ")
            your_province_id = int(input("Province id: "))

            your_token = ControlToken(Caste(your_caste), power)
            your_token.visible = visible
            your_token.on_board = on_board

            key = client.put_control_token(your_id, your_token, your_province_id).key
            print(f'Is correct? {key}')
        elif cmd == '8' or cmd == 'round_count':
            print(f'Current round is {client.round_count().round}')

        cmd = input()
