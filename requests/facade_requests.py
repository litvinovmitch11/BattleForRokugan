from concurrent import futures
import grpc
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
        result = {"key": True}
        return pb2.Key(**result)


def serve():
    port = '5050'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_BasicServicer_to_server(BasicService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
