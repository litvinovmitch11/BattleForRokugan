# NOW JUST FOR TEST !!!
# Test client

import grpc
import basic_pb2 as pb2
import basic_pb2_grpc as pb2_grpc


class BasicClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 5050
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = pb2_grpc.BasicStub(self.channel)

    def send_message(self, message):
        message = pb2.Message(message=message)
        return self.stub.Echo(message)

    def put_control_token(self, player_id, province_id):
        context = pb2.PlayerProvinceId(player_id = player_id, province_id = province_id)
        return self.stub.PutControlToken(context)

    def round_count(self):
        return self.stub.RoundCount(pb2.Empty())


if __name__ == '__main__':
    client = BasicClient()

    result = client.put_control_token(player_id=312, province_id=31)
    print(result.key)

    result = client.send_message(message=input())
    print(f'{result.message}')

    result = client.round_count()
    print(result.count)
