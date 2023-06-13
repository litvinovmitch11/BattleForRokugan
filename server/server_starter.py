import sys
from concurrent import futures
from threading import Thread
import grpc

sys.path.append('../common/')
sys.path.append('../server/')
sys.path.append('../server/model/')
sys.path.append('../server/requests/')

from server_config import *
import facade_service
import facade_pb2_grpc as facade_pb2_grpc
import registration_service
import registration_pb2_grpc as registration_pb2_grpc


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
    t1 = Thread(target=registration_server, args=(HOSTDB, PORTDB,))
    t2 = Thread(target=game_server, args=(HOSTGM, PORTGM,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
