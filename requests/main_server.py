from concurrent import futures
import grpc
import starter_pb2_grpc
import facade_pb2_grpc

import facade
import starter_service
import facade_service


def start_game_session(host='localhost', port='8888'):

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    bd = facade.Board()
    start_fd = facade.StarterFacade(bd)
    game_fd = facade.GameFacade(bd)

    starter_pb2_grpc.add_StarterServicer_to_server(starter_service.StarterService(start_fd), server)
    facade_pb2_grpc.add_FacadeServicer_to_server(facade_service.FacadeService(game_fd), server)

    server.add_insecure_port(f'{host}:{port}')
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    start_game_session()
