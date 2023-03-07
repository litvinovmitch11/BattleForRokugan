# NOW JUST FOR TEST !!!
# Test server

from concurrent import futures
import grpc
import basic_pb2_grpc as pb2_grpc
import facade
import facade_service


def serve():
    port = '5050'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bd = facade.Board()
    fd = facade.Facade(bd)
    pb2_grpc.add_BasicServicer_to_server(facade_service.BasicService(fd), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
