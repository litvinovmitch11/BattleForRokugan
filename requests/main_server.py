from concurrent import futures
import grpc
import starter_pb2_grpc
import facade_pb2_grpc

import facade
import facade_service
import starter_service


def start_game_session(port='8888'):
    # WARNINGWARNINGWARNINGWARNINGWARNINGWARNINGWARNING
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    # WARNINGWARNINGWARNINGWARNINGWARNINGWARNINGWARNING
    server.add_insecure_port('[::]:' + port)
    server.start()

    bd = facade.Board()
    start_fd = facade.StarterFacade(bd)
    fd = facade.GameFacade(bd)

    starter_pb2_grpc.add_StarterServicer_to_server(starter_service.StarterService(start_fd), server)
    facade_pb2_grpc.add_FacadeServicer_to_server(facade_service.FacadeService(fd), server)

    server.wait_for_termination()


if __name__ == '__main__':
    start_game_session()
