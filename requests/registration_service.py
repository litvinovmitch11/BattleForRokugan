import registration_pb2 as pb2
import registration_pb2_grpc as pb2_grpc
import generate_pwd


class RegistrationService(pb2_grpc.RegistrationServicer):
    def __init__(self, *args, **kwargs):
        pass

    def AddUser(self, request, context):
        result = {"key": generate_pwd.add_user(request.login, request.password)}
        return pb2.Key(**result)

    def LoginUser(self, request, context):
        result = {"key": generate_pwd.login_user(request.login, request.password)}
        return pb2.Key(**result)

    def GetResult(self, request, context):
        list_res = pb2.ListResult(
            result=[pb2.Result(login=item[0], games=item[1], wins=item[2]) for item in generate_pwd.get_result()])
        return list_res

    def UpdateResult(self, request, context):
        generate_pwd.upd_result(request.login, request.final)
        return pb2.Empty()
