import facade_pb2 as pb2
import facade_pb2_grpc as pb2_grpc
import facade


class FacadeService(pb2_grpc.FacadeServicer):

    def __init__(self, fd: facade.GameFacade, *args, **kwargs):
        self.facade = fd

    def Echo(self, request, context):
        print("Echo")
        message = request.message
        result = {"message": f"Your message: {message}"}
        return pb2.Message(**result)

    def RoundCount(self, request, context):
        print("RoundCount")
        result = {"count": self.facade.round_count()}
        return pb2.Count(**result)
