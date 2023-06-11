import grpc
import registration_pb2 as pb2
import registration_pb2_grpc as pb2_grpc


class RegistrationClient:
    def __init__(self, host='localhost', port='8889'):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.game_stub = pb2_grpc.RegistrationStub(self.channel)

    def add_user(self, login, password):
        return self.game_stub.AddUser(pb2.LoginInformation(login=login, password=password))

    def login_user(self, login, password):
        return self.game_stub.LoginUser(pb2.LoginInformation(login=login, password=password))

    def get_results(self):
        return self.game_stub.GetResult(pb2.Empty())

    def update_result(self, login, win):
        return self.game_stub.UpdateResult(pb2.Final(login=login, win=win))
