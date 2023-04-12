# NOW JUST FOR TEST !!!
# Test client

import grpc
import facade_pb2 as pb2
import facade_pb2_grpc as pb2_grpc


class BasicClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 5050
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = pb2_grpc.FacadeStub(self.channel)

    def send_message(self, message):
        message = pb2.Message(message=message)
        return self.stub.Echo(message)

    def round_count(self):
        return self.stub.RoundCount(pb2.Empty())


if __name__ == '__main__':
    client = BasicClient()

    result = client.send_message(message=input())
    print(f'{result.message}')

    result = client.round_count()
    print(result.count)
