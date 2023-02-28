import basic_pb2 as pb2
import basic_pb2_grpc as pb2_grpc
import facade


class BasicService(pb2_grpc.BasicServicer):

    def __init__(self, *args, **kwargs):
        pass

    def Echo(self, request, context):
        print("Echo")
        message = request.message
        result = {"message": f"Your message: {message}"}
        return pb2.Message(**result)

    def PutControlToken(self, request, context):
        print("PutControlToken")
        print(f"Player id: {request.player_id}")
        print(f"Province id: {request.province_id}")
        # result = facade.Facade.put_control_token()
        result = {"key": True}
        return pb2.Key(**result)

    def RoundCount(self, request, context):
        print("RoundCount")
        # result = facade.Facade.round_count()
        result = {"count": 3}
        return pb2.Count(**result)
