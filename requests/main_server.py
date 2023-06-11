from concurrent import futures
from threading import Thread
import grpc
import facade_service
import registration_service
import facade_pb2_grpc
import registration_pb2_grpc


def game_server(host='localhost', port='8888'):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))

    games = dict()

    facade_pb2_grpc.add_FacadeServicer_to_server(facade_service.FacadeService(games), server)

    server.add_insecure_port(f'{host}:{port}')
    server.start()
    print("Game_server started, listening on " + port)
    server.wait_for_termination()


def registration_server(host='localhost', port='8889'):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))

    registration_pb2_grpc.add_RegistrationServicer_to_server(registration_service.RegistrationService(), server)

    server.add_insecure_port(f'{host}:{port}')
    server.start()
    print("Registration_server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    t1 = Thread(target=game_server, args=())
    t2 = Thread(target=registration_server, args=())

    t1.start()
    t2.start()
    t1.join()
    t2.join()
