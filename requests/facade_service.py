import basic_pb2 as pb2
import basic_pb2_grpc as pb2_grpc
import facade


class BasicService(pb2_grpc.BasicServicer):

    def __init__(self, fd: facade.Facade, *args, **kwargs):
        self.facade = fd

    def Echo(self, request, context):
        print("Echo")
        message = request.message
        result = {"message": f"Your message: {message}"}
        return pb2.Message(**result)

    def PutControlToken(self, request, context):
        print("PutControlToken")
        result = {"key": self.facade.put_control_token(request.player_id, request.province_id)}
        return pb2.Key(**result)

    def RoundCount(self, request, context):
        print("RoundCount")
        result = {"count": self.facade.round_count()}
        return pb2.Count(**result)
