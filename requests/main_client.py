import grpc
import starter_pb2 as pb2
import starter_pb2_grpc as pb2_grpc


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


if __name__ == '__main__':
    client = Client()

    your_id = client.get_unique_id().player_id
    print(f'Your ID: {your_id}')

    key = client.add_player(your_id)
    if key:
        print("Good!")
    else:
        print("Your id has been added :(")

    key2 = client.add_player(your_id)
    if key2:
        print("Good!")
    else:
        print("Your id has been added :(")

    print(f'Your ID: {your_id}')
